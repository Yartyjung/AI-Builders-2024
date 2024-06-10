import logging.handlers
import time
import unicodedata
import logging
import numpy as np
import pandas as pd
from cleantext import clean
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from langdetect import detect



logging.basicConfig(filename=f'C:\\Users\\User\\Documents\\GitHub\\AI-Builders-2024\\review summarizer\\log{time.strftime("%H-%M-%S")}.log',
                    format='%(asctime)s | %(message)s',
                    filemode='w',
                    level=logging.INFO)

def scrape(url,bool,stergy,y,times): #[str(url),bool,str("normal"/"eager"),int(y position)]   
    logging.info('Start scraping...')
    
    review = []
    
    chrome_options = webdriver.ChromeOptions()
    # chrome_options.page_load_strategy = "normal"
    chrome_options.page_load_strategy = stergy
    chrome_options.add_argument('--disable-webusb')
    
    driver = webdriver.Chrome(options=chrome_options) 
    
    if bool == True :
        driver.set_window_position(-1000, 0)
    
    driver.maximize_window()
    driver.get(url)

    logging.info(f'Opening chrome for {url}')
    logging.info('Start scrolling...')
    
    time.sleep(2)
    
    driver.execute_script(f"window.scrollTo(0, {y})")
    
    logging.info(f'{time.strftime("%H:%M:%S")} |finished scrolling...')
    
    time.sleep(1)
    
    soup = BeautifulSoup(driver.page_source,features="html.parser")
    
    elements = soup.find_all('div', class_='item-content')
    
    for element in elements :
        
        text = element.get_text(strip = True)
        
        review.append(text)
        
    logging.info(f'Finished get soup for {url} page 1')
    
    time.sleep(1)

    for page in range(times) :
        
        try : 
            
            WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH,'//*[@id="module_product_review"]/div/div/div[2]')))
        
            driver.find_element(By.XPATH,'//*[@id="module_product_review"]/div/div/div[3]/div[2]/div/button[2]/i').click()
            
            time.sleep(0.7)
            
            soup = BeautifulSoup(driver.page_source,features="html.parser")
            
            elements = soup.find_all('div', class_='content')
            
            for element in elements : 
                
                text = element.get_text(strip = True)
        
                review.append(text)

            logging.info(f'Finished get soup for {url} page {page+2}')
            
            time.sleep(0.7)
        
        except :
            
            logging.info('No page to go further')
            logging.info('Started breaking loop...')
            
            break
    
    logging.info('Closing chrome driver...')
    
    driver.quit()
        
    return review

def annotate (review,url) :

    logging.info(f'Start annotating {url}')

    annotated_list_th = []
    for text in review :
        try :
            if text :
                cleaned = text.replace("TH_TISI","").replace("\n"," ").replace("(","").replace(")","").replace("\\","").replace("Damaged box","")
                cleaned = unicodedata.normalize("NFKD", cleaned)
                cleaned = clean(cleaned,extra_spaces=True,)
                try :
                    if detect(cleaned) == "th" and "คะแนน" not in cleaned : 
                        annotated_list_th.append(cleaned)
                except :
                    pass
        except:
            pass
    logging.info(f'finished annotate for {url}')
    return annotated_list_th


def write_to_csv (arr,name):
    go = list(set(arr))
    print(type(go))
    print(go)
    np.savetxt(f"{name}.csv",
               go,
               delimiter=",",
               fmt="% s",
               encoding="utf-8")

finish = []

urls = ["https://www.lazada.co.th/products/i2643219630-s17164368334.html"]
        # rename dude
for url in urls :
    for scrapes in scrape(url,True,"normal",1200,70) :
        finish.append(scrapes)
    print(len(finish))
write_to_csv(annotate(finish,None),"box")