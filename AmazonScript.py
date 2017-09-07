from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

#setting up enviroment
driver = webdriver.Firefox()
driver.get("https://www.amazon.com")
loginElement=driver.find_element_by_id("nav-link-accountList")
loginElement.click()

#user credentials
userMail = "username"
userPassword = "password"

#text for searching operation
searchText = "Samsung"

userLoginMail = driver.find_element_by_id("ap_email")
userLoginPassword = driver.find_element_by_id("ap_password")

userLoginMail.send_keys(userMail)
userLoginPassword.send_keys(userPassword)

loginButton=driver.find_element_by_id("signInSubmit")
loginButton.click()

searchBox = driver.find_element_by_id("twotabsearchtextbox")
#searchBox.click()
searchBox.clear()
searchBox.send_keys(searchText)
searchBox.send_keys(Keys.RETURN)
driver.implicitly_wait(30)
#driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

secondPage = driver.find_element_by_link_text('2')
#secondPage = driver.find_element_by_id("pagnNextLink")
secondPage.click()

#li id result_29
#ul id s-results-list-atf
item = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#result_29 a[class='a-link-normal s-access-detail-page  s-color-twister-title-link a-text-normal']")))
item.click()

addList = driver.find_element_by_id('add-to-wishlist-button-submit')
addList.click()
#wishList = driver.find_element_by_link_text('Wish List')
#wishList.click()

deleteList = driver.find_element_by_id('WLHUC_viewlist')
deleteList.click()

deleteBttn = driver.find_element_by_name('submit.deleteItem')
deleteBttn.click()
