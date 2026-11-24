#Task 6: Scraping Structured Data--------------------------------
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as chromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, TimeoutException, WebDriverException
import time
import csv

driver=webdriver.Chrome(service=chromeService(ChromeDriverManager().install()))

def retry_delay(driver, url, max_attempts=3):
    for attempt in range(1, max_attempts+1):
        try:
            driver.get(url)
            return True
        except (TimeoutException,WebDriverException) as e:
            if attempt< max_attempts:
                wait=2 * attempt
                time.sleep(wait)
            else:
                print(f"Giving up on url: {url} because of :{e}")
                return False

retry_delay(driver,"https://owasp.org/www-project-top-ten/")

recent_top_ten_link=driver.find_element(By.XPATH,"//a[contains(@href,'2025')]")
print(recent_top_ten_link.get_attribute("href"))
url=recent_top_ten_link.get_attribute("href")
retry_delay(driver,url)
links=driver.find_elements(By.XPATH, "//h3[@id='top-102025-list']/following-sibling::ol[1]/li/a")
vul_list=[]
for link in links:
    title=link.text
    href=link.get_attribute("href")
    dic={}
    dic["Title"]=title
    dic["Link"]=href
    vul_list.append(dic)

print(vul_list)

with open("owasp_top_10.csv","w",newline="") as file:
    writer=csv.DictWriter(file,fieldnames=["Title","Link"])
    writer.writeheader()
    writer.writerows(vul_list)

