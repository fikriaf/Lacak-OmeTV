import socket
import subprocess
import requests
import json
import threading


myip = socket.gethostbyname(socket.gethostname())
temp = []
def read_output():
    run = r"""C:\Program Files\Wireshark\tshark.exe -i "Wi-Fi 2" """

    proses = subprocess.Popen(run, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, encoding="UTF-8")


    for line in iter(proses.stdout.readline, b""):
        if "ICMP" in line:
            process_output(line)
        else:
            continue


def process_output(line):
    baris = str(line).split(" ")

    if ":" in baris:
        return
    elif "→" in baris:
        getip = baris[baris.index("→") - 1]
        myip2 = baris[baris.index("→") + 1]
        gettype = baris[baris.index("→") + 2]

        if getip in temp:
            return
        elif myip2 in getip or myip in getip or ":" in getip:
            return

        print(f"IP - {getip} ----- protocol {gettype}")
    else:
        print("STARTED CAPTURING.....")

try:
    output_thread = threading.Thread(target=read_output)
    output_thread.start()
    output_thread.join()
except KeyboardInterrupt:
    print("Script stopped by user")
