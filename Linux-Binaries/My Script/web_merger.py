#! /usr/bin/python3

# A simple script to URL encode your web payloads.

import requests
from bs4 import BeautifulSoup

merge = input("[*] Payload to encode: ")

url = "https://www.urlencoder.org/"

response = requests.get(url)

if response.status_code == 200:
    print("[+] Site Accessible!")
else:
    print("[-] Site Inaccessible!")
    exit(1)

data = {'input':merge,'charset':'UTF-8','separator':'lf'}

response = requests.post(url,data=data)

soup = BeautifulSoup(response.text, 'html.parser')

textarea = soup.find_all('textarea')

inpt = str(textarea[0].text)
outpt = str(textarea[1].text)

print("\n[*] Plain Input: "+inpt+"\n"+"[*] Encoded Output: "+outpt)
