from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome()

browser.get('http://ya.ru')
assert 'Яндекс' in browser.title

elem = browser.find_element_by_class_name('input__control')
elem.send_keys('Ozone'+Keys.RETURN)

