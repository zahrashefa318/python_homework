#Task 3 ----------------------------------------------------------------------------------
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as chromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, TimeoutException, WebDriverException
from time import sleep
import pandas as pd
import json


driver=webdriver.Chrome(service=chromeService(ChromeDriverManager().install()))
URL="https://books.toscrape.com/"


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



results=[]
retry_and_delay(driver,URL)           
while True: 
    article_elements=driver.find_elements(By.XPATH,"//li//article[contains(@class,'product_pod')]")
    for article in article_elements:
         title=article.find_element(By.XPATH,".//h3//a").get_attribute("title")
         star_rating=article.find_element(By.XPATH,".//p[contains(@class,'star-rating')]").get_attribute("class").split()[-1]
         price=article.find_element(By.XPATH,".//div[contains(@class,'product_price')]/p[contains(@class,'price_color')]").text
         dic={
              "Title":title,
              "Rating":star_rating,
              "Price":price
         }
         results.append(dic)

    next_btn=driver.find_elements(By.XPATH,"//li[@class='next']/a")
    if not next_btn:
        break
    next_url=next_btn[0].get_attribute("href")
    sleep(2)
    retry_and_delay(driver,next_url)
   
books_dataset=pd.DataFrame(results)
print(books_dataset)

#Task 4---------------------------------------------------------------------
books_dataset.to_csv("get_books.csv",index=False)
books_dataset.to_json("get_books.json", orient="records",indent=4)





