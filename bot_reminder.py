from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from datetime import datetime
import random


trip_date = datetime(2025, 10, 17)   
group_name = '"Friends"'        
update_time = "00:04"  

messages = {
    15: [
        "15 days, pack your craze, adventure’s on the way!",
        "15 nights, future delights, memes and snacks in sight!"
    ],
    14: [
        "14 to cheer, the trip is near, start practicing your weird dance gear!",
        "14 more, fun at the core, prank wars knocking at the door!"
    ],
    13: [
        "13 nights, dreamy sights, selfies, giggles, late-night fights!",
        "13 days, in so many ways, countdown memes to fill our craze!"
    ],
    12: [
        "12 to go, vibes will flow, can’t wait to see who cries first though!",
        "12 more nights, epic delights, pizza, jokes, and starry nights!"
    ],
    11: [
        "11 to heaven, joy level 7, may the funniest one win the leaven!",
        "11 more days, let’s set the blaze, silly selfies and crazy plays!"
    ],
    10: [
        "10 to begin, let the fun spin, get ready to lose in a pillow bin!",
        "10 more, joy will soar, laugh so hard your cheeks get sore!"
    ],
    9: [
        "9 to shine, it’s gonna be divine, snack fights and terrible wine!",
        "9 more sleeps, excitement peaks, midnight pranks and pillow squeaks!"
    ],
    8: [
        "8 is great, we just can’t wait, who snores first seals their fate!",
        "8 to go, happiness will grow, selfies, memes, and a water-throw!"
    ],
    7: [
        "Lucky 7, feels like heaven, dancing in weird socks we’ve chosen!",
        "7 to show, the thrill will glow, prank battles and epic slow-mo!"
    ],
    6: [
        "6 to fix, memories to mix, can’t wait to see who loses their kicks!",
        "6 more nights, endless delights, group selfies and funny fights!"
    ],
    5: [
        "High five, only 5 till we arrive, may the snacks survive the dive!",
        "5 more days, joy always stays, laughter, chaos, and sunny rays!"
    ],
    4: [
        "Just 4 more, fun at the door, prank wars knocking hardcore!",
        "4 days in line, the trip will shine, pizza, memes, and plenty of wine!"
    ],
    3: [
        "3 days away, we’re ready to slay, games and giggles all the way!",
        "Only 3 more nights, then we take flight, selfie sticks and silly fights!"
    ],
    2: [
        "2 days to go, the excitement will show, who will snore first? Nobody knows!",
        "Double the fun, only 2 days and we run, laughing, dancing, under the sun!"
    ],
    1: [
        "Only 1 day, hooray hooray! Pack your jokes, it’s time to play!",
        "Just 1 more sleep, thrill runs deep, get ready for memories we’ll keep!"
    ]
}


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

    if days_left in messages:
        message = random.choice(messages[days_left])
    else:
        message = f"Only {days_left} days left! Trip vibes loading"


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
        time.sleep(60)  
    time.sleep(30)  

while True:
    pass

