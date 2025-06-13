#pip install selenium
#pip install webdriver_manager
#pip install pandas guardar en csv
#elegir version 3.11.4 64 bits abajo derecha
from time import sleep

from selenium import webdriver 
from selenium.webdriver.common.by import By 
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

opts = Options()

opts.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36")
#No abre navegador
opts.add_argument ("--headless")
driver = webdriver.Chrome (
    service=Service(ChromeDriverManager().install()), 
    options=opts
)
driver.get("https://www.airbnb.es/")
sleep(5)
"""
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

boton = driver.find_element(By.XPATH, '//button[@data-testid="show-more-button]')
for i in range(5):
    boton.click()
    boton = driver.find_element(By.XPATH, '//button[@data-testid="show-more-button"]')
    sleep(5)
# hay que hacer scroll para que cargue el resto de los elementos
"""
#Extraer los titulos
titulos = driver.find_elements(By.XPATH, '//div[@data-testid="listing-card-title"]')
for titulo in titulos:
    print(titulo.text)