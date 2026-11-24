#Task 3 ----------------------------------------------------------------------------------
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as chromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, TimeoutException, WebDriverException
from time import sleep
import pandas as pd
import json
from urllib.robotparser import RobotFileParser

robot_parser=RobotFileParser()
robot_parser.set_url("https://durhamcounty.bibliocommons.com/robots.txt")
robot_parser.read()

driver=webdriver.Chrome(service=chromeService(ChromeDriverManager().install()))
URL="https://durhamcounty.bibliocommons.com/v2/search?query=learning%20spanish&searchType=smart"


def retry_and_delay(driver,url,max_attempts=3):
    for attempt in range(1,max_attempts+1):
        try:
            driver.get(url)
            return True
        except (TimeoutException,WebDriverException) as e:
                if attempt < max_attempts:
                    wait=2 * attempt
                    print(f"Waiting {wait} seconds before next attempt.")
                    sleep(wait)
    print("Giving up on {URL} after {max_attempts} attempts.")
    return False



result=[]
while True:
    print(URL)
    print("Allowed:", robot_parser.can_fetch("*", URL))
    if not robot_parser.can_fetch("*",URL):
         print(f"This url:{URL} is not allowed to scarp.")
         break

    retry_and_delay(driver,URL)
            
    li_elements=driver.find_elements(By.CSS_SELECTOR,'div.col-md-12.results-list-items li')
   

    for i in li_elements:
        title_element=i.find_element(By.CSS_SELECTOR,'span.title-content')
        Title=title_element.text.strip()

        author_elements=i.find_elements(By.CSS_SELECTOR,'a.author-link')
        Author=";".join(a.text.strip()for a in author_elements)
        
        date_and_Format_div=i.find_element(By.CSS_SELECTOR,'div.cp-format-info')
        format_year_element=date_and_Format_div.find_element(By.CSS_SELECTOR,'span.display-info-primary')
        Format_Year=format_year_element.text

        dic={"Title":Title,"Author":Author,"Format-Year": Format_Year}
        result.append(dic)
    #Find the next button in current page
    nextbtn=driver.find_element(By.CSS_SELECTOR,'section li.cp-pagination-item.pagination__next-chevron')
    next_btn_classes=nextbtn.get_attribute('class')
    print("Current URL:", URL)
    print("Next button classes:", next_btn_classes)
    if "pagination-item--disabled" in next_btn_classes:
         break
    URL=nextbtn.find_element(By.CSS_SELECTOR,'a').get_attribute('href')
     
    sleep(2)

books_dataset=pd.DataFrame(result)
print(books_dataset)

#Task 4---------------------------------------------------------------------
books_dataset.to_csv("get_books.csv",index=False)
books_dataset.to_json("get_books.json", orient="records",indent=4)





