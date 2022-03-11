from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.utils import ChromeType

def SetupDriver():  
    chrome_options = Options()
    chrome_options.add_argument("--disable-notifications");
    chrome_options.add_argument("--start-maximized");
    # chrome_options.add_argument("--incognito");
    chrome_options.add_argument("--ignore-ssl-errors");
    chrome_options.add_argument("--ignore-certificate-error");
    chrome_options.add_argument("--disable-extensions");
    chrome_options.add_argument("--headless");
    chrome_options.add_argument("no-sandbox");
    chrome_options.add_argument("--disable-logging");
    chrome_options.add_argument("--disable-popup-blocking")
    chrome_options.add_argument("log-level=3")
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument('--disable-gpu')
    return webdriver.Chrome(ChromeDriverManager(chrome_type=ChromeType.GOOGLE).install(), chrome_options = chrome_options)