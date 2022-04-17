import json
import time
import os
import psutil
import requests
import adafruit_dht
import board

dht_device = adafruit_dht.DHT22(board.D4)
temperature = dht_device.temperature
humidity = dht_device.humidity

channel_id = "1706005"
write_key = "H6F5AMOVJG6AOTOX"
url = "https://api.thingspeak.com/update"
messageBuffer = []

while True:
    queries = {"api_key": write_key, "field1": humidity, "field2": temperature}

    r = requests.get(url, params = queries)
    if r.status_code == requests.codes.ok:
        print("data received")
    else:
        print("Error Code: " + str(r.status_code))
        time.sleep(15)