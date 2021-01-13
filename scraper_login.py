import requests, sys, time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
#page = driver.get('https://www.youtube.com/playlist?list=PLU_L-hA1sDm_VE7Z8yDA9eG6Jrq3rm9ec')
#track_list = driver.find_elements_by_id('video-title')
driver.get('https://www.codewars.com/users/sign_in')
user = driver.find_element_by_id('user_email')
user.clear()#to clear the stuff already present in the fields
user.send_keys('particleofmass@gmail.com')
password = driver.find_element_by_id('user_password')
password.clear()
password.send_keys('Cp@7184090841')
login = driver.find_element_by_xpath('/html/body/div[1]/div[1]/main/div[2]/form/button')
login.click()
time.sleep(9)
