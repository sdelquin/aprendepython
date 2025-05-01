from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

GEOLOC = (28.1247618, -15.4358226)
URL = f'https://info.mercadona.es/es/supermercados?coord={GEOLOC[0]}%2C{GEOLOC[1]}'

options = Options()
options.add_argument('-headless')

driver = webdriver.Firefox(options=options)
driver.get(URL)

css_selector = 'p.blq-drcha-cookies a#third-btn'
elem = driver.find_element(By.CSS_SELECTOR, css_selector)
elem.click()

elem = driver.find_element(By.TAG_NAME, 'body')
driver.execute_script('arguments[0].scrollIntoView(false)', elem)

css_selector = 'div.verTodosLista button'
elem = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, css_selector))
)
elem.click()

print(f'Supermercados MERCADONA cerca de {GEOLOC}')
print('----------------------------------------------------------')

css_selector = 'h3.panelLateralResultadosDireccion'
for res in driver.find_elements(By.CSS_SELECTOR, css_selector):
    print(res.text)

driver.quit()
