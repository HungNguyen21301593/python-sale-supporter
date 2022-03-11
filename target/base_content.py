import json
from logging import exception
from selenium import webdriver
from selenium.webdriver.common import action_chains
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from target.notifycation.mail import sendmail
import requests


def Execute(driver, startPage, endPage):
    # startPage = input('Started Page :')
    startPage = 1
    # endPage = input('End Page :')
    endPage = 500
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
    homePage = f'https://nha.chotot.com/toan-quoc/mua-ban-bat-dong-san?page={pageindex}'
    driver.get(homePage)
    urls = driver.find_elements_by_class_name('AdItem_adItem__2O28x')
    for index in range(len(urls)):
        try:
            print(f'Page {pageindex}, Url:{driver.current_url}')
            urls[index].click()
            ScanUrl(driver)
            driver.get(homePage)
            urls = driver.find_elements_by_class_name('AdItem_adItem__2O28x')
        except Exception as e:
            print(e)
            driver.get(homePage)
            urls = driver.find_elements_by_class_name('AdItem_adItem__2O28x')
            continue


def ScanUrl(driver: webdriver.Chrome):
    wait = WebDriverWait(driver, 100)

    phoneClickPath = '/html/body/div[1]/div[3]/div[1]/div/div[6]/div/div[2]/div[2]/div[1]/div/div/div'
    wait.until(EC.element_to_be_clickable(
        (By.XPATH, phoneClickPath)))
    phoneClick = driver.find_element_by_xpath(phoneClickPath)
    phoneClick.click()
    phone = driver.find_element_by_xpath(
        '/html/body/div[1]/div[3]/div[1]/div/div[6]/div/div[2]/div[2]/div[1]/div/div/span')
    phoneText = phone.text
    print(phoneText)
    userRes = requests.get(
        'https://apisso.batdongsan.com.vn/service/userclient.svc/Authenticate?password=1234567&systemId=8&userName=KhangNTH')
    json = userRes.json()
    certificate = json['Data']
    print(certificate)
    checkRes = requests.post(
        'https://addonbcrm.batdongsan.com.vn/AddOn/SearchCustomerV2', json={'keyword': phoneText, 'userName': certificate})
    checkBcrm = checkRes.json()
    print(checkBcrm)
    print(checkBcrm[0]['Id'])

    if checkBcrm[0]['Id'] == 0:
        name = driver.find_element_by_xpath(
            '/html/body/div[1]/div[3]/div[1]/div/div[6]/div/div[2]/div[1]/div/a/div[2]/div[1]/div/b')
        job = driver.find_element_by_xpath(
            '/html/body/div[1]/div[3]/div[1]/div/div[6]/div/div[2]/div[1]/div/div/div[1]/div/p')
        content = driver.find_element_by_xpath(
            '/html/body/div[1]/div[3]/div[1]/div/div[4]/div[2]/p')
        sendmail(phone.text, name.get_attribute("innerText"), job.get_attribute("innerText"),
                 content.text, driver.current_url)
        print(f'********************Found ${phoneText}')
        # InsertDb(phoneText, checkBcrm)
    print(f'{driver.current_url}')
    print('******************************************************************************')
