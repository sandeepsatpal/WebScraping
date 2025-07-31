# WebScraping
This repository contains different web scrapping logic
1. Static html content
2. Dynamic html pages which loads the content via javascripts/API calls
3. Web pages with captcha
4. Web pages with credentials

# WebScraping methods 

1. ticketmaster.py -> get_events_html_data: <br />
   This methond extracts the static html content using beautiful soup

2. livescore.py -> get_events_josn_data and enentime.py -> get_eventime_json_data: <br />
   This methods demostract how to extract data from dynamic pages which internally uses API calls with different parameters

3. livescore.py -> get_events_html_data: <br />
   If finding API in the html page is difficult as they are hidden sometimes, we can also extract dynamic web content using browser extension like chromedriver. In this method, dynamic data is extracted using chromedriver. But this method is generally slow and useful for smaller set of urls. Till entire dynamic content is loaded, extracting needs to wait.

4. eventime.py -> get_eventime_topUrls_rotating_proxies: <br />
   This method uses Freeproxy: https://pypi.org/project/free-proxy/ (python free-proxy) module to get the free proxy in the python code. It is possible that http or https proxies are not available when you run the code. Either you need to run at different time or buy the proxies.

5. livescore.py -> get_events_html_data_zenrows_proxy: <br />
   This method uses zenrows proxy. This is not free. Once purchase, you need to provide API Key to get the support of proxies.
    

