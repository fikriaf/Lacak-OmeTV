import socket
import subprocess
import requests
import json
from bs4 import BeautifulSoup as BS
import threading
import http.client

def getiplock(ip):
    #loc = json.loads(requests.get(f"https://geo.leadboxer.com/GeoIpEngine/{ip}?jsonp&callback=jQuery112406168206409877375_1684598717950&_=1684598717951").text.replace("jQuery112406168206409877375_1684598717950(", "").replace(")", ""))
    conn = http.client.HTTPSConnection("geo.leadboxer.com")
    conn.request("GET", f"/GeoIpEngine/{ip}?jsonp&callback=jQuery112406168206409877375_1684598717950&_=1684598717951")
    response = conn.getresponse()
    data = response.read()
    conn.close()

    loc = json.loads(data.decode("utf-8").replace("jQuery112406168206409877375_1684598717950(", "").replace(")", ""))

    try:
        negara = loc["countryName"]
    except:
        negara = "Tidak Terdeteksi"
    try:
        provinsi = loc["regionName"]
    except:
        provinsi = "Tidak Terdeteksi"
    try:
        kota = loc["city"]
    except:
        kota = "Tidak Terdeteksi"
    try:
        prov = loc["org"]
    except:
        prov = "Tidak Terdeteksi"

    return negara, provinsi, kota, prov

myip = socket.gethostbyname(socket.gethostname())
temp = []
def read_output():
    run = r"""C:\Program Files\Wireshark\tshark.exe -i "Wi-Fi 2" """

    proses = subprocess.Popen(run, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, encoding="UTF-8")


    for line in iter(proses.stdout.readline, b""):
        if "STUN" in line:
            continue
        else:
            process_output(line)


def process_output(line):
    baris = str(line).split(" ")

    if "172.67.69.226" in baris or "104.20.7.44" in baris or "31.24.224.27" in baris or ":" in baris:
        return
    elif "→" in baris:
        getip = baris[baris.index("→") - 1]
        myip2 = baris[baris.index("→") + 1]
        gettype = baris[baris.index("→") + 2]

        if getip in temp:
            return
        elif myip2 in getip or myip in getip or ":" in getip:
            return

        negara, provinsi, kota, _ = getiplock(getip)
        if "United States" == negara or "Germany" == negara or "France" in negara:
            return
        else:
            temp.clear()
            print(f"IP:{getip} {gettype} | Negara:{negara} | Provinsi:{provinsi} | Kota:{kota} | Network:{_}")
            temp.append(getip)
    else:
        print("STARTED CAPTURING.....")

try:
    output_thread = threading.Thread(target=read_output)
    output_thread.start()
    output_thread.join()
except KeyboardInterrupt:
    print("Script stopped by user")
