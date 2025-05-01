import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

URL = 'https://wordle.danielfrg.com/'


def init_webdriver():
    return webdriver.Firefox()


def play(driver):
    play_btn_xpath = '//*[@id="headlessui-dialog-1"]/div/div[2]/div[5]/button'
    play_btn = driver.find_element_by_xpath(play_btn_xpath)
    play_btn.click()


def try_word(driver, word: str):
    body = driver.find_element_by_tag_name('body')
    for char in word:
        body.send_keys(char)
        time.sleep(0.5)
    body.send_keys(Keys.ENTER)


driver = init_webdriver()
driver.get(URL)
play(driver)
try_word(driver, 'vamos')
