from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome('/home/emre/Documents/py_projects/chromedriver/chromedriver')
driver.get("https://eksisozluk.com")

search_box = driver.find_element_by_id("search-textbox")
search_box.clear()

userInput = "mustafa kemal atatürk" #Başlık örneği.
search_box.send_keys(userInput)
search_box.submit()

xpath_sukela_tumu = driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/section/div/div[1]/div[1]/span/a[1]")
xpath_sukela_bugun = driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/section/div/div[1]/div[1]/span/a[2]")


element_wait = WebDriverWait(driver, 10)

xpath_sukela_tumu.click()

""""
This section will be developed next releases.
try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "myDynamicElement"))
    )
finally:
    driver.quit()
"""""
