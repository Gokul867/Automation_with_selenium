from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def prompt3():
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
            chrome_browser.implicitly_wait(40)
            chrome_browser.get(
                'https://login.salesforce.com/?locale=in'
            )

            box = chrome_browser.find_element(
                By.XPATH, '//*[@id="username"]')
            box.clear()
            box.send_keys('gokulraj48150-p0wv@force.com')

            pas = chrome_browser.find_element(
                By.XPATH, '//*[@id="password"]')
            pas.clear()
            pas.send_keys('Aish@@12345')

            time.sleep(3)
            search = chrome_browser.find_element(
                By.XPATH, '//*[@id="Login"]'
            )
            search.click()
            time.sleep(1)

            chrome_browser.refresh()

            time.sleep(2)

            # remind_later = chrome_browser.find_element(
            #     By.XPATH, '//*[@id="editPage"]/p[2]/a[1]'
            # )
            # remind_later.click()
            # time.sleep(1)

            # chrome_browser.refresh()

            leads = chrome_browser.find_element(
                By.XPATH, "//a[@title='Leads']"
            )

            chrome_browser.execute_script("arguments[0].click();", leads)
            time.sleep(2)

            # james

            james = chrome_browser.find_element(
                By.XPATH, '//*[@id="brandBand_1"]/div/div/div/div/div[2]/div/div[1]/div[2]/div[2]/div[1]/div/div/table/tbody/tr[1]/th/span/a')
            james.click()

            time.sleep(2)

            log_call = chrome_browser.find_element(

                By.XPATH, "//button[@title='Log a Call']"
            )
            log_call.click()
            time.sleep(2)

            comments = chrome_browser.find_element(
                By.XPATH, "//textarea[@role='textbox']"
            )
            comments.clear()
            comments.send_keys('He is looking to buy 100 widgets')
            time.sleep(2)

            new = chrome_browser.find_element(
                By.XPATH, "//button[@class='slds-button slds-button--brand cuf-publisherShareButton uiButton']"
            )
            new.click()

            time.sleep(10)

            break

        except Exception as e:
            print(e)
            print("Try again")
