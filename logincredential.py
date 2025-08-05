from playwright.sync_api import sync_playwright

def get_data_user_credential(url,user,password):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        # Navigate to login page
        page.goto(url)

        # Fill in login credentials
        page.fill("input#email", user)
        page.fill("input#password", password)
        page.select_option("select#city", value="Hyderabad")
        # Click the login button
        page.click("input[type=submit]")

        # Optional: wait for dashboard to load
        page.wait_for_selector("div#content")

        # Take a screenshot to confirm login
        page.screenshot(path="dashboard.png")

        browser.close()

def test_data_user_credential():
    get_data_user_credential("https://www.countryclubworld.com/ccmember/index.php","sandeepsatpal@gmail.com","PASSWORD")