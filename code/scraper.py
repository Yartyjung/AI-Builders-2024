import time
import unicodedata
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from langdetect import detect


# def get_df(soup,pagenum):
#     return pd.DataFrame([{ "page" : pagenum,'url': i.find('"').get()} for i in soup.find_all('div', class_='content')])

def scrape():   
    
    chrome_options = webdriver.ChromeOptions()
    # chrome_options.page_load_strategy = "normal"
    chrome_options.page_load_strategy = "eager"
    chrome_options.add_argument('--disable-webusb')
    
    driver = webdriver.Chrome(options=chrome_options) 
    driver.set_window_position(-1000, 0)
    driver.maximize_window()
    
    driver.get("https://www.lazada.co.th/products/zombie-kittens-card-game-by-exploding-kittens-i4649902413-s19117770627.html")
    
    print("Opened chrome")
    print("start scrolling...")
    
    time.sleep(2)
    
    driver.execute_script("window.scrollTo(0, 1500)")
    
    print("finished scrolling...")
    
    time.sleep(5)
    
    soup = BeautifulSoup(driver.page_source,features="html.parser")
    
    print("after")
    
    elements = soup.find_all('div', class_='content')
    
    review = []
    
    for element in elements :
        
        text = element.get_text(strip = True)
        
        review.append(text)
        
    print("finished get soup")
    
    print(f'Saved soup and dataframe from page 1')
    
    time.sleep(3)

    for page in range(20) :
        
        try : 
            
            WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH,'//*[@id="module_product_review"]/div/div/div[2]')))
        
            driver.find_element(By.XPATH,'//*[@id="module_product_review"]/div/div/div[3]/div[2]/div/button[2]/i').click()
            
            # driver.execute_script("window.scrollTo(0, 3300)")
            
            time.sleep(2)
        
            # time.sleep(1)

            # driver.execute_script("window.scrollTo(0, 3100)")

            # time.sleep(1)
            
            soup = BeautifulSoup(driver.page_source,features="html.parser")
            
            elements = soup.find_all('div', class_='content')
            
            for element in elements : 
                
                text = element.get_text(strip = True)
        
                review.append(text)

            time.sleep(1)
        
        except :
            
            print("None to go further")
            
            break

    # print(review)
    
    driver.quit()

    return review

def annotate (review) :
    annotated_list_th = []
    for text in review :
        if text :
            cleaned = text.replace("TH_TISI","").replace("\n","").replace("(","").replace(")","").replace("\\","").replace("Damaged box","")
            cleaned = unicodedata.normalize("NFKD", cleaned)
            try :
                if detect(cleaned) == "th" and "คะแนน" not in cleaned : 
                    annotated_list_th.append(cleaned)
                else : 
                    pass
            except :
                pass
    return annotated_list_th

print(annotate(scrape()))


