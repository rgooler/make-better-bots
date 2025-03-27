from selenium.webdriver.common.by import By
import undetected_chromedriver as uc
from time import sleep

linux_useragent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36'
mac_useragent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36"

# set up Undetected ChromeDriver
options = uc.ChromeOptions()
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
#options.add_argument('--window-size=1280,720')
options.add_argument('start-maximized')
options.add_argument("--disable-extensions")
options.add_argument(f"--user-agent={linux_useragent}")

# run in headless mode
#options.headless = True

# create a new instance of the Chrome driver
driver = uc.Chrome(options=options)

driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
driver.execute_cdp_cmd('Network.setUserAgentOverride', {"userAgent": linux_useragent})
print(driver.execute_script("return navigator.userAgent;"))


# navigate to the URL
driver.get("https://demo.fingerprint.com/playground")

# get the response body
response_body = driver.find_element(By.TAG_NAME, "body").text

# print the response
print(response_body)

sleep(300)
# close the browser
#driver.quit()