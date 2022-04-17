# Data-science-in-IOT-project

## concept omschrijving
Ik heb een product gemaakt dat de luchtvochtigheid en de temperatuur in een ruimte meet en dit opstuurd naar thingspeak. Dit heb ik gemaakt met mijn TLE project (project voor school) in gedachten. We zijn met TLE van plan om een sensoren bundeltje te maken die data over een plant en zijn omgeving naar een applicatie stuurt, die dan vervolgens een melding geeft aan de gebruiker of zijn/haar plant water nodig heeft of in het geval van het product dat ik heb gemaakt, of de plant kan groeien in de omgeving waar hij op dat moment staat. 

Ik heb in dit product niet gebruik gemaakt van een grondvochtsensor, omdat ik niet genoeg tijd had om dit ook nog werkend te krijgen voor de deadline. Dit zal uiteindelijk wel de bedoeling zijn voor TLE.

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

## inspiratie
Ik heb inspiratie en stukjes code kunnen halen uit twee verschillende bronnen:<br/>

- De docent zijn gegeven code voor de connectie met thingspeak: <br/>
https://github.com/robvdw/CMIDAT01K-DATA-SCIENCE-for-IOT/blob/master/Code/ThingSpeak_Python_v3_Example.py<br/>
- Een tutorial voor werken met een DHT22 sensor (raspberry pi):<br/>
https://pimylifeup.com/raspberry-pi-humidity-sensor-dht22/<br/>


## Data soort
De data die ik gebruik in mijn applicatie is: <br/>

Temperatuur - Continues data<br/>
Humdity - continues data (https://www.rasch.org/rmt/rmt144a.htm)<br/>

Een continue variabele is een variabele waarvan de waarde wordt verkregen door te meten, dwz een die een ontelbare reeks waarden kan aannemen .

Een variabele over een niet-leeg bereik van de reële getallen is bijvoorbeeld continu, als het een waarde in dat bereik kan aannemen. De reden is dat elk bereik van reële getallen van bijvoorbeeld a naar b ontelbaar zijn.

Rekenmethoden worden vaak gebruikt bij problemen waarbij de variabelen continu zijn, bijvoorbeeld bij continue optimalisatieproblemen .

In de statistische theorie kunnen de kansverdelingen van continue variabelen worden uitgedrukt in termen van kansdichtheidsfuncties .

In continue- tijddynamica wordt de variabele tijd behandeld als continu, en de vergelijking die de evolutie van een variabele in de tijd beschrijft, is een differentiaalvergelijking . De onmiddellijke veranderingssnelheid is een goed gedefinieerd concept. (https://en.wikipedia.org/wiki/Continuous_or_discrete_variable)<br/>

## iteraties
Ik ben natuurlijk niet gelijk op dit product gekomen, hiervoor heb ik veel verschillende dingen moeten uitvogelen. 

### iteratie 1
Ik had een product gemaakt dat, met de DHT22 en een bodemvochtsensor, luchtvochtigheid, bodemvochtigheid en temperatuur opmeet. Dit had ik gedaan met een Arduino uno en javascript. Er zit geen wifi module ingebouwd in de Arduino uno, wat later een probleem werd. Ik had geprobeerd een wifi module werkend te krijgen aan de arduino uno, echter is mij dit niet gelukt. Ik had een nieuw board gebruikt om de ESP8266 (wifi module) aan te kunnen sturen, maar om een of andere reden kon hij de seriële port van de arduino uno niet meer zien. Dit heb ik toen een hele week geprobeerd om op te lossen zonder succes.

### iteratie 2
Omdat de arduino uno niet mee wou werken heb ik ervoor besloten (een week voor de oplevering) om toch maar met de raspberry pi en met python(3) te gaan werken. Dit verliep iets soepeler, al was ik in het begin wel vergeten hoe ik de raspberry pi moest gebruiken. Dit was echter al snel opgelost door het kijken van een tutorial.

In iteratie 2 heb ik een "product" gemaakt dat mij direct heeft geholpen met mijn laatste iteratie (iteratie 3). Ik had namelijk code geschreven waardoor de DHT22 luchtvochtigheid en temperatuur kon meten met de raspberry pi. Ik was toen bezig om dit op te sturen naar thingspeak, echter had ik hier wederom een probleem met het opsturen van de data. Omdat ik python 3 had gebruikt met een tutorial die gemaakt was met een oudere versie, was mijn code foutief, en kon ik dus geen connectie maken met thingspeak. Uiteindelijk ben ik online gaan kijken voor andere tutorials die ik wel kon gebruiken met python 3, wat resulteerde in de laatste iteratie van het product. (Ik had ervoor gekozen om de bodemvochtsensor niet te gebruiken met de raspberry pi, omdat ik daar te weinig tijd voor had, sinds ik een week van tevoren had bedacht om van microcontroller naar microcomputer te switchen).

### iteratie 3
In deze iteratie heb ik het product werkend gekregen. Ik had een voorbeeld code gevonden van de docent over hoe je een connectie met thingspeak moest maken dat gemaakt was voor python3. In deze code stond echter niet hoe ik de data van de sensoren moest doorsturen naar thingspeak. Om dit voor elkaar te krijgen heb ik onderdelen van de vorige iteratie gepakt en aangepast zodat het bij de code van de docent zou passen. Het prodcut werkt nu, het stuurt sensor data naar thingspeak door middel van de raspberry pi.

## verder werken
Ik ga aan dit project verder werken, omdat ik zoals ik eerder al had gezegd dit nodig heb voor TLE. Op dit moment heb ik het werkend gekregen om een DHT22 aan te sluiten aan een raspberrypi en de data door te sturen naar thingspeak. In de toekomst zal het product er echter heel anders uitzien.

Voor TLE moet ik ook nog een bodemvochtsensor toevoegen en misschien ook nog een lichtsensor, waardoor het al een stukje uitgebreider wordt dan wat ik nu heb gemaakt. Ook zal ik in de toekomst een connectie moeten maken met een eigen gemaakt applicatie in plaats van thingspeak, wat ook nog wel een uitdaging kan worden.

## conclusie
Ik heb dit project afgerond met een werkend prototype, echter zal dit product nog verder ontwikkeld worden door mijn team en ik tijdens TLE. Het is een IOT project, dus het voldoet aan de eisen van dit keuzevak. Ik vondt het een interessant keuze vak waar ik veel van geleerd heb. Ik wist aan het begin niet eens hoe ik een ledje moest aansluiten aan de Raspberry pi, dus dat ik nu sensor data kan versturen via wifi naar thingspeak vindt ik enorm gaaf. 
