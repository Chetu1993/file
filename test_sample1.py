
import pytest
import time


from practice.pageObjects.firstpage import firstpage

@pytest.mark.usefixtures("drivers")
class Testfile:
    pass
class Test_first(Testfile):

    @pytest.mark.test1
    def test_func(self):
        self.driver.get("https://automationteststore.com")
        time.sleep(2)
        self.driver.maximize_window()
        first=firstpage(self.driver)
        second = first.button1()
        second.method_name().send_keys("chetan")
        second.method_password().send_keys("chetan456$")
        second.method_submit()
        third = second(self.driver)
        a = third.method_text().text
        print(a, "validation passed")
        third.b_button1()
        third.b_button2()
        third.b_button3()
        third.b_button4()
        b = self.third.t_text1()
        c = self.third.t_text2()
        assert b == c, 'both values are matching'


        # self.driver.find_element(By.LINK_TEXT,"Login or register").click()


        # second.method_name().send_keys("chetan")
        # second.method_password().send_keys("chetan456$")
        # second.method_submit()

        # self.driver.find_element(By.XPATH,"(//input[@type='text'])[2]").send_keys("chetan")
        # self.driver.find_element(By.XPATH,"//input[@name='password']").send_keys("chetan456$")

        # self.driver.find_element(By.XPATH,"(//button[@type='submit'])[2]").click()


    # def test_third(self):
    #     third=secondpage(self.driver)
    #     a = self.third.method_text().text
    #     # a=print(self.driver.find_element(By.XPATH,"//span[@class='subtext']").text)
    #     print(a,"validation passed")


    # def test_forth(self):
    #     self.third.b_button1()
    #     self.third.b_button2()
    #     self.third.b_button3()
    #     self.third.b_button4()
        # self.driver.find_element(By.XPATH,"(//li/a)[39]").click()
        # self.driver.find_element(By.XPATH,"(//a/img)[9]").click()

        # self.driver.find_element(By.XPATH,"//a[@class='cart']").click()
        # self.driver.find_element(By.XPATH,"//a[@id='cart_checkout1']").click()


    # def test_fifth(self):
    #     b=self.third.t_text1()
    #     c=self.third.t_text2()
        # b=print(self.driver.find_element(By.XPATH,"(//span[@class='cart_block_total'])[12]").text)
        # c=print(self.driver.find_element(By.XPATH,"//span[@class='bold totalamout']").text)
        # assert b==c,'both values are matching'

