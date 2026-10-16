from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
import matplotlib.pyplot as plt
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import os

driver = webdriver.Chrome
driver.get('https://pass.rw.by/ru/route/?from=%D0%9C%D0%B8%D0%BD%D1%81%D0%BA-%D0%9F%D0%B0%D1%81%D1%81%D0%B0%D0%B6%D0%B8%D1%80%D1%81%D0%BA%D0%B8%D0%B9&from_exp=2100001&from_esr=&to=%D0%91%D0%BE%D1%80%D0%B8%D1%81%D0%BE%D0%B2&to_exp=2100305&to_esr=141406&front_date=%D1%81%D0%B5%D0%B3%D0%BE%D0%B4%D0%BD%D1%8F&date=today')


def coockies():
    button = driver.find_element(By.XPATH, "//button[text()='Принять']")
    button.click()


def cliker():
    label = driver.find_element(By.XPATH, "//*[@data-filter-value='w_places']/ancestor::label")
    driver.execute_script("arguments[0].click();", label)

    checkbox = driver.find_element(By.XPATH, "//input[@name='form-CITY_LINES']")
    driver.execute_script("arguments[0].click();", checkbox)

coockies()
cliker()

input("Enter — закрыть")
driver.quit()