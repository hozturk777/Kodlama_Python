from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep


class Test_Kodlamaio:
    def test_invalid_login(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window() 
        driver.get("https://www.saucedemo.com/")
        
        sleep(1)
        usernameInput = driver.find_element(By.NAME, "user-name")
        usernameInput.send_keys("DİLBER")

        sleep(1)
        passwordInput = driver.find_element(By.NAME, "password")
        passwordInput.send_keys("dilber")

        sleep(1)
        loginBtn = driver.find_element(By.NAME,"login-button")
        sleep(1)
        loginBtn.click()

        errorMessage = driver.find_element(By.XPATH, "//*[@id='login_button_container']/div/form/div[3]")
        testResult = errorMessage.text == "Epic sadface: Username and password do not match any user in this service"
        if testResult == True:
            print("doğru output")
        else:
            print("yanlış output")

        
       
        


testClass = Test_Kodlamaio()
testClass.test_invalid_login()


