import pytest

from PageObjects.HomePage import HomePage
from TestData.HomePageData import HomePageData
from utilities.BaseClass import BaseClass


class TestHomePage(BaseClass):


    def test_for_submission(self, get_data):

        log = self.get_logger()

        homepage = HomePage(self.driver)
        log.info("First name is " + get_data["firstname"])
        homepage.get_name().send_keys(get_data["firstname"])
        homepage.get_email().send_keys(get_data["email"])
        homepage.get_check_box().click()

        self.select_option_by_text(homepage.get_gender(), get_data["gender"])

        homepage.submit_form().click()

        alert_text = homepage.get_success_message().text

        assert ("Success" in alert_text)

        self.driver.refresh()

    @pytest.fixture(params=HomePageData.get_test_data("testcase 2"))
    def get_data(self, request):
        return request.param





