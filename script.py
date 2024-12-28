from selenium import webdriver
from selenium.webdriver.chrome.service import Service


from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


service = Service("C:\Windows\chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get("https://x.com/home")

wait = WebDriverWait(driver, 10)  # Wait up to 10 seconds
try:
    trends_section = wait.until(
        EC.presence_of_element_located((By.XPATH, "//section[contains(., 'What’s Happening')]"))
    )
except TimeoutException:
    print("The page took too long to load or the element was not found.")
    driver.quit()
    exit()