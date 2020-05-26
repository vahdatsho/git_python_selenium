
from PageObjects.CheckoutPage import CheckOutPage
from PageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass


class TestOne(BaseClass):

    def test_end_to_end(self):

        log = self.get_logger()

        home_page = HomePage(self.driver)

        home_page.shopitems().click()
        log.info("Getting all the card titles")

        checkout_page = CheckOutPage(self.driver)

        cards = checkout_page.get_card_titles()

        i = -1

        for card in cards:

            i += 1

            card_text = card.text
            log.info(card_text)
            if card_text == "Blackberry":
                checkout_page.get_card_footer()[i].click()

        self.driver.find_element_by_css_selector("a[class*='btn-primary']").click()

        checkout_page.checkout_items().click()

        log.info("Entering country name")
        self.driver.find_element_by_id("country").send_keys("ind")

        self.verify_link_presence("India")

        self.driver.find_element_by_link_text("India").click()

        self.driver.find_element_by_xpath("//div[@class='checkbox checkbox-primary']").click()

        self.driver.find_element_by_css_selector("[type='submit']").click()

        text_match = self.driver.find_element_by_css_selector("[class*='alert-success']").text
        log.info("Text received from application is " + text_match)


        assert ("Success! Thank you!" in text_match)
















