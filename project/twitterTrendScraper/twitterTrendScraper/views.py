from django.shortcuts import render
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

from .models import TrendingHashtags

# Set the path to ChromeDriver
PATH = "C:/Windows/chromedriver.exe"
def home(request):
    return render(request, 'index.html');

def get_trending_hashtags():
    
    #  replace with yours
    PROXY =""

    chrome_options = Options()
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--headless")
    chrome_options.add_argument(f"--proxy-server={PROXY}")


    service = Service(PATH)
    driver = webdriver.Chrome(service=service, options=chrome_options)
    
    try:
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
        password.send_keys("replace with your")

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
            if topic.text.strip().startswith("#"):
                hashtag_list.append(topic.text.strip())

       
        hashtag_list = set(hashtag_list);
        return hashtag_list

    finally:
        driver.quit()

# Django view to render the hashtags
def trending_hashtags_view(request):
    hashtags = get_trending_hashtags()
    if hashtags:
        TrendingHashtags.objects.create(
            trend1=hashtags[0] if len(hashtags) > 0 else None,
            trend2=hashtags[1] if len(hashtags) > 1 else None,
            trend3=hashtags[2] if len(hashtags) > 2 else None,
            trend4=hashtags[3] if len(hashtags) > 3 else None,
        )

    return render(request, 'trend.html', {'hashtags': hashtags})
