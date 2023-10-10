from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def prompt4(item, price):
    for i in range(0, 1):
        try:
            options = webdriver.ChromeOptions()

            options.add_experimental_option(
                'excludeSwitches', ['enable-logging'])

            chrome_browser = webdriver.Chrome(
                service=Service('chromedriver.exe'),
                options=options,
            )

            chrome_browser.maximize_window()
            chrome_browser.implicitly_wait(60)
            chrome_browser.get(
                'https://sfbay.craigslist.org/'
            )
            box = WebDriverWait(chrome_browser, 10).until(EC.presence_of_element_located(
                (By.XPATH, "//a[@class='ppa']")))
            # box = chrome_browser.find_element(
            #     By.XPATH, "//a[@class='ppa']")
            box.click()
            time.sleep(5)
            chrome_browser.refresh()

            search = WebDriverWait(chrome_browser, 10).until(EC.presence_of_element_located(
                (By.XPATH, "//input[@placeholder='search appliances']")))

            # search = chrome_browser.find_element(
            #     By.XPATH, "//input[@placeholder='search appliances']")
            # search.clear()
            search.send_keys(item)
            time.sleep(5)

            button = WebDriverWait(chrome_browser, 10).until(EC.presence_of_element_located(
                (By.XPATH, "//button[@type='submit']")))

            # button = chrome_browser.find_element(
            #     By.XPATH, "//button[@type='submit']")
            button.click()
            time.sleep(5)

            max_cost = WebDriverWait(chrome_browser, 10).until(EC.presence_of_element_located(
                (By.XPATH, "//input[@placeholder='max']")))

            # max_cost = chrome_browser.find_element(
            #     By.XPATH, "//input[@placeholder='max']")
            # max_cost.clear()
            max_cost.send_keys(price)
            time.sleep(5)

            apply = WebDriverWait(chrome_browser, 10).until(EC.presence_of_element_located(
                (By.XPATH, "//button[@class='bd-button cl-exec-search label-only']")))

            # apply = chrome_browser.find_element(
            #     By.XPATH, "//button[@class='bd-button cl-exec-search label-only']")
            apply.click()
            time.sleep(5)

            pic = WebDriverWait(chrome_browser, 20).until(EC.presence_of_element_located(
                (By.XPATH, "//a[@class='titlestring']")))

            # pic = chrome_browser.find_element(
            #     By.XPATH, "//a[@class='titlestring']")
            pic.click()
            time.sleep(5)

            reply_b = WebDriverWait(chrome_browser, 20).until(EC.presence_of_element_located(
                (By.XPATH, "//button[@role='button']")))

            # reply_b = chrome_browser.find_element(
            #     By.XPATH, "//button[@role='button']")
            reply_b.click()
            time.sleep(5)

            reply_c = chrome_browser.find_element(
                By.XPATH, "//button[@class='reply-option-header']")
            reply_c.click()
            time.sleep(5)

            reply_d = chrome_browser.find_element(
                By.XPATH, "//a[@class='reply-email-webmail-link gmail']")
            reply_d.click()
            time.sleep(2)

            # gmail = chrome_browser.find_element(
            #     By.XPATH, '//*[@id="identifierId"]')
            # gmail.send_keys('dummyEmail8000@gmail.com')
            # time.sleep(2)

            # ok = chrome_browser.find_element(
            #     By.XPATH, "//*[@class='VfPpkd-RLmnJb']")
            # ok.click()
            # time.sleep(2)

            # password = chrome_browser.find_element(
            #     By.XPATH, '//input[@type=password"]')
            # password.send_keys('sun@@@123')
            # time.sleep(2)

            # ok1 = chrome_browser.find_element(
            #     By.XPATH, "//*[@class='VfPpkd-RLmnJb']")
            # ok1.click()
            # time.sleep(2)

            time.sleep(10)

        except Exception as e:
            print(e)
            print("Try again")
