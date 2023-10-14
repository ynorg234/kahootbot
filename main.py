# Kahoot Botter V0.2
from selenium_driver_updater import DriverUpdater
from selenium.webdriver.common.by import By
from selenium import webdriver
from time import sleep
import os
# testing first version that uses working selenium
bd = os.path.dirname(os.path.abspath(__file__))
fn = DriverUpdater.install(path=bd, driver_name=DriverUpdater.chromedriver, upgrade=True, check_driver_is_up_to_date=True)
driver = webdriver.Chrome(fn)
id = input("Enter kahoot id...")
bots = input("Enter number of bots... ")
botname = input("Enter Bot name here...")
kahootlink = f"https://kahoot.it/?pin={id}&refer_method=link"
driver.get(kahootlink)
i = 0
while True:
    sleep(2.5)
    input = driver.find_element(By.XPATH, "/html/body/div/div[1]/div/div/div/div/div[2]/main/div/form/input")
    input.send_keys(f"{botname}[{str(i)}]")
    btn = driver.find_element(By.XPATH, '/html/body/div/div[1]/div/div/div/div/div[2]/main/div/form/button')
    btn.click()
    sleep(1.5)
    i += 1
    driver.execute_script("window.open('')")
    driver.switch_to.window(driver.window_handles[i])
    driver.get(kahootlink)
    if i == int(bots):
        driver.execute_script("window.open('about:blank')")
        break
    
