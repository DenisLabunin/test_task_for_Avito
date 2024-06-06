from base_test import BaseTest


LINK = 'https://www.avito.ru/avito-care/eco-impact'


class TestEcoImpactCounter(BaseTest):
    def test_tc01(self, browser):
        self.eco_impact_page.open(LINK)
        self.eco_impact_page.is_opened(LINK)
        assert self.eco_impact_page.is_energy_counter_displayed(), 'Элемент не найден'
        self.eco_impact_page.energy_take_screenshot()

    def test_tc02(self, browser):
        self.eco_impact_page.open(LINK)
        self.eco_impact_page.is_opened(LINK)
        assert self.eco_impact_page.is_water_counter_displayed(), 'Элемент не найден'
        self.eco_impact_page.water_take_screenshot()

    def test_tc03(self, browser):
        self.eco_impact_page.open(LINK)
        self.eco_impact_page.is_opened(LINK)
        assert self.eco_impact_page.is_co2_counter_displayed(), 'Элемент не найден'
        self.eco_impact_page.co2_take_screenshot()
