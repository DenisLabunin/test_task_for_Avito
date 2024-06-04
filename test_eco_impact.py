from base_test import BaseTest


LINK = 'https://www.avito.ru/avito-care/eco-impact'


class TestEcoImpactCounter(BaseTest):
    def test_energy(self, browser):
        self.eco_impact_page.open(LINK)
        self.eco_impact_page.is_opened(LINK)
        self.eco_impact_page.is_energy_counter_displayed()
        self.eco_impact_page.energy_take_screenshot()

    def test_water(self, browser):
        self.eco_impact_page.open(LINK)
        self.eco_impact_page.is_opened(LINK)
        self.eco_impact_page.is_water_counter_displayed()
        self.eco_impact_page.water_take_screenshot()

    def test_co2(self, browser):
        self.eco_impact_page.open(LINK)
        self.eco_impact_page.is_opened(LINK)
        self.eco_impact_page.is_co2_counter_displayed()
        self.eco_impact_page.co2_take_screenshot()
