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
import test_saucedemo
import openpyxl


URL = "https://www.saucedemo.com/"



def waitForUser_Name(driver, timeout = 5):
        WebDriverWait(driver, timeout).until(ec.visibility_of_element_located((By.NAME, "user-name")))
def waitForPassword(driver,timeout = 5):
        WebDriverWait(driver, timeout).until(ec.visibility_of_element_located((By.ID, "password")))
def waitForLogin_Button(driver,timeout = 5):
        WebDriverWait(driver, timeout).until(ec.visibility_of_element_located((By.ID, "login-button")))
def waitForError_Button(driver,timeout = 5):
        WebDriverWait(driver, timeout).until(ec.visibility_of_element_located((By.CLASS_NAME, "error-button")))
def waitForInventory_Item(driver,timeout = 5):
        WebDriverWait(driver, timeout).until(ec.visibility_of_element_located((By.CLASS_NAME, "inventory_item")))
def waitForBackPack_AddtoCart(driver,timeout = 5):
        WebDriverWait(driver, timeout).until(ec.visibility_of_element_located((By.NAME, "add-to-cart-sauce-labs-backpack")))
def waitForShoppingCart(driver,timeout = 5):
        WebDriverWait(driver, timeout).until(ec.visibility_of_element_located((By.ID, "shopping_cart_container")))
def waitForRemoveBackPack_ShoppingCart(driver,timeout = 5):
        WebDriverWait(driver, timeout).until(ec.visibility_of_element_located((By.ID, "remove-sauce-labs-backpack")))
def waitForMenu_Button(driver,timeout = 5):
        WebDriverWait(driver, timeout).until(ec.visibility_of_element_located((By.ID, "react-burger-menu-btn")))
def waitForAll_Items_Button(driver,timeout = 5):
        WebDriverWait(driver, timeout).until(ec.visibility_of_element_located((By.ID, "inventory_sidebar_link")))
def waitForSelect_Container(driver,timeout = 5):
        WebDriverWait(driver, timeout).until(ec.visibility_of_element_located((By.CLASS_NAME, "select_container")))
def waitForLogOut_Button(driver,timeout = 5):
        WebDriverWait(driver, timeout).until(ec.visibility_of_element_located((By.ID, "logout_sidebar_link")))



