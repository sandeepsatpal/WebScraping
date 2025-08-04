import asyncio
from playwright.async_api import async_playwright
import datetime
import json
from datetime import datetime
from datetime import timedelta
from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time


# Define the custom User-Agent string
custom_user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36'

# Create a dictionary for the headers
headers = {
    'User-Agent': custom_user_agent
}

'''
# Set path to your chromedriver
service = Service('D:\Personal\PythonLearning\chromedriver-win64\chromedriver-win64\chromedriver.exe')
options = webdriver.ChromeOptions()
options.add_argument('--headless')
driver = webdriver.Chrome(service=service)
'''

def get_events_josn_data(game,url):
    json_data_url = requests.get(url).text
    json_data = json.loads(json_data_url)
    with open("livescore_data.csv", 'a',encoding='utf-8') as csvfile:
        for events in json_data["Stages"]:
            snm = events["Snm"]
            cnm = events["Cnm"]
            for event in events["Events"]:
                time = str(event["Esd"])
                team1 = event["T1"][0]["Nm"]
                team2 = event["T2"][0]["Nm"]
                csvfile.write(game + "," + snm + "," + cnm + "," + time + "," + team1 + "," + team2)
                csvfile.write("\n")

async def get_events_html_data_playwright(url):
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()

        # Load the page and wait for full network activity to settle
        await page.goto(url, wait_until="networkidle")

        # Optional: run custom JavaScript if needed
        await page.evaluate("""() => {
            // Example: scroll to bottom to trigger lazy loading
            window.scrollTo(0, document.body.scrollHeight);
        }""")

        with open("temp.html", "w", encoding='utf-8') as htmlfile:
            events = await page.query_selector_all('div[class="zp Ep"]')

            for event in events:
                teams = await event.query_selector_all('div[class="Kp"]')
                team1 = await teams[0].text_content()
                team2 = await teams[1].text_content()
                print(team1,team2)
            #htmlfile.write(html)
        # Get the full HTML content

        await browser.close()

'''
def get_events_html_data(url):
    driver.get(url)
    # Let JavaScript load (you can tweak the sleep time or use WebDriverWait)
    time.sleep(5)

    # Extract page source
    html = driver.page_source
    soup = BeautifulSoup(html, 'lxml')
    events = soup.find_all('div', class_='zp Ep')
    with open("example.html","w",encoding='utf-8') as htmlfile:
        for event in events:
            teams = event.find_all('div', class_='Kp')
            team1 = teams[0].text
            team2 = teams[1].text
            print(team1,team2)

'''

def get_events_html_data_zenrows_proxy(url):
    apikey = '####'
    params = {
        'url': url,
        'apikey': apikey,
    }
    with open("eventimezenrow.html", "w", encoding='utf-8') as htmlfile:
        response = requests.get('https://api.zenrows.com/v1/', params=params)
        htmlfile.write(response.text)

def get_livescore_data():
    #get_events_html_data("https://www.livescore.com/en/basketball/")
    #get_events_html_data_zenrows_proxy("https://www.eventim.co.uk/categories/")
    asyncio.run(get_events_html_data_playwright("https://www.livescore.com/en/basketball/"))
    '''
    allevents = {"soccer","hockey","basketball","tennis","cricket"}
    start_date = datetime.now()
    end_date = datetime.now() + timedelta(days=10)


    for event in allevents:
        for single_date in range((end_date - start_date).days + 1):
            current_date = (start_date + timedelta(days=single_date)).strftime("%Y%m%d")
            url = 'https://prod-cdn-mev-api.livescore.com/v1/api/app/date/' + event + '/' + current_date + '/5.30?locale=en'
            get_events_josn_data(event,url)
    '''
