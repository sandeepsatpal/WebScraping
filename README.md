# WebScraping
This repository contains different web scrapping logic for varieties of web pages like
1. Static html content
2. Dynamic html pages which loads the content via javascripts/API calls
3. Web pages with captcha
4. Web pages with credentials

# WebScraping methods 

1. <b> Static content </b><br/>

<p>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;		Web pages with static contents are easiet to scrape. <br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;   	Below python module extract static content and save them in csv/tsv file using beautiful soup. <br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;   	<u><i> ticketmaster.py -> get_events_html_data </i></u> <br />
</p>

2. <b>Dynamic content</b><br/>
<p>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;	Html pages can download the data dynamically using javascript/API calls. There are different methods to scrape such pages. </p></br>
</p>
<p>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<b>Method 1: Scrape through API calls </b> </br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Find the API calls from html page/javascript and use them directly in Python.</br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Below python module uses API to scrape Json and store them in csv/tsv file. </br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<i> livescore.py -> get_events_josn_data </i><br /> 
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<i>enentime.py -> get_eventime_json_data  </i> <br />
</p>

<p>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<b>Method 2: Using browser extension (Selenium and chrome driver) </b> </br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; If finding API in the html page is difficult as they are hidden sometimes, we can also extract dynamic web content using browser extension like chromedriver. </br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Below python module uses selenium and chromedriver to scrape and store them in csv/tsv. But this method is generally slow and useful for smaller set of urls. </br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Till entire dynamic content is loaded, extraction needs to wait. </br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<i> livescore.py -> get_events_html_data</i> <br />

<p>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<b>Method 3: Using browser extension (Playwright and chromium) </b> </br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Although Selenium remains the go-to for legacy browser support, cross-browser testing, and enterprise environments due to its mature ecosystem and wider language support </br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Playwright is ideal for modern web applications, offering faster execution, better handling of dynamic content, and built-in features like auto-waiting and network interception </br> 
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Below python module uses playwright and chromium in async mode to scrape and store them in csv/tsv. </br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Till entire dynamic content is loaded, extraction needs to wait. </br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<i> livescore.py -> get_events_html_data_playwright </i> <br />

3. <b> Rotating proxy for anti-bot scraping </b>
<p>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;	Server may block IP address if scraping is done through code. So it is important to rotate proxies. </p> <br> 
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; There are different methods to handle rotating proxies
</p>
<p>
   &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<b>Method 1: Free Proxy </b> </br>
   &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Python provides free-proxy package. </br>
   &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Below python module uses Freeproxy: https://pypi.org/project/free-proxy/ (python free-proxy) module to generate proxies and use them to scrape web pages. </br>
   &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; It is possible that http or https proxies are not available when you run the code. Either you need to run at different time or buy the proxies.</br>
   &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <i> eventime.py -> get_eventime_topUrls_rotating_proxies </i> </br>
</p>
<p>
      &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<b>Method 2: Buy proxies using zenrows </b> </br>
      &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Other efficient way is to buy the proxies (like zenrows) and use them to scrape web pages. </br>
      &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Once purchase, you get API key which you need to pass. </br>
      &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Below python module demostrate this logic. </br>
      &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <i> livescore.py -> get_events_html_data_zenrows_proxy </i> <br />
</p>


   
    

