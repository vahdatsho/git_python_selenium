from selenium.webdriver.common.by import By

from utilities.BaseClass import BaseClass


class HomePage:
    def __init__(self, driver):
        self.driver = driver

    shop = (By.CSS_SELECTOR, "a[href*='shop']")
    name = (By.CSS_SELECTOR, "[name='name']")
    email = (By.NAME, "email")
    checkbox = (By.ID, "exampleCheck1")
    gender = (By.ID, "exampleFormControlSelect1")
    submit = (By.XPATH, "//input[@value='Submit']")
    success = (By.CSS_SELECTOR, "[class*='alert-success']")
    new_shop = (By.CSS_SELECTOR, "a[href*='shop']")
    new_name = (By.CSS_SELECTOR, "[name='name']")
    new_email = (By.NAME, "email")

    def shopitems(self):
        return self.driver.find_element(*HomePage.shop)


    def get_name(self):

        return self.driver.find_element(*HomePage.name)

    def get_email(self):

        return self.driver.find_element(*HomePage.email)

    def get_check_box(self):

        return self.driver.find_element(*HomePage.checkbox)

    def get_gender(self):

        return self.driver.find_element(*HomePage.gender)

    def submit_form(self):

        return self.driver.find_element(*HomePage.submit)

    def get_success_message(self):

        return self.driver.find_element(*HomePage.success)

    def new_shopitems(self):
        return self.driver.find_element(NewHomePage.shop)


    def new_get_name(self):

        return self.driver.find_element(NewHomePage.name)

    def new_get_email(self):

        return self.driver.find_element(NewHomePage.email)

    def new_get_check_box(self):

        return self.driver.find_element(NewHomePage.checkbox)
