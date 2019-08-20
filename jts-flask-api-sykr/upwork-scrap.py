# -*- coding: utf-8 -*-
"""
Created on Fri Jul 12 15:47:53 2019

@author: hp
"""

       
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from bs4 import BeautifulSoup 
import requests

import re
import time

from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import time
import sys
#import pickle
import json

from selenium.webdriver.firefox.options import Options


from datetime import date  
import  datetime
import csv

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC


def scraper():
    
    #return HttpResponse(out_json)
    #options = Options()
    #options.headless = True
    driver = webdriver.Chrome(executable_path = r'C:\Elsoul\elsoul-py\config\webdriver/chromedriver.exe')

    #driver = webdriver.Firefox(options=options,executable_path = '/usr/local/bin/geckodriver')
    #driver = webdriver.Firefox(executable_path = '/usr/local/bin/geckodriver')
    wait = WebDriverWait(driver, 10)
    driver.get("https://www.aliexpress.com")
    time.sleep(3)

    # skip ad popup if present
    try:
        
        wait.until(EC.element_to_be_clickable((By.XPATH, "//span[.='SKIP']"))).click()
    except TimeoutException:
        pass
    #ac_click = driver.find_element_by_xpath("/html/body/div[1]/div[3]/div/div/div[5]/div[3]/span/a/span").click()
    driver.find_element_by_xpath("/html/body/div[1]/div[5]/div[1]/div[2]/div/div[4]/div[1]/div[3]/span[2]/a").click()


    #driver.execute_script('arguments[0].click();',wait.until(EC.element_to_be_clickable((By.ID, "fm-login-id"))))
    #wait.until(EC.element_to_be_clickable((By.ID, "fm-login-id"))).send_keys("manishkumar.zed@gmail.com")


    element = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, "fm-login-id")))
    driver.execute_script("arguments[0].click();", element)
    element.send_keys("manishkumar.zed@gmail.com")   

    driver.find_element_by_id("fm-login-password").send_keys("KuManIsh18")

    submit = driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div/form/div[5]/button")
    
    submit.click()
    
    time.sleep(5)
        
    
    
scraper()





from selenium import webdriver
from time import sleep
driver = webdriver.Chrome(executable_path = r'C:\Elsoul\elsoul-py\config\webdriver/chromedriver.exe') 
driver.get('https://login.aliexpress.com')
sleep(10)
driver.switch_to_frame(0)
username = driver.find_element_by_name("loginId")
username.send_keys('manishkumar.zed@gmail.com')
sleep(5)
password = driver.find_element_by_name("password")
password.send_keys('KuManIsh18')
sleep(5) 
submit = driver.find_element_by_name('submit-btn')
submit.click()



from selenium import webdriver
from time import sleep

#driver = webdriver.Firefox(executable_path = r'C:\Elsoul\elsoul-py\config\webdriver/geckodriver.exe') 
driver = webdriver.Chrome(executable_path = r'C:\Elsoul\elsoul-py\config\webdriver/chromedriver.exe') 

driver.get("https://login.aliexpress.com/")

frame = driver.find_element_by_id("alibaba-login-box")
driver.switch_to.frame(frame)

driver.find_element_by_id("fm-login-id").send_keys("manishkumar.zed@gmail.com")
driver.find_element_by_id("fm-login-password").clear()
driver.find_element_by_id("fm-login-password").send_keys("KuManIsh18")
submit = driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div/form/div[5]/button")
    
submit.click()
    
