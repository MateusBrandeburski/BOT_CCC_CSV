from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

browser = webdriver.Chrome()

browser.get('https://www.hashtagtreinamentos.com/blog')

link = "contato@hashtagtreinamentos.com"

browser.find_element(By.LINK_TEXT, link).click()

sleep(3)