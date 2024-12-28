from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


# Set the path to ChromeDriver
PATH = "C:/Windows/chromedriver.exe"

# Configure Chrome options
chrome_options = Options()
chrome_options.add_argument("--disable-extensions")
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("--headless")

service = Service(PATH)
driver = webdriver.Chrome(service=service, options=chrome_options)

# Navigate to Twitter login page
driver.get("https://x.com/i/flow/login")


sleep(5)  # Shorter sleep for page load

# Username
wait = WebDriverWait(driver, 10)
username = wait.until(EC.presence_of_element_located((By.XPATH, '//input[@name="text"]')))
username.send_keys("ankitkumar.97738911@gmail.com")

# Next button
next_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'Next')]")))
next_button.click()


sleep(10)

# Username for next step
username = wait.until(EC.presence_of_element_located((By.XPATH, '//input[@name="text"]')))
username.send_keys("Ankit977006")

new_next_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'Next')]")))
new_next_button.click()


sleep(10)

# Password
password = wait.until(EC.presence_of_element_located((By.XPATH, '//input[@name="password"]')))
password.send_keys("twitterisNewNews@123")

# Log in button
login_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'Log in')]")))
login_button.click()


sleep(15)



# Find trends
whats_happening_section = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//div[@aria-label='Timeline: Trending now']"))
)  
trending_topics = whats_happening_section.find_elements(By.XPATH, ".//span")

hashtag_list = []

for topic in trending_topics:
    if topic.text.strip():
        print(topic.text.strip())


for topic in trending_topics:
    if topic.text.strip().startswith("#"):
        hashtag_list.append(topic.text.strip())

print(hashtag_list) 
hashtag_list = set(hashtag_list);
print(hashtag_list)


# Close the browser
driver.quit()
