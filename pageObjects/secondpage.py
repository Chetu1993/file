
from selenium.webdriver.common.by import By
from practice.pageObjects.thirdpage import thirdpage


class secondpage:
    def __init__(self,driver):
        self.driver=driver

    name=(By.XPATH, "(//input[@type='text'])[2]")
    password=(By.XPATH, "//input[@name='password']")
    submit=(By.XPATH, "(//button[@type='submit'])[2]")
    text=(By.XPATH, "//span[@class='subtext']")

    def method_name(self):
        return self.driver.findelement(secondpage.name)
    def method_password(self):
        return self.driver.findelement(secondpage.password)
    def method_submit(self):
        self.driver.findelement(secondpage.submit).click()
    def method_text(self):
        self.driver.findelement(secondpage.text)
        third=thirdpage(self.driver)
        return third

   

