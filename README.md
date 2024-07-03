Running LinkedIn Job Scraper
This script uses Selenium to scrape job postings from LinkedIn. It automates the process of logging in, applying filters, scrolling through job listings, and saving the data to a CSV file.

Prerequisites
Python: Ensure Python is installed on your system. You can download it from python.org.
Chrome Browser: This script uses Chrome WebDriver. Make sure you have Google Chrome installed.
Setup Instructions
Clone the Repository:

Clone this repository to your local machine using Git:
bash
Copy code
git clone <repository_url>
Install Dependencies:

Navigate to the project directory:
bash
Copy code
cd linkedin-job-scraper
Install the required Python packages using pip:
Copy code
pip install -r requirements.txt
Set Up Chrome WebDriver:

The script uses Chrome WebDriver managed by webdriver_manager. It will automatically download the appropriate driver.
Update LinkedIn Credentials:

Open the script (linkedin_job_scraper.py) in a text editor.
Replace username and password variables with your LinkedIn credentials:
python
Copy code
username = "your_linkedin_username"
password = "your_linkedin_password"
Run the Script:

Execute the script from your terminal:
Copy code
python linkedin_job_scraper.py
Wait for Execution:

The script will log into LinkedIn, apply filters for jobs in the United States (remote, entry-level), scroll through job listings, and save the data to a CSV file (linkedin_jobs.csv).
Check Output:

After completion, check the project directory for linkedin_jobs.csv containing scraped job data.
Close the Script:

Once done, the script will automatically close the Chrome WebDriver.
Notes
Adjust the script as needed for different job search criteria by modifying url variable and toggle_past_24_hours function parameters.
Ensure your LinkedIn credentials are kept secure and not shared publicly.
