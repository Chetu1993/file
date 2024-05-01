
from selenium.webdriver.common.by import By


class thirdpage:
    def __init__(self,driver):
        self.driver=driver

    button1=(By.XPATH, "(//li/a)[39]")
    button2=(By.XPATH, "(//a/img)[9]")
    button3=(By.XPATH, "//a[@class='cart']")
    button4=(By.XPATH, "//a[@id='cart_checkout1']")
    text1=(By.XPATH,"(//span[@class='cart_block_total'])[12]")
    text2=(By.XPATH,"//span[@class='bold totalamout']")

    def b_button1(self):
        self.driver.find_element(thirdpage.button1).click()
    def b_button2(self):
        self.driver.find_element(thirdpage.button2).click()
    def b_button3(self):
        self.driver.find_element(thirdpage.button3).click()
    def b_button4(self):
        self.driver.find_element(thirdpage.button4).click()
    def t_text1(self):
        return self.driver.find_element(thirdpage.text1)
    def t_text2(self):
        return self.driver.find_element(thirdpage.text2)

