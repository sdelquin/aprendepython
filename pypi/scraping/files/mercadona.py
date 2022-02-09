from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

geo = (28.1035677, -15.5319742)
URL = f'https://info.mercadona.es/es/supermercados?coord={geo[0]}%2C{geo[1]}'

options = Options()
options.headless = True
driver = webdriver.Firefox(options=options)
driver.get(URL)

cookies = driver.find_element_by_id('third-btn')
cookies.click()

body = driver.find_element_by_tag_name('body')
# Scroll to bottom in order to view "Ver todos"
driver.execute_script('arguments[0].scrollIntoView(false)', body)

see_all_xpath = '/html/body/div[1]/div[3]/div/div/div[2]/div[1]/ul/div/button'
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, see_all_xpath)))

see_all = driver.find_element_by_xpath(see_all_xpath)
see_all.click()

for li in driver.find_elements_by_class_name('panelLateralResultadosElemento '):
    h3 = li.find_element_by_tag_name('h3')
    print(h3.text)
