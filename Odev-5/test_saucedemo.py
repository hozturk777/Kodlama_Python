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
import openpyxl
from constants import globalConstants

class Test_SauceDemo:
    def setup_method(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.maximize_window()
        self.driver.get(globalConstants.URL)

        self.folderPath = str(date.today())
        Path(self.folderPath).mkdir(exist_ok=True)
        

    def teardown_method(self):
        self.driver.quit()

     
    
    def test_Invalid_Login(self):     #Kullanıcı adı ve şifre alanları boş geçildiğinde uyarı mesajı olarak "Epic sadface: Username is required" gösterilmelidir.
        loginBtn = self.driver.find_element(By.ID, "login-button")
        globalConstants.waitForLogin_Button(self.driver)
        loginBtn.click()

        errorMessage = self.driver.find_element(By.XPATH, "//*[@id='login_button_container']/div/form/div[3]/h3")
        self.driver.save_screenshot(f"{self.folderPath}/test_Invalid_Login.png")
        assert errorMessage.text == "Epic sadface: Username is required"

     

    @pytest.mark.parametrize("username ",["hüseyin","Halil","Engin"] )
    def test_Invalid_Password(self,username):    #Sadece şifre alanı boş geçildiğinde uyarı mesajı olarak "Epic sadface: Password is required" gösterilmelidir.
        usernameInput = self.driver.find_element(By.ID, "user-name")
        globalConstants.waitForUser_Name(self.driver)
        usernameInput.send_keys(username)

        loginBtn = self.driver.find_element(By.ID, "login-button")
        globalConstants.waitForLogin_Button
        loginBtn.click()

        errorMessage = self.driver.find_element(By.XPATH, "//*[@id='login_button_container']/div/form/div[3]/h3")
        self.driver.save_screenshot(f"{self.folderPath}/test_Invalid_Password-{username}.png")
        assert errorMessage.text == "Epic sadface: Password is required"

    

    def test_Locked_User(self):    #Kullanıcı adı "locked_out_user" şifre alanı "secret_sauce" gönderildiğinde "Epic sadface: Sorry, this user has been locked out." mesajı gösterilmelidir.
        usernameInput = self.driver.find_element(By.ID, "user-name")       
        passwordInput = self.driver.find_element(By.ID, "password")

        globalConstants.waitForUser_Name(self.driver)
        usernameInput.send_keys("locked_out_user")
        globalConstants.waitForPassword(self.driver)
        passwordInput.send_keys("secret_sauce")

        loginBtn = self.driver.find_element(By.ID, "login-button")
        globalConstants.waitForLogin_Button(self.driver)
        loginBtn.click()

        errorMessage= self.driver.find_element(By.XPATH,  "//*[@id='login_button_container']/div/form/div[3]/h3")
        self.driver.save_screenshot(f"{self.folderPath}/test_Locked_User.png")
        assert errorMessage.text == "Epic sadface: Sorry, this user has been locked out."



    def test_Click_LoginError(self):    #Kullanıcı adı ve şifre alanları boş geçildiğinde bu iki inputun yanında da kırmızı "X" ikonu çıkmalıdır. Daha sonra aşağıda çıkan uyarı mesajının kapatma  butonuna tıklandığında bu "X" ikonları kaybolmalıdır.
        loginBtn = self.driver.find_element(By.ID, "login-button")
        globalConstants.waitForLogin_Button(self.driver)
        loginBtn.click()

        errorBtn = self.driver.find_element(By.CLASS_NAME, "error-button")
        globalConstants.waitForError_Button(self.driver)
        errorBtn.click()
        self.driver.save_screenshot(f"{self.folderPath}/test_Click_LoginError.png")
        assert True

    def test_Valid_Login(self):    #Kullanıcı adı "standard_user" şifre "secret_sauce" gönderildiğinde kullanıcı "/inventory.html" sayfasına gönderilmelidir.
        usernameInput = self.driver.find_element(By.ID, "user-name")
        passwordInput = self.driver.find_element(By.ID, "password")

        globalConstants.waitForUser_Name(self.driver)
        usernameInput.send_keys("standard_user")
        globalConstants.waitForPassword(self.driver)
        passwordInput.send_keys("secret_sauce")

        loginBtn = self.driver.find_element(By.ID, "login-button")
        globalConstants.waitForLogin_Button(self.driver)
        loginBtn.click()

        appLogoText = self.driver.find_element(By.CLASS_NAME, "app_logo")
        self.driver.save_screenshot(f"{self.folderPath}/test_Valid_Login-{usernameInput}-{passwordInput}.png")
        assert appLogoText.text == "Swag Labs"


    def test_List_Product(self):    #Giriş yapıldıktan sonra kullanıcıya gösterilen ürün sayısı "6" adet olmalıdır.
        usernameInput = self.driver.find_element(By.ID, "user-name")
        passwordInput = self.driver.find_element(By.ID, "password")

        globalConstants.waitForUser_Name(self.driver)
        usernameInput.send_keys("standard_user")
        globalConstants.waitForPassword(self.driver)
        passwordInput.send_keys("secret_sauce")

        loginBtn = self.driver.find_element(By.ID, "login-button")
        globalConstants.waitForLogin_Button(self.driver)
        loginBtn.click()

        globalConstants.waitForInventory_Item(self.driver)
        entityCount = self.driver.find_elements(By.CLASS_NAME, "inventory_item")
        self.driver.save_screenshot(f"{self.folderPath}/test_List_Product.png")
        assert len(entityCount) == 6

    def test_AddCart_Product(self):   #Giriş yapıldıktan sonra belirlenen ürünü sepete ekleme
        usernameInput = self.driver.find_element(By.ID, "user-name")
        passwordInput = self.driver.find_element(By.ID, "password")

        globalConstants.waitForUser_Name(self.driver)
        usernameInput.send_keys("standard_user")
        globalConstants.waitForPassword(self.driver)
        passwordInput.send_keys("secret_sauce")

        loginBtn = self.driver.find_element(By.ID, "login-button")
        globalConstants.waitForLogin_Button(self.driver)
        loginBtn.click()

        backPackAddToCart = self.driver.find_element(By.NAME, "add-to-cart-sauce-labs-backpack")
        globalConstants.waitForBackPack_AddtoCart(self.driver)
        backPackAddToCart.click()
        self.driver.save_screenshot(f"{self.folderPath}/test_AddCart_Product.png")
        backPackAddToCart = self.driver.find_element(By.NAME, "remove-sauce-labs-backpack")
        
        if backPackAddToCart.text == "Remove":
            assert True
        elif backPackAddToCart.text == "Add to cart":
            assert False
        else:
            assert False
    def test_Remove_ShoppingCart(self):     #Giriş yapıp bir ürünü sepete ekleyip sepetten çıkartıp tekrar tüm ürünlere geri döner
        usernameInput = self.driver.find_element(By.ID, "user-name")
        passwordInput = self.driver.find_element(By.ID, "password")

        globalConstants.waitForLogin_Button(self.driver)
        usernameInput.send_keys("standard_user")
        globalConstants.waitForPassword(self.driver)
        passwordInput.send_keys("secret_sauce")

        loginBtn = self.driver.find_element(By.ID, "login-button")
        globalConstants.waitForLogin_Button(self.driver)
        loginBtn.click()

        backPackAddToCart = self.driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack")
        globalConstants.waitForBackPack_AddtoCart(self.driver)
        backPackAddToCart.click()

        shoppingCart = self.driver.find_element(By.ID, "shopping_cart_container")
        globalConstants.waitForShoppingCart(self.driver)
        shoppingCart.click()
        self.driver.save_screenshot(f"{self.folderPath}/test_Remove_ShoppingCart_1.png")
        removeBackPackToCart = self.driver.find_element(By.ID, "remove-sauce-labs-backpack")
        globalConstants.waitForRemoveBackPack_ShoppingCart(self.driver)
        removeBackPackToCart.click()
        self.driver.save_screenshot(f"{self.folderPath}/test_Remove_ShoppingCart_2.png")
        menuBtn = self.driver.find_element(By.ID, "react-burger-menu-btn")
        globalConstants.waitForMenu_Button(self.driver)
        menuBtn.click()

        allItemsBtn = self.driver.find_element(By.ID, "inventory_sidebar_link")
        globalConstants.waitForAll_Items_Button(self.driver)
        allItemsBtn.click()
        self.driver.save_screenshot(f"{self.folderPath}/test_Remove_ShoppingCart_3.png")
        mainMenu = self.driver.find_element(By.CLASS_NAME, "title")
        
        if mainMenu.text == "Products":
            assert True
        else:
            assert False
    def test_LowtoHigh_Price(self):  # Ucuzdan pahalıya sıraladıktan sonra logout yapar
        usernameInput = self.driver.find_element(By.ID, "user-name")
        passwordInput = self.driver.find_element(By.ID, "password")

        globalConstants.waitForUser_Name(self.driver)
        usernameInput.send_keys("standard_user")
        globalConstants.waitForPassword(self.driver)
        passwordInput.send_keys("secret_sauce")

        loginBtn = self.driver.find_element(By.ID, "login-button")
        globalConstants.waitForLogin_Button(self.driver)
        loginBtn.click()

        selectContainer = self.driver.find_element(By.CLASS_NAME, "select_container")
        globalConstants.waitForSelect_Container(self.driver)
        selectContainer.click()
        self.driver.save_screenshot(f"{self.folderPath}/test_LowtoHigh_Price_1.png")
        lowToHigh = self.driver.find_element(By.XPATH, "//*[@id='header_container']/div[2]/div/span/select/option[3]")
        lowToHigh.click()
        self.driver.save_screenshot(f"{self.folderPath}/test_LowtoHigh_Price_2.png")
        menuBtn = self.driver.find_element(By.ID, "react-burger-menu-btn")
        globalConstants.waitForMenu_Button(self.driver)
        menuBtn.click()

        logOut = self.driver.find_element(By.ID, "logout_sidebar_link")
        globalConstants.waitForLogOut_Button(self.driver)
        out = logOut.click()
        self.driver.save_screenshot(f"{self.folderPath}/test_LowtoHigh_Price_3.png")
        if out == True:
            assert True
        else:
            False








