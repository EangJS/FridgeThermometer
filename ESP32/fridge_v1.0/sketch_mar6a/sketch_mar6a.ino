#include <OneWire.h>
#include <DallasTemperature.h>
#include <WiFi.h>
#include <HTTPClient.h>
#include <WebServer.h>
#include <EEPROM.h>
#include <WiFiClientSecure.h>
#include <UniversalTelegramBot.h>  // Universal Telegram Bot Library written by Brian Lough: https://github.com/witnessmenow/Universal-Arduino-Telegram-Bot
#include <ArduinoJson.h>
#include <time.h>

const int oneWireBus = 4;
OneWire oneWire(oneWireBus);
int i = 0;
int statusCode;
const char* ssid = "";
const char* passphrase = "";
String st;
String content;
String esid ="";
String epass = "";
String BOTtoken = "";
String ekey = "";
String eid = "";
String GROUP_ID = "";
WiFiClientSecure client;
WebServer server(80);
int botRequestDelay = 1000;
unsigned long lastTimeBotRan;
DallasTemperature sensors(&oneWire);
UniversalTelegramBot bot(BOTtoken, client);
const char* ntpServer = "pool.ntp.org";
const long  gmtOffset_sec = 28800;
const int   daylightOffset_sec = 0;

void setup() {
  // Start the Serial Monitor
  Serial.begin(115200);
  WiFi.mode(WIFI_STA);
  client.setCACert(TELEGRAM_CERTIFICATE_ROOT);
  EEPROM.begin(512);
  sensors.begin();
  for (int i = 0; i < 32; ++i){
    esid += char(EEPROM.read(i));
  }
  for (int i = 32; i < 96; ++i){
    epass += char(EEPROM.read(i));
  }
  for (int i = 96; i < 142; ++i){
    ekey += char(EEPROM.read(i));
  }
  for (int i = 142; i < 152; ++i){
    eid += char(EEPROM.read(i));
  }
  if(ekey.length() > 0){
    bot.updateToken(ekey);
  }
  if(eid.length() == 10){
    GROUP_ID = eid;
  }
  WiFi.begin(esid.c_str(), epass.c_str());
}

String printLocalTime(){
  struct tm timeinfo;
  if(!getLocalTime(&timeinfo)){
    Serial.println("Failed to obtain time");
    return "";
  }
  char timeDay[30];
  strftime(timeDay,30, "%B %d %Y %H:%M:%S", &timeinfo);
  return timeDay;
}

void sendSheets(){
  struct tm timeinfo;
  if(!getLocalTime(&timeinfo)){
    Serial.println("Failed to obtain time");
    return;
  }
  char hour[6];
  strftime(hour,6, "%M", &timeinfo);
  if(String(hour) == "00" || String(hour) == "30"){
    HTTPClient http;
    String tempurl = "https://script.google.com/macros/s/AKfycbwzN9P7fZTUMRbY9JDqi8Hll7wXmkCfi5odI0ljctjXr8tyPhMNhyuhlOMJSscpd-tftQ/exec?sensor=";
    sensors.requestTemperatures();
    float temperatureC = sensors.getTempCByIndex(0);
    String url = tempurl + String(temperatureC);
    http.begin(url.c_str()); //Specify the URL and certificate
    http.setFollowRedirects(HTTPC_STRICT_FOLLOW_REDIRECTS);
    http.GET();
    http.end();
    delay(60000);
  }
}

void handleNewMessages(int numNewMessages) {
  String keyboardJson = "[[{ \"text\" : \"Refresh\", \"callback_data\" : \"0001\" }]]";
  for (int i = 0; i < numNewMessages; i++) {
    String chat_id = String(bot.messages[i].chat_id);
    String sgTime = printLocalTime();
    String text = bot.messages[i].text;
    int message_id = bot.messages[i].message_id;
    Serial.println(text);
    String from_name = bot.messages[i].from_name;
    if (bot.messages[i].type == "callback_query"){
      String button_data = bot.messages[i].text;
      if(button_data == "0001"){
        sensors.requestTemperatures();
        float temperatureC = sensors.getTempCByIndex(0);
        String message = "Hello!, " + from_name + " Temperature is: " + String(temperatureC) + "ºC .\n"+ "Updated: " + sgTime;
        bot.sendMessageWithInlineKeyboard(chat_id, message, "", keyboardJson, message_id);
      }
    }
    else if(text == "/start"){
        bot.sendMessage(chat_id,"Send me /temp to get the fridge temperature!");
    } else if (text == "/temp"){
      sensors.requestTemperatures();
      float temperatureC = sensors.getTempCByIndex(0);
      String message = "Hello!, " + from_name + " Temperature is: " + String(temperatureC) + "ºC .\n"+ "Updated: " + sgTime;
      bot.sendMessageWithInlineKeyboard(chat_id, message,"", keyboardJson); 
    }
    else if(text == "/sheets"){
      String message = "This is the link to the google sheets";
      String keybd = "[[{ \"text\" : \"Go to Google\", \"url\" : \"https://docs.google.com/spreadsheets/d/1wPJGWEIItwlbYcbH3K586pipDY0JFe1QBFw5chFwF-Q/edit#gid=572956026\" }]]";
      bot.sendMessageWithInlineKeyboard(chat_id, message , "",keybd);
    }
    else if(text == "/reset"){
      bot.sendMessage(chat_id,"Resetting...");
      for (int i = 0; i < 152; ++i) {
          EEPROM.write(i, 0);
      }
      EEPROM.commit();
      bot.sendMessage(chat_id,"Sucessfully cleared memory");
    }
    else {
        bot.sendMessage(chat_id,"Unknown input!");
    }
  }
}

void checkAlert(float temperatureC,int numNewMessages){
    long int t1 = millis();
    while(temperatureC > 8.0){
      long int t2 = millis();
      if(t2-t1 > 300000){
        String message = "Warning High temperature "  + String(temperatureC) + "ºC .\n";
        Serial.println("High");
        bot.sendMessage(GROUP_ID, message, "");
        t1 = millis();
      }      
      while (numNewMessages) {
        handleNewMessages(numNewMessages);
        numNewMessages = bot.getUpdates(bot.last_message_received + 1);
      }
      sendSheets();
      delay(30000);
      sensors.requestTemperatures();
      temperatureC = sensors.getTempCByIndex(0);
    }  
    while(temperatureC < 2.0){
      long int t2 = millis();
      if(t2-t1 > 300000){
        String message = "Warning Low temperature "  + String(temperatureC) + "ºC .\n";
        Serial.println("Low");
        bot.sendMessage(GROUP_ID, message, "");
        t1 = millis();
      } 
      while (numNewMessages) {
        handleNewMessages(numNewMessages);
        numNewMessages = bot.getUpdates(bot.last_message_received + 1);
      }
      sendSheets();
      delay(30000);
      sensors.requestTemperatures();
      temperatureC = sensors.getTempCByIndex(0);
    }
}

bool testWifi(void){
  int c = 0;
  //Serial.println("Waiting for Wifi to connect");
  while ( c < 20 ) {
    if (WiFi.status() == WL_CONNECTED){
      configTime(gmtOffset_sec, daylightOffset_sec, ntpServer);
      return true;
    }
    delay(500);
    Serial.print("*");
    c++;
  }
  Serial.println("");
  Serial.println("Connect timed out, opening AP");
  return false;
}
void launchWeb(){
  Serial.println("");
  if (WiFi.status() == WL_CONNECTED){
    Serial.println("WiFi connected");
  }
  Serial.print("Local IP: ");
  Serial.println(WiFi.localIP());
  Serial.print("SoftAP IP: ");
  Serial.println(WiFi.softAPIP());
  createWebServer();
  // Start the server
  server.begin();
  Serial.println("Server started");
}
void setupAP(void){
  WiFi.mode(WIFI_STA);
  WiFi.disconnect();
  delay(100);
  int n = WiFi.scanNetworks();
  Serial.println("scan done");
  if (n == 0){
    Serial.println("no networks found");
  }
  else{
    Serial.print(n);
    Serial.println(" networks found");
    for (int i = 0; i < n; ++i){
      // Print SSID and RSSI for each network found
      Serial.print(i + 1);
      Serial.print(": ");
      Serial.print(WiFi.SSID(i));
      Serial.print(" (");
      Serial.print(WiFi.RSSI(i));
      Serial.print(")");
      //Serial.println((WiFi.encryptionType(i) == ENC_TYPE_NONE) ? " " : "*");
      delay(10);
    }
  }
  Serial.println("");
  st = "<ol>";
  for (int i = 0; i < n; ++i){
    st += "<li>";
    st += WiFi.SSID(i);
    st += " (";
    st += WiFi.RSSI(i);
    st += ")";
    st += "</li>";
  }
  st += "</ol>";
  delay(100);
  WiFi.softAP("ESP32-FTemp", "");
  Serial.println("Initializing_softap_for_wifi credentials_modification");
  launchWeb();
  Serial.println("over");
}
void createWebServer()
{
  {
    server.on("/", []() {
      IPAddress ip = WiFi.softAPIP();
      String ipStr = String(ip[0]) + '.' + String(ip[1]) + '.' + String(ip[2]) + '.' + String(ip[3]);
      content = "<!DOCTYPE HTML>\r\n<html>Update your WiFi Credentials";
      content += "<form action=\"/scan\" method=\"POST\"><input type=\"submit\" value=\"scan\"></form>";
      content += ipStr;
      content += "<p>";
      content += st;
      content += "</p><form method='get' action='setting'><label>SSID: </label><input name='ssid' length=32><p><label>PASS: </label><input name='pass' length=64>";
      content += "</p><p><label>Key: </label><input name='key' length=46>";
      content += "</p><p><label>GroupID: </label><input name='id' length=10><input type='submit'></p></form>";
      content += "</html>";
      server.send(200, "text/html", content);
    });
    server.on("/scan", []() {
      //setupAP();
      IPAddress ip = WiFi.softAPIP();
      String ipStr = String(ip[0]) + '.' + String(ip[1]) + '.' + String(ip[2]) + '.' + String(ip[3]);
      content = "<!DOCTYPE HTML>\r\n<html>go back";
      server.send(200, "text/html", content);
    });
    server.on("/setting", []() {
      String qsid = server.arg("ssid");
      String qpass = server.arg("pass");
      String qkey = server.arg("key");
      String qid = server.arg("id");
      if (qsid.length() > 0 && qpass.length() > 0 && qkey.length() > 0 ** qid.end() > 0) {
        Serial.println("clearing eeprom");
        for (int i = 0; i < 152; ++i) {
          EEPROM.write(i, 0);
        }
        Serial.println("writing eeprom ssid:");
        for (int i = 0; i < qsid.length(); ++i)
        {
          EEPROM.write(i, qsid[i]);
        }
        Serial.println("writing eeprom pass:");
        for (int i = 0; i < qpass.length(); ++i)
        {
          EEPROM.write(32 + i, qpass[i]);
          Serial.print("Wrote: ");
          Serial.println(qpass[i]);
        }
        Serial.println("writing eeprom key:");
        for (int i = 96; i < 142; ++i){
          EEPROM.write(i, qkey[i-96]);
          Serial.println(qkey[i-96]);
        }
        Serial.println("writing eeprom groupid:");
        for (int i = 142; i < 152; ++i){
          Serial.println(qid[i-142]);
          EEPROM.write(i, qid[i-142]);
        } 
        EEPROM.commit();
        content = "{\"Success\":\"saved to eeprom... reset to boot into new wifi\"}";
        delay(1000);
        statusCode = 200;
        ESP.restart();
      } 
      else {
        content = "{\"Error\":\"404 not found\"}";
        statusCode = 404;
        Serial.println("Sending 404");
      }
      server.sendHeader("Access-Control-Allow-Origin", "*");
      server.send(statusCode, "application/json", content);
    });
  }
}

void loop() {
  if (!testWifi() || ekey == ""){
    setupAP(); 
    launchWeb();
  }
  while ((WiFi.status() != WL_CONNECTED || ekey == "")){
    Serial.print(".");
    delay(100);
    server.handleClient();
  }
  sendSheets();
  int numNewMessages = bot.getUpdates(bot.last_message_received + 1);
  while (numNewMessages) {
      handleNewMessages(numNewMessages);
      numNewMessages = bot.getUpdates(bot.last_message_received + 1);
  }
  sensors.requestTemperatures();
  float temperatureC = sensors.getTempCByIndex(0);
  checkAlert(temperatureC,numNewMessages);  
  delay(100);
}
