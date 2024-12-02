import requests,json
from bs4 import BeautifulSoup as BS

head={
"Host": "geo.leadboxer.com",
"User-agent": "Mozilla/5.0 (Linux; Android 11; Infinix X662) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.85 Mobile Safari/537.36"
}
loc=json.loads(requests.get("https://geo.leadboxer.com/GeoIpEngine/110.136.218.146?jsonp&callback=jQuery112406168206409877375_1684598717950&_=1684598717951").text.replace("jQuery112406168206409877375_1684598717950(", "").replace(")", ""))
print(json.loads(loc.replace("jQuery112406168206409877375_1684598717950(", "").replace(")", "")))


#print(requests.get("https://demo.ip-api.com/json/114.5.102.49?field=6§439&lang=en", headers=head).text)