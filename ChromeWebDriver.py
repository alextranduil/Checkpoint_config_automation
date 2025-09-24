from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

# Function to set up Chrome WebDriver
def set_up_chrome_web_driver(headless=True):
    """
    Sets up and returns a Chrome WebDriver instance.
    """
    service = Service(ChromeDriverManager().install())
    options = Options()
    if headless:
        options.add_argument("--headless")
    driver = webdriver.Chrome(service=service, options=options)
    return driver