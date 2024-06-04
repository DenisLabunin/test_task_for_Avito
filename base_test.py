from pages.eco_impact_page import EcoImpact
import pytest


class BaseTest:

    @pytest.fixture(autouse=True)
    def setup(self, request, browser):
        request.cls.browser = browser
        request.cls.eco_impact_page = EcoImpact(browser)
