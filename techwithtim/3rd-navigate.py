from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://amasty.com/")
link = driver.find_element(By.LINK_TEXT, "Blog")
link.click()

try:
    sort = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.LINK_TEXT, "Extensions & Updates"))
    )
    sort.click()
    driver.back()
    driver.back()
    driver.forward()
    
except:
    driver.quit()