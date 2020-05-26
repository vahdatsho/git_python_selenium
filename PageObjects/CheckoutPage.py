from selenium.webdriver.common.by import By


class CheckOutPage:

    def __init__(self, driver):
        self.driver = driver

    card_title = (By.CSS_SELECTOR, ".card-title a")
    card_footer = (By.CSS_SELECTOR, ".card-footer button")
    checkout = (By.XPATH, "//button[@class='btn btn-success']")

    def get_card_titles(self):
        return self.driver.find_elements(*CheckOutPage.card_title)

    def get_card_footer(self):
        return self.driver.find_elements(*CheckOutPage.card_footer)

    def checkout_items(self):
        return self.driver.find_element(*CheckOutPage.checkout)




