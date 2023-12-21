from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://amasty.com/")
print(driver.title)

search = driver.find_element(By.NAME, "q")
search.send_keys("catalog")
search.send_keys(Keys.RETURN)

try:
    result = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "ol.product-items"))
    )
    productName = result.find_element(By.CSS_SELECTOR, "div.product-item-details")
    for product in productName:
        print(product.text)
finally:
    driver.quit()