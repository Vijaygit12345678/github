import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )


@pytest.fixture(scope="class")
def setup(request):
    browser = request.config.getoption("browser_name")

    if browser == "chrome":
        driver = webdriver.Chrome(executable_path="C:\chromedriver_win32\chromedriver.exe")
    elif browser == "firefox":
        driver = webdriver.Firefox(executable_path="C:geckodriver.exe")
    elif browser == "IE":
        print('IE')

    driver.get("https://rahulshettyacademy.com/angularpractice/")
    driver.maximize_window()
    driver.implicit_

    request.cls.driver = driver
    yield
    driver.close()
