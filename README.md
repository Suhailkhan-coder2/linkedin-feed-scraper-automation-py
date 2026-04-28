# LinkedIn Feed Automation using Selenium (Python)

# Project Overview

This project automates the process of logging into LinkedIn and extracting the top 5 visible posts from the home feed using Selenium WebDriver in Python.

It demonstrates practical skills in **automation testing, web scraping, and handling dynamic web elements**, which are essential for QA and Automation roles.



# Features

* Automated login to LinkedIn
* Navigation to home feed/dashboard
* Extraction of top 5 posts from feed
* Console output of post content
* Screenshot capture (success & failure)
* Explicit wait handling for synchronization
* Exception handling for robustness
* Fallback mechanism for dynamic content



# Tech Stack

* Python
* Selenium WebDriver
* ChromeDriver (via webdriver-manager)


# Project Structure


linkedin-feed-scraper-automation-py/
│── main.py
│── screenshots/
│── .gitignore




# Setup Instructions

# 1. Clone Repository


git clone https://github.com/Suhailkhan-coder2/linkedin-feed-scraper-automation-py.git
cd linkedin-feed-scraper-automation-py


# 2. Install Dependencies


pip install selenium webdriver-manager


# 3. Update Credentials

Open main.py and update:


USERNAME = "your_email_here"
PASSWORD = "your_password_here"


 Note: Do not push real credentials to GitHub.



# How to Run


python main.py




# Output

* Console displays top 5 posts from LinkedIn feed
* Screenshots saved in screenshots/ folder



# Challenges & Handling

* LinkedIn uses dynamic content and anti-bot mechanisms
* Implemented:

  * Explicit waits
  * Scroll-based loading
  * Fallback text extraction method



# Key Learnings

* Selenium automation with real-world applications
* Handling dynamic web elements
* Writing robust and maintainable test scripts
* Debugging automation failures



#  Author

Suhail Khan
Aspiring Software Developer | Python Full Stack Developer



# Note for Recruiters

This project showcases hands-on experience in automation testing using Selenium, including real-world challenges like dynamic UI handling and fallback strategies.

