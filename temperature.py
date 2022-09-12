import os
import glob
import time

import csv
from datetime import datetime
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

io.setmode(io.BCM)
led1 = 25
io.setup(led1, io.OUT)
p = io.PWM(led1, 90)

for i in range(0, 10):
    p.start(90)
    time.sleep(0.1)
    p.start(0)
    time.sleep(0.1)
#DHT_SENSOR = Adafruit_DHT.DHT22
#DHT_PIN = (4)
SERVICE_ACCOUNT_FILE = 'keys1.json'
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
cred = None
cred = service_account.Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE, scopes=SCOPES)

# If modifying these scopes, delete the file token.json.
# The ID and range of a sample spreadsheet.
SAMPLE_SPREADSHEET_ID = '1d6gqsvgL8D1Gw7kXl8QykNYYCjsF8Q1A2UkZUGHcJow'


def update_sheet(sheet_range, list_values, sheet):
    result = sheet.values().append(
        spreadsheetId=SAMPLE_SPREADSHEET_ID, range=sheet_range,
        valueInputOption="USER_ENTERED", body={"values": list_values})
    result.execute()
    return


def on_chat_message(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    if content_type == 'text':
        if msg['text'] == '/add_alert':
            chat_id_list.append(chat_id)
            bot.sendMessage(
                chat_id, f"Your id:{chat_id} is added, {chat_id_list}")
        elif msg['text'] == '/remove_alert':
            chat_id_list.remove(chat_id)
            bot.sendMessage(
                chat_id, f"Your id:{chat_id} is removed, {chat_id_list}")
        elif msg['text'] == '/start':
            bot.sendMessage(chat_id, 'Press button below', reply_markup=InlineKeyboardMarkup(inline_keyboard=[
                [InlineKeyboardButton(
                    text="Get Current Temp", callback_data='T')]
            ]
            ))
        elif msg['text'] == '/get_chatid':
            bot.sendMessage(
                chat_id, f"Your id: {chat_id} Chat id list: {chat_id_list}")
        else:
            bot.sendMessage(chat_id, "Try /add_alert, /remove_alert, /start")


def on_callback_query(msg):
    query_id, from_id, query_data = telepot.glance(
        msg, flavor='callback_query')
    if query_data == 'T':
        curr_temp = read_temp()
        bot.sendMessage(from_id, f"{curr_temp}*C")


def read_temp_raw():
    f = open(device_file, 'r')
    lines = f.readlines()
    f.close()
    return lines


def read_temp():
    lines = read_temp_raw()
    while lines[0].strip()[-3:] != 'YES':
        time.sleep(0.2)
        lines = read_temp_raw()
    equals_pos = lines[1].find('t=')
    if equals_pos != -1:
        temp_string = lines[1][equals_pos+2:]
        temp_c = float(temp_string) / 1000.0
        #temp_f = temp_c * 9.0 / 5.0 + 32.0
        return temp_c


def send():
    #f = open('temp.csv','a')
    #writer = csv.writer(f)
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S %d/%m/%Y")
    current_month = now.strftime("%B")
    # print(current_month)
    temp = read_temp()
    # print(temp)
    row = [current_time, f"{temp}"]
    service = build('sheets', 'v4', credentials=cred)
    sheet = service.spreadsheets()
    values = [row]
    update_sheet(f"{current_month}!A1", values, sheet)
    # writer.writerow(row)
    # f.close()


try:
    os.system('modprobe w1-gpio')
    os.system('modprobe w1-therm')
    base_dir = '/sys/bus/w1/devices/'
    device_folder = glob.glob(base_dir + '28*')[0]
    device_file = device_folder + '/w1_slave'
    p.start(90)
    time.sleep(0.2)
    print("Probe connected")
    p.start(0)
    print("Starting Service...")
    chat_id_list = []
    schedule.every().hour.at(":00").do(send)
    bot = telepot.Bot('5469401522:AAHh34PgJiZlgA0sq5NadCnOYjcvwMvp1LA')
    MessageLoop(bot, {'chat': on_chat_message,
                      'callback_query': on_callback_query}).run_as_thread()
    counter = True
    service = build('sheets', 'v4', credentials=cred)
    sheet = service.spreadsheets()
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S %d/%m/%Y")
    values = [["Service Booted", current_time]]
    update_sheet("Logs!A1", values, sheet)
    print("Service Started")
    print("Sending initial state...")
    send()
    print("Data sent!,Ready.")
    while 1:
        schedule.run_pending()
        try:
            p.start(15)
            time.sleep(0.2)
            p.start(0)
            time.sleep(3)
            current = read_temp()
            current = float(current)
        except KeyboardInterrupt:
            p.stop()
            io.cleanup()
            quit()
        if (current <= 2 and counter == False):
            for i in chat_id_list:
                bot.sendMessage(i, f"Low Temperature: {read_temp()}*C")
            counter = True
        if (current >= 8 and counter == False):
            for i in chat_id_list:
                bot.sendMessage(i, f"High Temperature: {read_temp()}*C")
            counter = True
        if (current > 2 and current < 8 and counter == True):
            for i in chat_id_list:
                bot.sendMessage(i, f"Normal Temperature: {read_temp()}*C")
            counter = False
except Exception as e:
    print(e)
