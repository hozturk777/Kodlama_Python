from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.action_chains import ActionChains
import pytest
from pathlib import Path
from datetime import date

class Test_demo:

    # her testten önce çağırılır
    def setup_method(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.maximize_window() 
        self.driver.get("https://www.saucedemo.com/")
        # günün tarihini al bu tarih ile bir klasör var mı kontrol et yoksa oluştur
        self.folderPath = str(date.today())
        Path(self.folderPath).mkdir(exist_ok=True)

    # her testten sonra çağırılır
    def teardown_method(self):
        self.driver.quit()

    #setup -> test_demo -> teardown 
    def test_demo(self):
        text = "hello"
        assert text == "hello"
    
    @pytest.mark.parametrize("username, password" , [("1", "2"), ("kullaniciadim", "sifrem")])
    def test_invalid_login(self, username, password):
        self.waitForElementVisible((By.NAME, "user-name"))
        usernameInput = self.driver.find_element(By.NAME, "user-name")
        self.waitForElementVisible((By.NAME, "password"), 10)
        passwordInput = self.driver.find_element(By.NAME, "password")

        usernameInput.send_keys(username)
        passwordInput.send_keys(password)

        self.waitForElementVisible(((By.NAME, "login-button")))
        loginBtn = self.driver.find_element(By.NAME,"login-button")
        loginBtn.click()

        errorMessage = self.driver.find_element(By.XPATH, "//*[@id='login_button_container']/div/form/div[3]")
        self.driver.save_screenshot(f"{self.folderPath}/test-invalid-login-{username}-{password}.png")
        assert errorMessage.text == "Epic sadface: Username and password do not match any user in this service"
        
    def waitForElementVisible(self, locator, timeout = 5):
        WebDriverWait(self.driver, timeout).until(ec.visibility_of_element_located(locator))