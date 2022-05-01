import time

import pytest
from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from PageObjects.Homepage import Homepage
from testData.HomePageData import HomePageData
from utilities.Baseclass import Baseclass


class TestHomePage(Baseclass):
    def test_formsubmission(self, getData):
        log=self.getLogger()
        # driver.find_element(By.NAME,"name").send_keys("vijaykumar")

        log.info("Firstname"+getData["firstname"])
        homepage = Homepage(self.driver)
        homepage.getName().send_Keys(getData["Firstname"])
        time.sleep(5)
        homepage.getEmail().click()
        time.sleep(5)

        # Select class provide the methods to handle the options in dropdowns

        # dropdown = Select(self.driver.find_element(By.ID, "exampleFormControlSelect1"))
        # dropdown.select_by_visible_text("Female")
        # dropdown.select_by_index(0)
        self.selectOptionByText(homepage.getGender(), getData[1])

        # self.driver.find_element(By.XPATH, "//input[@type='submit']").click()
        time.sleep(4)
        homepage.submitForm().click()

        # print(driver.find_element(By.CSS_SELECTOR, "div[class*='alert-success']").text)
        # message = self.driver.find_element(By.CLASS_NAME, "alert-success").text
        alerttext = homepage.alertSuccess().text
        # print(message)
        # //*[contains(@class,'alert-success')]
        assert "success" in alerttext
        time.sleep(5)
        self.driver.refresh()

    @pytest.fixture(params=HomePageData.getTestData("Testcase2"))
    def getData(self, request):
        return request.param
