from selenium import webdriver
from selenium.webdriver.edge.service import Service
# from selenium.webdriver.firefox.service import Service


import pytest

@pytest.fixture(params=['edge','firefox'],scope="class")

def drivers(request):

    if request.param=="edge":
        service_obj=Service("C:\\Users\\cks_1\\Downloads\\edgedriver_win64\\msedgedriver.exe")
        driver=webdriver.Edge(service=service_obj)
        request.cls.driver=driver
        yield
        driver.close()

    if request.param=="firefox":
        service_obj=Service("C:\\Users\\cks_1\\Downloads\\geckodriver-v0.34.0-win64\\geckodriver.exe")
        driver=webdriver.Firefox(service=service_obj)
        request.cls.driver=driver
        yield
        driver.close()




