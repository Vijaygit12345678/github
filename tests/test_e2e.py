import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from PageObjects.Checkoutpage import checkoutPage
from PageObjects.Homepage import Homepage
from utilities.Baseclass import Baseclass

#@pytest.mark.usefixtures()


class TestOne(Baseclass):

    def test_e2e(self):
        log=self.getLogger()
        homepage = Homepage(self.driver)
        checkoutPage1 = Homepage.shopItems()
        #self.driver.find_elements(By.CSS_SELECTOR, ".card-title a")
        time.sleep(3)
        #cards = self.driver.find_elements(By.CSS_SELECTOR,".card-footer button")
        #checkOut = checkoutPage(self.driver)
        cards = checkoutpage1.getCardTitle()
        i=-1
        for card in cards:
            i = i + 1
            cardText= card.text
            print(cardText)
            if cardText == "Blackberry":
                checkoutPage.getCardfooter()[i].click()

        self.driver.find_element(By.CSS_SELECTOR, "a[class*='nav-link btn btn-primary']").click()
        confirmpage=checkoutPage1.checkOutItems
        #self.driver.find_element(By.XPATH,"//button[@class='btn btn-success']").click()
        log.info("Enter the country name as ind")
        self.driver.find_element(By.ID,"country").send_keys("ind")

        self.verifyLinkPresence("India")
        self.driver.find_element(By.LINK_TEXT,"India").click()
        self.driver.find_element(By.XPATH,"//div[@class='checkbox checkbox-primary']").click()
        self.driver.find_element(By.CSS_SELECTOR,"[type='submit']").click()
        Textmatch=self.driver.find_element(By.CSS_SELECTOR,"[class*='alert alert-success alert-dismissible']").text
        log.info("Text received from application is "+Textmatch)

        assert "Success!" in Textmatch







