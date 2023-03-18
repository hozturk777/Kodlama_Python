from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
driver.get("https://www.google.com")

input = driver.find_element(By.NAME,"q")
input.send_keys("kodlamaio")

sleep(1)
searchButton = driver.find_element(By.NAME, "btnK")
sleep(2)
searchButton.click()

sleep(2)
kodlamaİo = driver.find_element(By.XPATH, "//*[@id='rso']/div[1]/div/div/div/div/div/div/div/div[1]/a")
sleep(1)
kodlamaİo.click()

courseCount = driver.find_elements(By.CLASS_NAME, "course-listing")
print(f"kodlamaio sitesi kurs sayısı : {len(courseCount)}")

while True:
    continue


#web scraping
#data scraping