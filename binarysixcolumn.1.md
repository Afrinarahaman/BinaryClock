---
title: Binary Clock
section: 1
header: User Manual
footer: binary clock 1.1.0
date: December 02,2022
---

# NAME

Binary clock--> Det er et Binære Ur, som viser tid  med to forskellige tidsformater (12 eller 24) på Rasberry Pi Sense Hat. Her LED'erne har blevet brugt til at vise uret, som timer, minutter og sekunder.

# SYNOPSIS
For at Køre programmet:
**binarysixcolumn** [*OPTIONS*]

Programmet kan køre med service. Kommandoer til at starte og stoppe service.

**Start service** ->  sudo systemctl start binaryclock.service

**Stop service** -> sudo systemctl stop binaryclock.service

Hvis der er nogle fejl, så kan du tjekke status for at kigge hvor er der fejl. Kommando til at tjekke service
**Check status** ->  sudo systemctl status binaryclock.service

# CONFIGURATION
For at ændre rettigheder  af service 
sudo chmod 644 /lib/systemd/system/binaryclock.service

For at sætte 'execute' mod i programmet
chmod +x /home/pi/binarysixcolumn.py

For at enable service
sudo systemctl daemon-reload
sudo systemctl enable binaryclock.service

# DESCRIPTION

**BinaryClock** --> Programmet viser aktuelt tid som binært ur. Det viser forskellige LED farver for timer, minutter og sekumder.
                    fx Grøn farve for Timer, Blå farve til Minutter og Rød farve til Sekunder.
                    Der er en anden lys har blevet vælgt for at vise hvilket format tidvisning er det nu i venstre hjørnet . 
                    Når det er lyseblå, det betyder uret er nu i 12timer format og hvis lyset er gul, så kører programmet i 24timer format.
                    Der er fire funktioner kan der udløses af joystick. 
                    Uret vises 12timer og 24timer formatter i 6 coloner i lodret, 12timer og 24timer formatter i 3 række i vandret. 

**JoyStick**  --> Man kan skifte forskellige tidvisning formater med joystick af Rasberry Pi.

**Joystick Op** --> Hvis joystick bliver trykket i oppe, vises det i 12timer format med 6 coloner.
**JoyStick Down** --> Hvis man trykker i ned, ændrer det fra 12timer format til 24timer format med 6 coloner.
**Joystick Left** -->  Hvis joystick bliver trykket i venstre, vises det i 12timer format med 3 rækker.
**Joystick Right** -->  Hvis man trykker i højre, ændre det fra 12timer format til 24timer format med 3 rækker.

# OPTIONS
**clock-time**
: 12h eller 24h 
**dir**
:h eller v

# EXAMPLES

**binaryclock dir=h**
