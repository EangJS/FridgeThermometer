#include <OneWire.h>
#include <DallasTemperature.h>
#include <WiFi.h>
#include <WiFiClientSecure.h>
#include <UniversalTelegramBot.h>  // Universal Telegram Bot Library written by Brian Lough: https://github.com/witnessmenow/Universal-Arduino-Telegram-Bot
#include <ArduinoJson.h>
// GPIO where the DS18B20 is connected to
const int oneWireBus = 4;

// Setup a oneWire instance to communicate with any OneWire devices
OneWire oneWire(oneWireBus);

const char* ssid = "Sun tp-link";
const char* password = "Sun988788";
#define BOTtoken "5604437722:AAG64KjDlOd73HFpn-9AtUSABuxm-6KMcjQ"
#define GROUP_ID "-742836910"

WiFiClientSecure client;
UniversalTelegramBot bot(BOTtoken, client);

int botRequestDelay = 1000;
unsigned long lastTimeBotRan;
// Pass our oneWire reference to Dallas Temperature sensor
DallasTemperature sensors(&oneWire);
String keyboardJson = "[[{ \"text\" : \"Refresh\", \"callback_data\" : \"0001\" }]]";

void setup() {
  // Start the Serial Monitor
  Serial.begin(115200);
  WiFi.mode(WIFI_STA);
  WiFi.begin(ssid, password);
  client.setCACert(TELEGRAM_CERTIFICATE_ROOT);
  while (WiFi.status() != WL_CONNECTED) {
    delay(1000);
    Serial.println("Connecting to WiFi..");
  }
  // Print ESP32 Local IP Address
  Serial.println(WiFi.localIP());
  // Start the DS18B20 sensor
  sensors.begin();
}

void handleNewMessages(int numNewMessages) {
  for (int i = 0; i < numNewMessages; i++) {
    String chat_id = String(bot.messages[i].chat_id);
    String text = bot.messages[i].text;
    int message_id = bot.messages[i].message_id;
    Serial.println(text);
    String from_name = bot.messages[i].from_name;
    if (bot.messages[i].type == "callback_query")
    {
      String button_data = bot.messages[i].text;
      if(button_data == "0001"){
        sensors.requestTemperatures();
        float temperatureC = sensors.getTempCByIndex(0);
        String message = "Hello!, " + from_name + " Temperature is: " + String(temperatureC) + "ºC .\n";
        bot.sendMessageWithInlineKeyboard(chat_id, message, "", keyboardJson, message_id);
      }
    }
    else if(text == "/start"){
        bot.sendMessage(chat_id,"Send me /temp to get the fridge temperature!");
    } else if (text == "/temp"){
      sensors.requestTemperatures();
      float temperatureC = sensors.getTempCByIndex(0);
      String message = "Hello!, " + from_name + " Temperature is: " + String(temperatureC) + "ºC .\n";
      bot.sendMessageWithInlineKeyboard(chat_id, message,"", keyboardJson);
    }
    else {
        bot.sendMessage(chat_id,"Unknown input!");
    }
  }
}

void checkAlert(float temperatureC){
    while(temperatureC > 29.0){
      String message = "Warning High temperature "  + String(temperatureC) + "ºC .\n";
      Serial.println("High");
      bot.sendMessage(GROUP_ID, message, "");
      delay(10000);
      sensors.requestTemperatures();
      temperatureC = sensors.getTempCByIndex(0);
    }
    while(temperatureC < 2.0){
      String message = "Warning Low temperature "  + String(temperatureC) + "ºC .\n";
      Serial.println("Low");
      bot.sendMessage(GROUP_ID, message, "");
      delay(10000);
      sensors.requestTemperatures();
      temperatureC = sensors.getTempCByIndex(0);
    }
}

void loop() {
  int numNewMessages = bot.getUpdates(bot.last_message_received + 1);
  while (numNewMessages) {
      handleNewMessages(numNewMessages);
      numNewMessages = bot.getUpdates(bot.last_message_received + 1);
  }
  sensors.requestTemperatures();
  float temperatureC = sensors.getTempCByIndex(0);
  checkAlert(temperatureC);  
  delay(100);
}
