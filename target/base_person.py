import json
from lib2to3.pgen2 import driver
from logging import exception
from tokenize import String
from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from target.notifycation.mail import sendmail
import requests
from selenium.webdriver.remote.webelement import WebElement


def Execute(driver, startPage, endPage):
    print(f'Started {__file__} from {startPage} to {endPage}')
    while 1:
        for index in range(int(startPage), int(endPage)):
            try:
                ScanPageIndex(driver, index)
            except Exception as e:
                print(e)
                continue


def ScanPageIndex(driver: webdriver.Chrome, pageindex):
    print('---------------------------------------------------------------------------')
    print(f'Scan page {pageindex}')
    print('---------------------------------------------------------------------------')
    homePage = f'https://alonhadat.com.vn/nha-moi-gioi/long-an-t39.html?p={pageindex}'
    driver.get(homePage)
    agents = driver.find_elements_by_class_name('view-personal-page');
    for index in range(len(agents)):
        try:
            print(
                '******************************************************************************')
            print(f'Page {pageindex}, Url:{driver.current_url}')
            agents[index].click()
            scan_agent(driver)
            print(
                '******************************************************************************')
            driver.get(homePage)
            agents = driver.find_elements_by_class_name('view-personal-page')
        except Exception as e:
            print(e)
            print(
                '******************************************************************************')
            driver.get(homePage)
            agents = driver.find_elements_by_class_name('view-personal-page')
            continue


def scan_agent(driver: webdriver.Chrome):
    agent = driver.find_element_by_class_name('agent-infor');
    phoneContainer = agent.find_element_by_class_name('phone')
    phones = phoneContainer.find_elements_by_tag_name('a')
    for phone in phones:
        phoneText = phone.get_attribute("innerText").replace('.', '')
        print(phoneText)
        bcrmUser = get_bcrm_user_info(phoneText)
        print(bcrmUser)
        if bcrmUser[0]['Id'] == 0:
            print(agent.get_attribute("innerText"))
            name = agent.find_element_by_class_name('fullname')
            sendmail(phoneText, name.get_attribute("innerText"), '',
                     agent.get_attribute("innerText"), driver.current_url)


def get_bcrm_user_info(phoneText):
    userRes = requests.get(
        'https://apisso.batdongsan.com.vn/service/userclient.svc/Authenticate?password=1234567&systemId=8&userName=KhangNTH')
    json = userRes.json()
    certificate = json['Data']
    print(certificate)
    checkRes = requests.post(
        'https://addonbcrm.batdongsan.com.vn/AddOn/SearchCustomerV2', json={'keyword': phoneText, 'userName': certificate})
    checkBcrm = checkRes.json()
    return checkBcrm
