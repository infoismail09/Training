import requests

def FetchAndSaveToFile(url, path):
    r = requests.get(url)
    # with open(path, "w") as f:
    #     f.write(r.text)
    with open(path, "w", encoding="utf-8") as f:
        f.write(r.text)  # with help this encoding we scrap data befor above line facing error

url = "https://timesofindia.indiatimes.com/city/delhi"

FetchAndSaveToFile(url,"data/times.html")
