# Fridge Temperature Sensor
A simple IOT device with Raspberry Pi Zero W V1.1 <br />
Used to track fridge temperature using the DS18B20 Digital One-Wire temperature sensor directly soldered onto GPIO pins of the Raspberry Pi <br />
<br />
Uses the telepota library to communicate with users via telegram group/private chat <br />
- Uses can request for real time temperature anytime <br />
- Daily reports of abnormal temperatures are also sent daily <br />
<br />
Uses the google sheets API to directly update google sheets for temperature logging hourly <br />
<br />

# Changelog
V0.4 Beta (Latest Version)
\+ Bug Fixes that causes requests for temperature to throw error <br />
\+ Added Minimum / Maximum Tracker for the day (beta) <br />
\+ Added counter to track number of Abnormalities in a day <br />
<br />
V0.3 Beta
\+ Bug Fixes that causes error to be thrown during daily reports <br />
\- Removed unnecessary inline keyboard in telegram when making groupchat temperature requests <br />
<br />
V0.2 Beta
\+ Bug Fixes <br />
\+ Added exception catcher to prevent unexpected exit of program <br />
\+ Added Telegram Chat Bot to send to private user and groups <br />
\+ Updated scheduler method instead of using datetime for daily reports <br />
<br />
V0.1 Beta
\+ Initial Temperature Sensor recorder with only google sheets API and single command of temperature to telegram user (Private Chat) <br />
