from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.action_chains import ActionChains

class Test_Kodlamaio:
    def initializeDriver(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window() 
        driver.get("https://www.saucedemo.com/")
        return driver

    def test_invalid_login(self):
        driver = self.initializeDriver()
        
        WebDriverWait(driver, 5).until(ec.visibility_of_element_located((By.NAME, "user-name")))
        usernameInput = driver.find_element(By.NAME, "user-name")
        usernameInput.send_keys("DİLBER")

        WebDriverWait(driver, 5).until(ec.visibility_of_element_located((By.NAME, "password")))
        passwordInput = driver.find_element(By.NAME, "password")
        passwordInput.send_keys("dilber")

        WebDriverWait(driver, 5).until(ec.visibility_of_element_located((By.NAME, "login-button")))
        loginBtn = driver.find_element(By.NAME,"login-button")
        loginBtn.click()

        errorMessage = driver.find_element(By.XPATH, "//*[@id='login_button_container']/div/form/div[3]")
        testResult = errorMessage.text == "Epic sadface: Username and password do not match any user in this service"
        if testResult == True:
            print("doğru output")
        else:
            print("yanlış output")

        

    def test_valid_input(self):
        driver = self.initializeDriver()

        WebDriverWait(driver, 5).until(ec.visibility_of_element_located((By.ID, "user-name")))
        usernameInput = driver.find_element(By.NAME, "user-name")
        WebDriverWait(driver, 5).until(ec.visibility_of_element_located((By.ID, "password")))
        passwordInput = driver.find_element(By.NAME, "password")

        # Action Chains 
        actions = ActionChains(driver)
        actions.send_keys_to_element(usernameInput, "standard_user")
        actions.send_keys_to_element(passwordInput, "secret_sauce")
        actions.perform()

        #usernameInput.send_keys("standard_user")
        #passwordInput.send_keys("secret_sauce")
        WebDriverWait(driver, 5).until(ec.visibility_of_element_located((By.NAME, "login-button")))
        loginBtn = driver.find_element(By.NAME,"login-button")
        loginBtn.click()

        #js execute
        driver.execute_script("window.scrollTo(0,500)")
        


        
       
        


testClass = Test_Kodlamaio()
testClass.test_invalid_login()
testClass.test_valid_input()


