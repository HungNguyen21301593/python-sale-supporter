from time import sleep
from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from target.notifycation.mail import sendmail
import requests
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def Execute(driver):
    # startPage = input('Started Page :')
    startPage = 1
    # endPage = input('End Page :')
    endPage = 500

    print(f'Started from {startPage} to {endPage}')
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
    homePage = f'https://bds123.vn/nha-dat-ban-ho-chi-minh.html?page={pageindex}'
    driver.get(homePage)
    urls = loadUrls(driver)
    for index in range(len(urls)):
        try:
            print(f'Page {pageindex}, Url:{driver.current_url}')
            urls[index].click()
            print('clicked url')
            ScanUrl(driver)
            driver.get(homePage)
            urls = loadUrls(driver)
        except Exception as e:
            print(e)
            driver.get(homePage)
            urls = loadUrls(driver)
            continue


def loadUrls(driver: webdriver.Chrome):
    WebDriverWait(driver, 100).until(EC.element_to_be_clickable(
        (By.TAG_NAME, 'article')))
    urls = driver.find_elements(By.TAG_NAME, 'article')
    print(f'found {len(urls)} urls')
    return urls


def ScanUrl(driver: webdriver.Chrome):
    phone = driver.find_element_by_class_name('btn-phone')
    phoneText = phone.text.replace('.', '')
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
    name = driver.find_element_by_class_name('author-name')
    content = driver.find_element_by_class_name('post-main-content')
    
    if checkBcrm[0]['Id'] == 0:
        print(f'********************Found ${phoneText}')
        sendmail(phoneText, name.text, '',
                 content.text, driver.current_url)
    print(f'{driver.current_url}')
    print('******************************************************************************')
