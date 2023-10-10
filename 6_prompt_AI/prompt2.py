from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def prompt2(name, lname, place):
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

            new = chrome_browser.find_element(
                By().XPATH, "//a[@title='New']"
            )
            new.click()
            time.sleep(2)

            # name_1 = WebDriverWait(chrome_browser, 20).until(EC.element_located_to_be_selected(
            #     (By.XPATH, "//input[@id='input-153']")))

            name_1 = chrome_browser.find_element(
                By.XPATH, '//*[@name="firstName"]'
            )
            name_1.clear()
            name_1.send_keys(name)
            time.sleep(2)

            l_name = chrome_browser.find_element(
                By.XPATH, '//*[@name="lastName"]'
            )
            l_name.clear()
            l_name.send_keys(lname)
            time.sleep(2)

            company = chrome_browser.find_element(
                By.XPATH, '//*[@name="Company"]'
            )
            company.send_keys(place)

            time.sleep(2)

            save = chrome_browser.find_element(
                By.XPATH, '//*[@name="SaveEdit"]'
            )
            save.click()

            time.sleep(10)

            break

        except Exception as e:
            print(e)
            print("Try again")
