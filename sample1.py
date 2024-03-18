
import pytest
from selenium import webdriver
from selenium.webdriver.edge.service import Service
import time
from selenium.webdriver.common.by import By
service_obj=Service("C:\\Users\\cks_1\\PycharmProjects\\project1\\practice\\edgedriver_win64 (3)\\msedgedriver.exe")
driver=webdriver.Edge(service=service_obj)

@pytest.mark.test1
def test_func():
    driver.get("https://automationteststore.com")
    time.sleep(2)
    driver.maximize_window()
    time.sleep(3)
    driver.find_element(By.LINK_TEXT,"Login or register").click()

def test_second():
    driver.find_element(By.XPATH,"(//input[@type='text'])[2]").send_keys("chetan")
    driver.find_element(By.XPATH,"//input[@name='password']").send_keys("chetan456$")
    driver.find_element(By.XPATH,"(//button[@type='submit'])[2]").click()

def test_third():
    a=print(driver.find_element(By.XPATH,"//span[@class='subtext']").text)
    print(a,"validation passed")

def test_fourth():
    driver.find_element(By.XPATH,"(//li/a)[39]").click()
    driver.find_element(By.XPATH,"(//a/img)[9]").click()
    driver.find_element(By.XPATH,"//a[@class='cart']").click()
    driver.find_element(By.XPATH,"//a[@id='cart_checkout1']").click()

def test_fifth():
    b=print(driver.find_element(By.XPATH,"(//span[@class='cart_block_total'])[12]").text)
    c=print(driver.find_element(By.XPATH,"//span[@class='bold totalamout']").text)
    assert b==c,'both values are matching'

