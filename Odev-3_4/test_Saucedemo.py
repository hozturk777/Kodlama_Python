from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep

class SauceDemo:
    def __init__(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.maximize_window()
        self.driver.get("https://www.saucedemo.com/")
              
    
    def task1(self):     #Kullanıcı adı ve şifre alanları boş geçildiğinde uyarı mesajı olarak "Epic sadface: Username is required" gösterilmelidir.
        loginBtn = self.driver.find_element(By.ID, "login-button")
        sleep(1)
        loginBtn.click()

        errorMessage = self.driver.find_element(By.XPATH, "//*[@id='login_button_container']/div/form/div[3]/h3")
        print(errorMessage.text)

        while True:
            continue   
    
    def task2(self):    #Sadece şifre alanı boş geçildiğinde uyarı mesajı olarak "Epic sadface: Password is required" gösterilmelidir.
        usernameInput = self.driver.find_element(By.ID, "user-name")
        usernameInput.send_keys("name")

        loginBtn = self.driver.find_element(By.ID, "login-button")
        sleep(1)
        loginBtn.click()

        errorMessage = self.driver.find_element(By.XPATH, "//*[@id='login_button_container']/div/form/div[3]/h3")
        print(errorMessage.text)

        while True:
            continue

    def task3(self):    #Kullanıcı adı "locked_out_user" şifre alanı "secret_sauce" gönderildiğinde "Epic sadface: Sorry, this user has been locked out." mesajı gösterilmelidir.
        usernameInput = self.driver.find_element(By.ID, "user-name")
        usernameInput.send_keys("locked_out_user")

        passwordInput = self.driver.find_element(By.ID, "password")
        passwordInput.send_keys("secret_sauce")

        loginBtn = self.driver.find_element(By.ID, "login-button")
        sleep(1)
        loginBtn.click()

        errorMessage= self.driver.find_element(By.XPATH,  "//*[@id='login_button_container']/div/form/div[3]/h3")
        print(errorMessage.text)

        while True:
            continue

    def task4(self):    #Kullanıcı adı ve şifre alanları boş geçildiğinde bu iki inputun yanında da kırmızı "X" ikonu çıkmalıdır. Daha sonra aşağıda çıkan uyarı mesajının kapatma  butonuna tıklandığında bu "X" ikonları kaybolmalıdır.
        loginBtn = self.driver.find_element(By.ID, "login-button")
        sleep(1)
        loginBtn.click()

        errorBtn = self.driver.find_element(By.XPATH, "//*[@id='login_button_container']/div/form/div[3]/h3/button")
        sleep(1)
        errorBtn.click()

        while True:
            continue

    def task5(self):    #Kullanıcı adı "standard_user" şifre "secret_sauce" gönderildiğinde kullanıcı "/inventory.html" sayfasına gönderilmelidir.
        usernameInput = self.driver.find_element(By.ID, "user-name")
        usernameInput.send_keys("standard_user")

        passwordInput = self.driver.find_element(By.ID, "password")
        passwordInput.send_keys("secret_sauce")

        loginBtn = self.driver.find_element(By.ID, "login-button")
        sleep(1)
        loginBtn.click()

        while True:
            continue

    def task6(self):    #Giriş yapıldıktan sonra kullanıcıya gösterilen ürün sayısı "6" adet olmalıdır.
        usernameInput = self.driver.find_element(By.ID, "user-name")
        usernameInput.send_keys("standard_user")

        passwordInput = self.driver.find_element(By.ID, "password")
        passwordInput.send_keys("secret_sauce")

        loginBtn = self.driver.find_element(By.ID, "login-button")
        sleep(1)
        loginBtn.click()

        sleep(1)
        entityCount = self.driver.find_elements(By.CLASS_NAME, "inventory_item")
        print(f"Ürün Sayısı: {len(entityCount)}")


        while True:
            continue        

saucedemo = SauceDemo()
saucedemo.task6()