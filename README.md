# WebScraping
This repository contains different web scrapping logic for varieties of web pages like
1. Static html content
2. Dynamic html pages which loads the content via javascripts/API calls
3. Web pages with captcha
4. Web pages with credentials

# WebScraping methods 

1. <b> Static content </b><br/>
<table border=0>
   <tr>
      <td>
		Web pages with static contents are easiet to scrape. </br>
      Below python module extract static content and save them in csv/tsv file using beautiful soup. </br>
      </td>
   </tr>
   <tr>
      <td>
   	<u><i> ticketmaster.py -> get_events_html_data </i></u> 
      </td>
   </tr>
</table>


2. <b>Dynamic content</b><br/>
<table border=0>
   <tr>
      <td>
         Html pages can download the data dynamically using javascript/API calls. There are different methods to scrape such pages.
      </td>
   </tr>
</table>

<table border=0>
   <tr>
      <td>
         <b>Method 1: Scrape through API calls </b> </br>
      </td>
   </tr>
   <tr>
      <td>
         Find the API calls from html page/javascript and use them directly in Python.</br>
         Below python module uses API to scrape Json and store them in csv/tsv file. </br>
      </td>
   </tr>
   <tr>
      <td>
         <i> livescore.py -> get_events_josn_data </i><br /> 
         <i>enentime.py -> get_eventime_json_data  </i> <br />
      </td>
   </tr>
</table>

<table border=0>
   <tr>
      <td>
         <b>Method 2: Using browser extension (Selenium and chrome driver) </b> </br>
         </td>
   </tr>
   <tr>
      <td>
          If finding API in the html page is difficult as they are hidden sometimes, we can also extract dynamic web content using browser extension like chromedriver. </br>
          Below python module uses selenium and chromedriver to scrape and store them in csv/tsv. But this method is generally slow and useful for smaller set of urls. </br>
         Till entire dynamic content is loaded, extraction needs to wait. </br>
         </td>
   </tr>
   <tr>
      <td>
         <i> livescore.py -> get_events_html_data</i> <br />
       </td>
   </tr>
</table>        

<table border=0>
   <tr>
      <td>
         <b>Method 3: Using browser extension (Playwright and chromium) </b> </br>
         </td>
   </tr>
   <tr>
      <td>
         Although Selenium remains the go-to for legacy browser support, cross-browser testing, and enterprise environments due to its mature ecosystem and wider language support </br>
         Playwright is ideal for modern web applications, offering faster execution, better handling of dynamic content, and built-in features like auto-waiting and network interception </br> 
         Below python module uses playwright and chromium in async mode to scrape and store them in csv/tsv. </br>
         Till entire dynamic content is loaded, extraction needs to wait. </br>
      </td>
   </tr>
   <tr>
      <td>
         <i> livescore.py -> get_events_html_data_playwright </i> <br />
        </td>
   </tr>
</table>           

3. <b> Rotating proxy for anti-bot scraping </b>

<table border=0>
   <tr>
      <td>
         Server may block IP address if scraping is done through code. So it is important to rotate proxies. <br> 
         There are different methods to handle rotating proxies
      </td>
   </tr>
</table>
<table border=0>
   <tr>
      <td>
         <b>Method 1: Free Proxy </b> </br>
      </td>
   </tr>
   <tr>
      <td>
         Python provides free-proxy package. </br>
         Below python module uses Freeproxy: https://pypi.org/project/free-proxy/ (python free-proxy) module to generate proxies and use them to scrape web pages. </br>
         It is possible that http or https proxies are not available when you run the code. Either you need to run at different time or buy the proxies.</br>
         </td>
   </tr>
   <tr>
        <td>
           <i> eventime.py -> get_eventime_topUrls_rotating_proxies </i> </br>
        </td>
   </tr>
</table>           

<table border=0>
   <tr>
      <td>
         <b>Method 2: Buy proxies using zenrows </b> </br>
         </td>
   </tr>
   <tr>
      <td>
         Other efficient way is to buy the proxies (like zenrows) and use them to scrape web pages. </br>
         Once purchase, you get API key which you need to pass. </br>
         Below python module demostrate this logic. </br>
            </td>
   </tr>
   <tr>
        <td>
            <i> livescore.py -> get_events_html_data_zenrows_proxy </i> <br />
         </td>
   </tr>
</table>               


4. <b> Provide user credentials for private data scraping </b>
<table border=0>
   <tr>
      <td>
         Some websites do not provide the content publicly for scraping.  <br>
         Before scraping, form or input (user and password) may need to fill.  
         There are different methods to scrape private data.
      </td>
   </tr>
</table>

<table border=0>
   <tr>
      <td>
         <b>Method 1: Using browser extension (Playwright and chromium)  </b> </br>
         </td>
   </tr>
   <tr>
      <td>
         Playwright also provides a mechanism to dynamically update the content. </br>
         It also have functions to provide inputs (like user credentials) and click the button </br>
         Below python module demostrate this logic. </br>
            </td>
   </tr>
   <tr>
        <td>
            <i> logincredential.py  -> get_data_user_credential </i> <br />
         </td>
   </tr>
</table>    

