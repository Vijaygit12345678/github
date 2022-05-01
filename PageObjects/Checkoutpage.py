from selenium.webdriver.common.by import By

from PageObjects.ConfirmPage import ConfirmPage


class checkoutPage():

    def __init__(self, driver):
        self.driver = driver

    # self.driver.find_elements(By.CSS_SELECTOR,".card-title a")
    cardTitle = (By.CSS_SELECTOR, ".card-title a")
    cardFooter = (By.CSS_SELECTOR, ".card-footer button")
    checkOutItems = (By.XPATH, "//button[@class='btn btn-success']")

    def getCardTitles(self):
        return self.driver.find_elements(*checkoutPage.cardTitle)

    def getcardfooter(self):
        return self.driver.find_elements(*checkoutPage.cardFooter)

    def checkOutItems(self):
        self.driver.find_element(*checkoutPage.checkOutItems).click()
        confirmpage = ConfirmPage(self.driver)
        return confirmpage
