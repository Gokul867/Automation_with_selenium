from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from prompt2 import prompt2
from prompt3 import prompt3
from prompt4 import prompt4


def prompt1(input1, cost):
    for i in range(0, 3):
        try:
            options = webdriver.ChromeOptions()

            options.add_experimental_option(
                'excludeSwitches', ['enable-logging'])

            chrome_browser = webdriver.Chrome(
                service=Service('chromedriver.exe'),
                options=options,
            )

            chrome_browser.maximize_window()
            chrome_browser.implicitly_wait(10)
            chrome_browser.get(
                'https://www.redfin.com/'
            )

            box = chrome_browser.find_element(
                By.XPATH, '//*[@id="search-box-input"]')
            box.clear()
            box.send_keys(input1)

            time.sleep(3)
            search = chrome_browser.find_element(
                By.XPATH, '//*[@id="tabContentId0"]/div/div/form/div[1]/button'
            )
            search.click()
            time.sleep(2)
            chrome_browser.refresh()
            # PRICE
            search1 = chrome_browser.find_element(
                By.XPATH, '//*[@aria-label="Price"]'
            )
            search1.click()
            time.sleep(2)
            price_max = chrome_browser.find_element(
                By.XPATH, '//input[@placeholder="Enter max"]'
            )
            price_max.send_keys(cost)
            clk = chrome_browser.find_element(
                By.XPATH, '//*[@id="sidepane-header"]/div/div[1]/form/div[2]/div/div[2]/div[1]/div/div[2]/div/button[2]/span'
            )
            clk.click()
            time.sleep(2)
            # BED  ROOMS
            search2 = chrome_browser.find_element(
                By.XPATH, '//*[@id="sidepane-header"]/div/div[1]/form/div[4]/div/span'
            )
            search2.click()
            time.sleep(2)
            bed_max = chrome_browser.find_element(
                By.XPATH, '//*[@id="sidepane-header"]/div/div[1]/form/div[4]/div[2]/div[1]/div/div[1]/div/div[1]/div/div[2]/div/div/div/div[5]'
            )
            bed_max.click()
            # bath_max = chrome_browser.find_element(
            #     By.XPATH, '//*[@id="sidepane-header"]/div/div[1]/form/div[4]/div[2]/div[1]/div/div[1]/div/div[1]/div/div[2]/div/div/div/div[6]'
            # )
            # # Bath room
            # bath_max.click()
            # clk1 = chrome_browser.find_element(
            #     By.XPATH, '//*[@id="sidepane-header"]/div/div[1]/form/div[4]/div[2]/div[1]/div/div[2]/div/button[2]/span'
            # )
            # clk1.click()
            time.sleep(10)
            break
        except Exception as e:
            print(e)
            print("check for Internet and chrome Browser version")


if __name__ == '__main__':
    t = 4
    while t:
        prompt = input()
        if 'house' in prompt:
            house = prompt[11:16]
            cost = prompt[-2:-5:-1]
            prompt1('Houston', 600000)
        elif 'Add' in prompt:
            prompt2('Max', 'Nye', 'Workplete')
        elif 'call' in prompt:
            prompt3()
        elif 'Find' in prompt:
            prompt4('refrigerator', '1000')
        else:
            print("Sorry Iam Programmed to do only 3 tasks")
        t = t-1
