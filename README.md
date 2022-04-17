# Data-science-in-IOT-project

## video
Voor de eindoplevering heb ik een video gemaakt van de applicatie. Dit heb ik niet alleen gedaan omdat het moest voor de opdracht, maar het is ook meteen de beste manier om te laten zien dat mijn prototype/product werkt.

De video van het project is hier te vinden: <br/>
https://www.youtube.com/watch?v=kuEbJSHuz8I<br/>

## Aansluiting DHT22 op Raspberry pi
Hieronder heb ik neergezet hoe ik de DHT22 heb aangesloten aan de raspberry pi.
<img src="https://github.com/Kheitora/Data-science-in-IOT-project/blob/main/Raspberry-Pi-Humidity-Sensor-DHT22-Wiring-Schematic.webp"/>
<img src="https://github.com/Kheitora/Data-science-in-IOT-project/blob/main/eigen%20aansluiting%20raspbuerry%20pi.jpeg"/><br/>

## Raspberry pi omgeving klaarmaken voor DHT22
Om de DHT22 te kunnen gebruiken heb ik eerst een aantal commands moeten uitvoeren in de terminal van de raspberry pi. Hieronder zal je alle commands een voor een te zien krijgen:<br/>

- sudo apt-get update
- sudo apt-get upgrade

- sudo apt-get install python3-dev python3-pip
- sudo python3 -m pip install --upgrade pip setuptools wheel

- sudo pip3 install --install-option="--force-pi" Adafruit_DHT

Om de file aan te maken waarin je gaat werken gebruik je de volgende code, ook weer in de terminal.
nano ~/file_name.py

Voor een meer gedetailleerdere uitleg verwijs ik je naar de pagina die mij enorm heeft geholpen, waar ook alles wordt uitgelegd: https://pimylifeup.com/raspberry-pi-humidity-sensor-dht22/<br/>

## Data soort
De data die ik gebruik in mijn applicatie is: <br/>

Temperatuur - Continues data<br/>
Humdity - continues data (https://www.rasch.org/rmt/rmt144a.htm)<br/>

Een continue variabele is een variabele waarvan de waarde wordt verkregen door te meten, dwz een die een ontelbare reeks waarden kan aannemen .

Een variabele over een niet-leeg bereik van de reële getallen is bijvoorbeeld continu, als het een waarde in dat bereik kan aannemen. De reden is dat elk bereik van reële getallen van bijvoorbeeld a naar b ontelbaar zijn.

Rekenmethoden worden vaak gebruikt bij problemen waarbij de variabelen continu zijn, bijvoorbeeld bij continue optimalisatieproblemen .

In de statistische theorie kunnen de kansverdelingen van continue variabelen worden uitgedrukt in termen van kansdichtheidsfuncties .

In continue- tijddynamica wordt de variabele tijd behandeld als continu, en de vergelijking die de evolutie van een variabele in de tijd beschrijft, is een differentiaalvergelijking . De onmiddellijke veranderingssnelheid is een goed gedefinieerd concept. (https://en.wikipedia.org/wiki/Continuous_or_discrete_variable)<br/>
