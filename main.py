# LinkedIn  Automation (Login + Feed + Posts)

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time
import os

# Enter your credentials 
USERNAME = "your_email_here"
PASSWORD = "your_password_here"

# screenshots folder
if not os.path.exists("screenshots"):
    os.makedirs("screenshots")

# Chrome options
options = Options()
options.add_argument("--start-maximized")

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

try:
    wait = WebDriverWait(driver, 20)

    # Open LinkedIn login page
    driver.get("https://www.linkedin.com/login")

    # Enter username
    wait.until(EC.presence_of_element_located((By.ID, "username"))).send_keys(USERNAME)

    # Enter password
    driver.find_element(By.ID, "password").send_keys(PASSWORD)

    time.sleep(2)  # slight delay to mimic human

    # Click login
    driver.find_element(By.XPATH, "//button[@type='submit']").click()

    # Verify login success
    wait.until(EC.presence_of_element_located(
        (By.XPATH, "//input[contains(@placeholder,'Search')]")
    ))
    print("Login Successful")

    # Screenshot after login
    driver.save_screenshot("screenshots/home_page.png")

    # Wait for feed to load
    time.sleep(5)

    # Scroll to load posts
    for _ in range(5):
        driver.execute_script("window.scrollBy(0, 800);")
        time.sleep(2)

    print("\n========== TOP 5 POSTS ==========\n")

    # Capture posts
    posts = driver.find_elements(By.XPATH, "//div[contains(@class,'update-components-text')]")

    collected_posts = []

    for post in posts:
        text = post.text.strip()
        if text and len(text) > 40:
            collected_posts.append(text)

    # Fallback method if posts not found
    if len(collected_posts) < 5:
        print("Using fallback method...\n")

        body_text = driver.find_element(By.TAG_NAME, "body").text
        lines = body_text.split("\n")

        for line in lines:
            if len(line) > 60:
                collected_posts.append(line)
            if len(collected_posts) >= 5:
                break

    # Print top 5 posts
    for i, post in enumerate(collected_posts[:5]):
        print(f"Post {i+1}:\n{post}\n{'-'*60}")

except TimeoutException:
    print("Login Failed or Page Not Loaded")
    driver.save_screenshot("screenshots/login_failed.png")

finally:
    time.sleep(5)
    driver.quit()