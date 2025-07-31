import itertools
from fileinput import close
import json
import requests
from bs4 import BeautifulSoup
from fp.fp import FreeProxy

allproxies = []

for i in range(1,3):
    proxy = FreeProxy(rand=True,https=True).get() # proxy = FreeProxy(rand=True).get()
    proxies = {
        "http": f"{proxy}".replace("https","http"),
        "https": f"{proxy}".replace("https","http").replace("http","https")
    }
    allproxies.append(proxies)

print(allproxies)

def proxy_rotator(allproxies):
    return itertools.cycle(allproxies)

# create a generator from the proxy rotator function
proxy_gen = proxy_rotator(allproxies)

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)',
    'Accept-Language': 'en-US,en;q=0.9',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'
}

def get_eventime_json_data(event,url):
    json_data_url = requests.get(url).text
    json_data = json.loads(json_data_url)
    #print(json_data)
    with open("eventim_data.tsv", 'a', encoding='utf-8') as tsvfile:
        for events in json_data["productGroups"]:
            name = events["name"]
            for product in events["products"]:
                eventname = product["name"]
                link = product["link"]
                city = product["typeAttributes"]["liveEntertainment"]["location"]["city"]
                address = product["typeAttributes"]["liveEntertainment"]["location"]["name"]
                tsvfile.write(name+"\t"+eventname+"\t"+link+"\t"+city+"\t"+address+"\n")

def get_eventime_json_data_rotating_proxies(event,url):

    json_data_url = requests.get(url,proxies=next(proxy_gen)).text
    json_data = json.loads(json_data_url)
    print(json_data)
    with open("eventime_data_proxy.tsv", 'a', encoding='utf-8') as tsvfile:
        for events in json_data["productGroups"]:
            name = events["name"]
            for product in events["products"]:
                eventname = product["name"]
                link = product["link"]
                city = product["typeAttributes"]["liveEntertainment"]["location"]["city"]
                address = product["typeAttributes"]["liveEntertainment"]["location"]["name"]
                tsvfile.write(name+"\t"+eventname+"\t"+link+"\t"+city+"\t"+address+"\n")

def get_eventime_topUrls_rotating_proxies(url):
    list_topUrls = []
    html = requests.get(url,headers=headers,proxies=next(proxy_gen)).text
    soup = BeautifulSoup(html, 'lxml')
    listings = soup.find_all('ul', class_='text-listing')
    for listing in listings:
        topurl = listing.find('li').a.attrs['href']
        list_topUrls.append(topurl)
    return list_topUrls

def get_eventime_topUrls(url):
    list_topUrls = []
    html = requests.get(url,headers=headers).text
    soup = BeautifulSoup(html, 'lxml')
    listings = soup.find_all('ul', class_='text-listing')
    for listing in listings:
        topurl = listing.find('li').a.attrs['href']
        list_topUrls.append(topurl)
    return list_topUrls

def get_eventime_data():
    # get top level urls
    list_topUrls = get_eventime_topUrls('https://www.eventim.co.uk/categories/')
    for url in list_topUrls:
        print("top url:" + url)

    list_topUrls = get_eventime_topUrls_rotating_proxies('https://www.eventim.co.uk/categories/')
    for url in list_topUrls:
        print("top url:" + url)


    allevents = {"Music", "Sport", "Attractions", "Theatre %26 Arts", "Social Events", "Exhibitions %26 Immersive"}


    for event in allevents:
        for page in range(1,2):
            url = "https://public-api.eventim.com/websearch/search/api/exploration/v2/productGroups?webId=web__eventim-co-uk&language=en&page="+str(page)+"&retail_partner=EUK&categories="+event+"&categories=null&sort=Recommendation&in_stock=true"
            #print(url)
            #get_eventime_json_data(event,url)
            #get_eventime_json_data_rotating_proxies(event,url)

