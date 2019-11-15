#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

os.system("apt-get install python-pip")
os.system("apt-get install figlet")
os.system("clear")
os.system("figlet ANONIM")
print("""
Bu araç "torghost" aracının indirme, kurma ve çalıştırma işlemlerini otomatik yapar. 

1) Başlat
2) Durdur

""")

secim = raw_input("Seçim : ")

if(secim=="1"):
	os.system("git clone https://github.com/SusmithKrishnan/torghost.git")
	os.system("cd torghost/ && bash install.sh")
	os.system("torghost start")

if(secim=="2"):
	os.system("torghost stop")
