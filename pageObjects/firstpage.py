


from selenium.webdriver.common.by import By

from practice.pageObjects.secondpage import secondpage

class firstpage:
    def __init__(self,driver):
        self.driver=driver

    button=(By.LINK_TEXT, "Login or register")

    def button1(self):
        self.driver.findelement(firstpage.button).click()
        second=secondpage(self.driver)
        return second



