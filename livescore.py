import datetime
import json
from datetime import datetime
from datetime import timedelta
from bs4 import BeautifulSoup
import requests


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

def get_events_html_data(url):
    pass

def get_livescore_data():
    allevents = {"soccer","hockey","basketball","tennis","cricket"}
    start_date = datetime.now()
    end_date = datetime.now() + timedelta(days=10)


    for event in allevents:
        for single_date in range((end_date - start_date).days + 1):
            current_date = (start_date + timedelta(days=single_date)).strftime("%Y%m%d")
            url = 'https://prod-cdn-mev-api.livescore.com/v1/api/app/date/' + event + '/' + current_date + '/5.30?locale=en'
            get_events_josn_data(event,url)

