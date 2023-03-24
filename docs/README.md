---
title: Guide
---

* Table of Contents
{:toc}

# Fridge Temperature Sensor Guide

## Raspberry Pi Zero
A simple IOT device with Raspberry Pi Zero W V1.1
Used to track fridge temperature using the DS18B20 Digital One-Wire temperature sensor directly soldered onto GPIO pins of the Raspberry Pi
Uses the telepota li ary to communicate with user via telegram group/private chat
- Uses can request for real time temperature anytime
- Daily reports of abnormal temperatures are also sent daily
Uses the google sheets API to directly update google sheets for temperature logging hourly

# Getting started

1. Clone this repositry to the home directory of the device
2. Copy ```T_log.json```, ```logs.json```, and all .sh files from this repositry to the home directory
3. In crontab, set start_temp.sh to run on every startup and make_run.sh every 5-10 mins or as desired 

# Changelog

V2.0 18 Feb 2022
+ Added webpage dashboard

V1.1 26 Jan 2022
+ Added refresh button

V1.0 29 Nov 2022
+ Ensure wi-fi is connected at all times
+ Local text file logging
V0.4 Beta
+ Bug Fixes that causes requests for temperature to throw error
+ Added Minimum / Maximum Tracker for the day (beta)
+ Added counter to track number of Abnormalities in a day
V0.3 Beta
+ Bug Fixes that causes error to be thrown during daily reports
- Removed unnecessary inline keyboard in telegram when making groupchat temperature requests
V0.2 Beta
+ Bug Fixes
Added exception catcher to prevent unexpected exit of program
Added Telegram Chat Bot to send to private user and groups 
Updated scheduler method instead of using datetime for daily reports
V0.1 Beta
 Initial Temperature Sensor recorder with only google sheets API and single command of temperature to telegram user (Private Chat)

## ESP32

ESP32 Version of Fridge Thermometer

# Getting Started
1. Download .zip file from https://github.com/witnessmenow/Universal-Arduino-Telegram-Bot
2. Add zip file to arduino ide library
3. Install ArduinoJson by Benoit Blanchon
4. Install DallasTemperature by Miles Burton
5. Install OneWire by Jim Studt et.al.
6. Install drivers for ESP32 if not done
7. Upload .ino file into ESP32

# Initial setup
1. Connect to ESP32-FTemp WiFi
2. Fill in necessary details
3. Get groupID from: https://api.telegram.org/bot[API_KEY from botfather]/getUpdates (begins with "id":-123456789)
4. Ready to use


# Changelog

V1.0
+ WiFi Browser setup 192.168.4.1
+ Inlinekeyboard to update message

V0.1
+ Ability to recieve temperature upon request via telegram bot
+ Ability to receive alerts when temperature out of desired range
ALL FUNCTIONALITY HAS NOT BEEN TESTED EXTENSIVELY YET BUGS MAY OCCUR

