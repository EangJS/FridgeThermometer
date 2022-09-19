# Temperature V0.21 added exception handling
import os
import glob
import time

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
io.setmode(io.BCM)
led1 = 25
io.setup(led1, io.OUT)
p = io.PWM(led1, 90)
#minimum = int(103)
#maximum = int(103)

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


def update_sheet(sheet_range, list_values, sheet):
    try:
        result = sheet.values().append(
            spreadsheetId=SAMPLE_SPREADSHEET_ID, range=sheet_range,
            valueInputOption="USER_ENTERED", body={"values": list_values})
        result.execute()
        return
    except Exception as e:
        bot.sendMessage(groupchatid, f"{e}")
        print(e)
        return


def on_chat_message(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    if content_type == 'text':
        if msg['text'] == '/start':
            bot.sendMessage(chat_id, 'Press button below', reply_markup=InlineKeyboardMarkup(inline_keyboard=[
                [InlineKeyboardButton(
                    text="Get Current Temp", callback_data='T')]
            ]
            ))
        if msg['text'] == '/temp':
            bot.sendMessage(chat_id, read_temp())


def on_callback_query(msg):
    query_id, from_id, query_data = telepot.glance(
        msg, flavor='callback_query')
    if query_data == 'T':
        curr_temp = read_temp()
        bot.sendMessage(groupchatid, f"{curr_temp}*C")


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


def high():
    bot.sendMessage(groupchatid, f"Temperature above 8 at {read_temp()}")


def low():
    bot.sendMessage(
        groupchatid, f"Testing Temperature below 2 at {read_temp()}")


def report(info):
    try:
        if info == True:
            bot.sendMessage(
                groupchatid, f"Daily Update: Abnormal Temperature detected today")
        else:
            bot.sendMessage(
                groupchatid, f"No abnormal temperatures detected today")
    except Exception as e:
        print(e)


bot = telepot.Bot('5469401522:AAG1L6SJ2rs94Z4j_tl8HCHNVnMWLcg81kc')
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
    schedule.every().hour.at(":00").do(send)
    service = build('sheets', 'v4', credentials=cred)
    sheet = service.spreadsheets()
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    current_date = now.strftime("%d/%m/%Y")
    values = [["Service Booted", current_date, current_time]]
    update_sheet("Logs!A1", values, sheet)
    print("Service Started")
    print("Sending initial state...")
    send()
    print("Data sent!,Ready.")
    status = False
    daily = False
    schedule.every().day.at("21:30").do(report, info=daily)
    while 1:
        schedule.run_pending()
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        if now.strftime("%H:%M") == "21:32":
            daily = False
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
        if current > 8 and status == False:
            bot.sendMessage(groupchatid, "High Temperature")
            schedule.every(15).minutes.do(high).tag('warnings')
            status = True
            daily = True
        if current < 2 and status == False:
            bot.sendMessage(groupchatid, "Low Temperature")
            schedule.every(15).minutes.do(low).tag('warnings')
            status = True
            daily = True
        if (current <= 8 and current >= 2):
            schedule.clear('warnings')
            status = False

except Exception as e:
    bot.sendMessage(groupchatid, f"{e}")
    print(e)
