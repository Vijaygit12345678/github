from selenium.webdriver.common.by import By

from PageObjects import Checkoutpage


class Homepage:

    def __init__(self, driver):
        self.driver = driver

    shop = (By.CSS_SELECTOR, "a[href*='shop']")
    name = (By.CSS_SELECTOR, "input[name='name']")
    Email = (By.ID, "exampleCheck1")
    gender = (By.ID, "exampleFormControlSelect1")
    submitbutton =(By.XPATH, "//input[@type='submit']")
    alert=(By.CLASS_NAME, "alert-success")

    def shopItems(self):
        self.driver.find_element(*Homepage.shop).click()
        checkoutpage1 = Checkoutpage(self.driver)
        return checkoutpage1
    # self.driver.find_element(By.CSS_SELECTOR,"a[href*='shop']")

    def getName(self):
        return self.driver.find_element(*Homepage.name)

    def getEmail(self):
        return self.driver.find_element(*Homepage.Email)

    def getGender(self):
        return self.driver.find_element(*Homepage.gender)

    def submitForm(self):
        return self.driver.find_element(*Homepage.submitbutton)

    def alertSuccess(self):
        return self.driver.find_element(*Homepage.alert)

