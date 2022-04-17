#importeer alle belangrijke onderdelen
import json
import time
import os
import psutil
import requests
import adafruit_dht
import board

#link de uitkomsten van de DHT22 met de temperature en de humidity variabele.
dht_device = adafruit_dht.DHT22(board.D4)
temperature = dht_device.temperature
humidity = dht_device.humidity

#zet de data die je nodig hebt om een connectie te maken met thingspeak hieronder
channel_id = "1706005" #zet hier het ID van je eigen channel
write_key = "H6F5AMOVJG6AOTOX" #Zet hier de write key van je channel 
url = "https://api.thingspeak.com/update" #Deze link kan je laten staan.
messageBuffer = []

while True:
    #Zet alle connectie gegevens hierin, je wilt humidity en temperature doorsturen naar thingspeak en de api_key is er om een connectie te maken.
    queries = {"api_key": write_key, "field1": humidity, "field2": temperature}

    #Hier maak je een connectie met thingspeak en stuur je alles door
    r = requests.get(url, params = queries)
    #Wanneer het is gelukt zal er in de console komen "Data received"
    if r.status_code == requests.codes.ok:
        print("data received")
    #Wanneer het niet is gelukt zal er een error code in de console komen om je te helpen bij het identificeren van het probleem
    else:
        print("Error Code: " + str(r.status_code))
    #Na alles zal hij een tijdje wachten voordat hij weer data opstuurd naar thingspeak.
    time.sleep(15)
