from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep

# set up Undetected ChromeDriver
options = Options()
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('start-maximized')
options.add_argument("--disable-extensions")

# run in headless mode
#options.headless = True

# create a new instance of the Chrome driver
driver = webdriver.Chrome(options=options)

# navigate to the URL
driver.get("https://demo.fingerprint.com/playground")

# get the response body
response_body = driver.find_element(By.TAG_NAME, "body").text

# print the response
print(response_body)

sleep(300)
# close the browser
#driver.quit()