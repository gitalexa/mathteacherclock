# mathteacherclock


Hier geht es um ein python-script, das ein Uhr anzeigen soll. Dabei werden die Stunden und MInuten jeweils als Matheaufgabe angezeigt.


Grundlage ist das Git-Projekt: https://github.com/rm-hull/max7219 mit dem die Ansteuerung der LED-Matrixen durchgeführt wird.


Installation:

git clone https://github.com/rm-hull/max7219.git && cd max7219

sudo python setup.py install

die silly_clock.py aus dem Projekt ist die Basis für dieses Projekt.



https://tutorials-raspberrypi.de/led-dot-matrix-zusammenbau-und-installation/


Benötigt werden

LCD-Matrix und ein Raspberry Pi


Als Betriebssystem habe ich das hier genommen:

https://downloads.raspberrypi.org/raspbian/images/raspbian-2018-11-15/


dann über raspi-config SPI einschalten



