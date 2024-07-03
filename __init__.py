from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import time

# Initialize Chrome WebDriver
options = webdriver.ChromeOptions()
options.add_argument('--disable-blink-features=AutomationControlled')

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# LinkedIn login URL
login_url = "https://www.linkedin.com/login"

# Open the login URL
driver.get(login_url)

# Wait for the page to load completely
time.sleep(5)

# Enter your LinkedIn credentials
username = ""
password = ""

# Find the username and password fields and input the credentials
username_field = driver.find_element(By.ID, "username")
password_field = driver.find_element(By.ID, "password")

username_field.send_keys(username)
password_field.send_keys(password)

# Press enter to log in
password_field.submit()

# Wait for the login process to complete
time.sleep(5)

# Prompt the user to enter job keywords
job_keywords = input("Enter job keywords to search (e.g., Software Engineer): ")

# LinkedIn URL for job search based on user input
url = f"https://www.linkedin.com/jobs/search/?keywords={job_keywords}&location=United%20States&f_WT=2&f_E=2&geoId=&trk=public_jobs_jobs-search-bar_search-submit&position=1&pageNum=0"

# Open the URL
driver.get(url)

# Wait for the page to load completely
time.sleep(5)


# Function to toggle "Past 24 hours" filter
def toggle_past_24_hours():
    try:
        # Click on the "Date Posted" filter button
        date_filter_button = driver.find_element(By.ID, "searchFilter_timePostedRange")
        date_filter_button.click()

        # Wait for the dropdown to appear
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "search-reusables__filter-pill-button")))

        # Click on the "Past 24 hours" option within the dropdown
        past_24_hours_option = driver.find_element(By.XPATH, '//span[contains(text(), "Past 24 hours")]')
        past_24_hours_option.click()

        # Wait for the page to reload with the filter applied
        time.sleep(5)
    except Exception as e:
        print(f"Error toggling past 24 hours filter: {e}")


# Toggle the "Past 24 hours" filter
toggle_past_24_hours()


# Define a function to scroll to the bottom of the page
def scroll_to_bottom():
    last_height = driver.execute_script("return document.body.scrollHeight")
    while True:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(3)
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height


# Scroll to the bottom of the page to load all job postings
scroll_to_bottom()

# Find all job cards
job_cards = driver.find_elements(By.CSS_SELECTOR, '.job-card-container')

# Extract job information
jobs = []
for card in job_cards:
    job_title = card.find_element(By.CSS_SELECTOR, '.job-card-list__title').text
    company_name = card.find_element(By.CSS_SELECTOR, '.job-card-container__company-name').text
    location = card.find_element(By.CSS_SELECTOR, '.job-card-container__metadata-item').text
    date_posted = card.find_element(By.CSS_SELECTOR, '.job-card-container__listed-time').text
    job_link = card.find_element(By.CSS_SELECTOR, '.job-card-list__title a').get_attribute('href')

    jobs.append({
        'Job Title': job_title,
        'Company': company_name,
        'Location': location,
        'Date Posted': date_posted,
        'Job Link': job_link
    })

# Convert job information to a DataFrame
jobs_df = pd.DataFrame(jobs)

# Save DataFrame to a CSV file
jobs_df.to_csv('linkedin_jobs.csv', index=False)

# Close the driver
driver.quit()
