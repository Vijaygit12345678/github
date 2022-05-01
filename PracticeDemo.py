from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="C:\chromedriver_win32\chromedriver_win32\chromedriver.exe")
driver.get("http://demowebshop.tricentis.com/")
driver.find_element(By.LINK_TEXT,"Register").click()
driver.find_element(By.CSS_SELECTOR,"#gender-male").click()
driver.find_element(By.CSS_SELECTOR,"#FirstName").send_keys("Vijay")
driver.find_element(By.NAME,"LastName").send_keys("kumar")
driver.find_element(By.NAME,"Email").send_keys("Vak@gmail.com")
driver.find_element(By.NAME,"Password").send_keys("vijay123")
driver.find_element(By.NAME,"ConfirmPassword").send_keys("vijay123")
driver.find_element(By.CSS_SELECTOR,"input[type='submit']").click()

