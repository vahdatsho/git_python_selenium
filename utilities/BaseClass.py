import inspect

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
import logging



@pytest.mark.usefixtures("setup")
class BaseClass:

    def verify_link_presence(self, text):
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, text)))

    def select_option_by_text(self, locator, text):

        sel = Select(locator)
        sel.select_by_visible_text(text)

    def get_logger(self):

        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)

        fileHandler = logging.FileHandler('my_log_file.log')  # path where log file will be stored

        formatter = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s ")  # in which format to print

        fileHandler.setFormatter(formatter)  # passing formatter to fileHandler

        logger.addHandler(fileHandler)  # fileHandler object
        logger.setLevel(logging.DEBUG)  # set level to print that level info

        return logger




