import requests
import os
import json
import http.client
import re
from urllib.request import urlopen

while True:
    data = input("Input detect info: ")
    spesifik = r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'
    search_key = re.findall(spesifik, data)
    if search_key:
        ip = search_key[0]
    else:
        print("Tidak ada alamat IP yang ditemukan.")

    url = f"https://geo.leadboxer.com/GeoIpEngine/{ip}?jsonp&callback=jQuery112406168206409877375_1684598717950&_=1684598717951"
    response = urlopen(url)
    if response.getcode() == 200:
        response_body = response.read().decode('utf-8')
        loc = json.loads(response_body.replace("jQuery112406168206409877375_1684598717950(", "").replace(")", ""))
    else:
        print("Connections is low, try again !")

    print(f"""
:::::::::::::::::::::::::::::::::::::::::
IP          : {ip}
Benua       : {loc["subContinent"]}
Negara      : {loc["countryName"]}
Provinsi    : {loc["regionName"]}
Kota        : {loc["city"]}
ISP         : {loc["isp"]}
Latitude    : {loc["latitude"]}
Longitude   : {loc["longitude"]}

pullspeed : {loc["response time [ms]"]} ms
:::::::::::::::::::::::::::::::::::::::::
""")
    input("LANJUT... ")
    os.system("cls")
