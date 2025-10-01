from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from datetime import datetime


trip_date = datetime(2025, 10, 17)   
group_name = '"Friends"'        
update_time = "00:01"  

options = webdriver.ChromeOptions()
options.add_argument("--user-data-dir=chrome-data")  
driver = webdriver.Chrome(options=options)

driver.get("https://web.whatsapp.com/")
wait = WebDriverWait(driver, 100)

time.sleep(5)  

def update_group():

    today = datetime.now()
    days_left = (trip_date - today).days
    new_name = f"Friends - {days_left} Days Left!!"
    message = f"Helloo Bastards! {days_left} more days to gooooo!!"


    contact_path = f'//span[contains(@title, {group_name})]'

    contact = wait.until(EC.element_to_be_clickable((By.XPATH, contact_path)))
    contact.click()
        
    header = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="main"]/header/div[2]/div[1]/div/span')))
    header.click()
    time.sleep(2)

    subject_box = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div[1]/div[3]/div/div[5]/span/div/span/div/div/div/section/div[1]/div/div[2]/div/div/div[3]/span[2]/button/span')))
    subject_box.click()
    time.sleep(1)



    input_box = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div[1]/div[3]/div/div[5]/span/div/span/div/div/div/section/div[1]/div/div[2]/div/div[1]/div[1]/div/div/p')))
    input_box.send_keys(Keys.COMMAND,"a")  
    time.sleep(2)
    input_box.send_keys(Keys.DELETE)   
    time.sleep(2)      
    input_box.send_keys(new_name)
    input_box.send_keys(Keys.ENTER)
    print(f"Group name updated to: {new_name}")

    wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div[1]/div[3]/div/div[5]/span/div/span/div/div/header/div/div[1]/div/span/div/div/div[1]/div[1]/span'))).click()
    time.sleep(2)

    msg_box = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="main"]/footer/div[1]/div/span/div/div[2]/div/div[3]/div[1]/p')))
    msg_box.click()
    msg_box.send_keys(message)
    msg_box.send_keys(Keys.ENTER)
    print(f"Sent message: {message}")

while datetime.now().date() < trip_date.date():
    current_time = datetime.now().strftime("%H:%M")
    if current_time == update_time:
        update_group()
        time.sleep(60)  # Wait a minute to avoid running multiple times
    time.sleep(30)  # Check every 30 seconds

while True:
    pass

