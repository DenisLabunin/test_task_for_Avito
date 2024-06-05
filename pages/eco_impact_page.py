from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class EcoImpact(BasePage):

    ENERGY_COUNTER = (By.XPATH, '//div[@class="desktop-impact-item-eeQO3"][last()]')
    WATER_COUNTER = (By.XPATH, '//div[@class="desktop-impact-item-eeQO3"][4]')
    CO2_COUNTER = (By.XPATH, '//div[@class="desktop-impact-item-eeQO3"][2]')

    SCREENSHOT_DIR = 'output'

    def energy_take_screenshot(self):
        self.browser.find_element(*self.ENERGY_COUNTER).screenshot(f'./{self.SCREENSHOT_DIR}/TC02.png')

    def water_take_screenshot(self):
        self.browser.find_element(*self.WATER_COUNTER).screenshot(f'./{self.SCREENSHOT_DIR}/TC01.png')

    def co2_take_screenshot(self):
        self.browser.find_element(*self.CO2_COUNTER).screenshot(f'./{self.SCREENSHOT_DIR}/TC03.png')

    def is_energy_counter_displayed(self):
        return self.browser.find_element(*self.ENERGY_COUNTER).is_displayed()

    def is_water_counter_displayed(self):
        return self.browser.find_element(*self.WATER_COUNTER).is_displayed()

    def is_co2_counter_displayed(self):
        return self.browser.find_element(*self.CO2_COUNTER).is_displayed()