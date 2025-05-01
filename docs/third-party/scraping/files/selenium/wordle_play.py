from selenium import webdriver

URL = 'https://wordle.danielfrg.com/'

driver = webdriver.Firefox()

driver.get(URL)

play_btn_xpath = '//*[@id="headlessui-dialog-1"]/div/div[2]/div[5]/button'
play_btn = driver.find_element_by_xpath(play_btn_xpath)
play_btn.click()
