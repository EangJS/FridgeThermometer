# Temperature Bug Fixes
import sys
import subprocess
import json
import os
import glob
import time
import urllib.request
import requests
import socket
from datetime import datetime
from tokenize import group
import schedule
import os.path
import RPi.GPIO as io
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from google.oauth2 import service_account
import telepot
from telepot.loop import MessageLoop
from telepot.namedtuple import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton


groupchatid = -761327315
p = subprocess.Popen([sys.executable, '/home/zeropi/FridgeThermometer/serve.py'],
                     stdout=subprocess.PIPE,
                     stderr=subprocess.STDOUT)

io.setmode(io.BCM)
led1 = 25
io.setup(led1, io.OUT)
p = io.PWM(led1, 90)
minimum = 100
maximum = -100
for i in range(0, 10):
    p.start(90)
    time.sleep(0.1)
    p.start(0)
    time.sleep(0.1)


SERVICE_ACCOUNT_FILE = 'keys1.json'
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
cred = None
cred = service_account.Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE, scopes=SCOPES)
SAMPLE_SPREADSHEET_ID = '1wPJGWEIItwlbYcbH3K586pipDY0JFe1QBFw5chFwF-Q'
TELEGRAM_TOKEN = '5469401522:AAG1L6SJ2rs94Z4j_tl8HCHNVnMWLcg81kc'


def update_sheet(sheet_range, list_values, sheet):
    try:
        result = sheet.values().append(
            spreadsheetId=SAMPLE_SPREADSHEET_ID, range=sheet_range,
            valueInputOption="USER_ENTERED", body={"values": list_values})
        result.execute()
        return
    except Exception as e:
        #bot.sendMessage(groupchatid, f"{e}")
        print(e)
        return


def check_internet():
    try:
        urllib.request.urlopen('https://www.google.com/')
        file1 = open("logs.txt", "r+")
        lines = file1.read().splitlines()
        while len(lines) > 5:
            lines.pop(0)
        now = datetime.now()
    except:
        try:

            print("Failed on first attempt, trying again...")
            time.sleep(5)
            urllib.request.urlopen('https://www.bing.com/')
            print("Passed on second attempt")
            lines.append(f"Connected successfully on second try: {now} \n")
            for i in lines:
                file1.write(i + '\n')
        except:
            try:
                print("Failed on second attempt, trying again...")
                time.sleep(10)
                urllib.request.urlopen('https://www.google.com/')
                print("Passed on third attempt")
                lines.append(f"Connected successfully on third try: {now} \n")
                for i in lines:
                    file1.write(i + '\n')
            except:
                print("Failed on all attempts.")
                now = datetime.now()
                lines.append(
                    f"Failed to connect at {now}. Attempted reboot \n")
                os.system("sudo reboot")
                for i in lines:
                    file1.write(i + '\n')


def on_chat_message(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    global edited
    global edited1
    curr_temp = read_temp()
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    if content_type == 'text':
        if msg['text'] == '/getPast':
            history = get_hx()
            bot.sendMessage(chat_id, history)
        if msg['text'] == '/start':
            bot.sendMessage(
                groupchatid, f"Fridge temperature at: {curr_temp} *C \n")
        if msg['text'] == '/temp':
            sent = bot.sendMessage(
                chat_id, f"Fridge temperature normal at: {curr_temp} *C \n")


def on_callback_query(msg):
    print(msg)

    query_id, from_id, query_data = telepot.glance(
        msg, flavor='callback_query')


def read_temp_raw():
    try:
        f = open(device_file, 'r')
        lines = f.readlines()
        f.close()
        return lines
    except Exception as e:
        print(e)


def read_temp():
    try:
        lines = read_temp_raw()
        if len(lines) != 0:
            while lines[0].strip()[-3:] != 'YES':
                time.sleep(0.2)
                lines = read_temp_raw()
            equals_pos = lines[1].find('t=')
            if equals_pos != -1:
                temp_string = lines[1][equals_pos+2:]
                temp_c = float(temp_string) / 1000.0
                #temp_f = temp_c * 9.0 / 5.0 + 32.0
                return temp_c
    except Exception as e:
        print(e)
        return float(999)


def send():
    try:
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        current_date = now.strftime("%d/%m/%Y")
        current_month = now.strftime("%B")
        temp = read_temp()
        row = [current_date, current_time, f"{temp}"]
        service = build('sheets', 'v4', credentials=cred)
        sheet = service.spreadsheets()
        values = [row]
        update_sheet(f"{current_month}!A1", values, sheet)
        print("sent")
    except Exception as e:
        print(e)


def get_hx():
    try:
        service = build('sheets', 'v4', credentials=cred)
        sheet = service.spreadsheets()
        result2 = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                     range="Main Page!A3:C26").execute()
        output = result2.get('values')
        string = "Past 12 Hours Readings:\n"
        for i in output:
            string += f"{i[0]} {i[1]} Temperature: {i[2]}*C\n"
        return string
    except Exception as e:
        print(e)


def high():
    print("hi")
    bot.sendMessage(groupchatid, f"Temperature above 8*C at {read_temp()}")


def low():
    print("low")
    bot.sendMessage(
        groupchatid, f"Temperature below 2*C at {read_temp()}")


var = False
status = False


def report():
    try:
        bot.sendMessage(
            groupchatid, f"""
Daily Update:
Maximum of {maximum}*C
Minimum of {minimum}*C

Use /getPast to get last 12 hours data

""")
    except Exception as e:
        print(e)


bot = telepot.Bot(TELEGRAM_TOKEN)
MessageLoop(bot, {'chat': on_chat_message,
                  'callback_query': on_callback_query}).run_as_thread()

try:
    os.system('modprobe w1-gpio')
    os.system('modprobe w1-therm')
    base_dir = '/sys/bus/w1/devices/'
    device_folder = glob.glob(base_dir + '28*')[0]
    device_file = device_folder + '/w1_slave'
    p.start(45)
    time.sleep(0.2)
    print("Probe connected")
    p.start(0)
    print("Starting Service...")
    schedule.every().hour.at(":30").do(send)
    schedule.every().hour.at(":00").do(send)
    service = build('sheets', 'v4', credentials=cred)
    sheet = service.spreadsheets()
    now = datetime.now()

    current_time = now.strftime("%H:%M:%S")
    current_date = now.strftime("%d/%m/%Y")
    values = [["Started at", current_date, current_time]]
    update_sheet("Logs!A1", values, sheet)
    print("Service Started")
    with open('logs.txt', 'r') as fin:
        data = fin.read().splitlines(True)
    with open('logs.txt', 'w') as fout:
        fout.writelines(data[1:])

    file1 = open("logs.txt", "a")
    now = datetime.now()
    file1.write(f"Service started at {now} \n")
    file1.close()
    #print("Sending initial state...")
    # send()
    #print("Data sent!,Ready.")
    schedule.every().day.at("21:30").do(report)
    while 1:
        time.sleep(5)
        check_internet()
        schedule.run_pending()
        now = datetime.now()
        current_datetime = now.strftime("%d/%m/%Y %H:%M:%S")
        current_time = now.strftime("%H:%M:%S")
        current_time_2 = now.strftime("%H:%M")
        if current_time_2 == "21:32":
            var = False
            maximum = -100
            minimum = 100
        try:
            p.start(35)
            time.sleep(0.2)
            p.start(0)
            time.sleep(3)
            current = read_temp()
        except KeyboardInterrupt:
            p.stop()
            io.cleanup()
            quit()
        if type(current) == type(None):  # safeguard
            print("Current == NoneType")
            continue

        with open('T_log.json', 'r+') as f:
            data = json.load(f)
            print(current)
            data['Time'] = current_datetime
            data['Temp'] = current
            f.seek(0)
            json.dump(data, f, indent=4)
            f.truncate()
        if current > maximum and current < 40:
            maximum = current
        if current < minimum and current > -20:
            minimum = current

        if current > 8 and status == False:
            schedule.every(5).minutes.do(high).tag('warnings')
            status = True
            var = True
        if current < 2 and status == False:
            schedule.every(5).minutes.do(low).tag('warnings')
            status = True
            var = True
        if (current <= 8 and current >= 2):
            schedule.clear('warnings')
            status = False

except Exception as e:
    #bot.sendMessage(groupchatid, f"{e}")
    print(e)
