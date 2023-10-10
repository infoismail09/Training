import requests

proxies = {
  "http": "http://10.10.1.10:3128",
  "https": "https://10.10.1.10:1080", # yaha humhe apni im use kar sakte hai proxy isse humari ip addresss change hote rahega
}

r = requests.get("https://api64.ipify.org?format=json",proxies=proxies)
print(r.json())