import requests
from bs4 import BeautifulSoup

# Define the custom User-Agent string
custom_user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36'

# Create a dictionary for the headers
headers = {
    'User-Agent': custom_user_agent
}
def get_events_html_data(url):
    html = requests.get(url,headers=headers).text
    soup = BeautifulSoup(html, 'lxml')
    events = soup.find_all('div', class_='article-content')
    with open("ticketmaster_data.tsv", 'a', encoding='utf-8') as tsvfile:
        for event in events:
            event_name = event.h3.text
            try:
                event_date = event.find('p',class_='date').span.text
            except AttributeError:
                event_date = ""
            try:
                event_venue = event.find('p',class_='venue').text
            except AttributeError:
                event_venue = ""
            try:
                event_ticket = event.find('p', class_='cta').a.get('href')
            except AttributeError:
                event_ticket = ""

            tsvfile.write(event_name + "\t" + event_date + "\t" + event_venue + "\t" + event_ticket)
            tsvfile.write("\n")

def get_ticketmaster_data():
    get_events_html_data('https://guides.ticketmaster.co.uk/sports-guide/')

