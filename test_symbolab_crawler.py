import unittest
from unittest.mock import patch, MagicMock
from Symbolab_Crawler import setup_driver, scrape_page, scrape_all_pages


class TestSymbolabCrawler(unittest.TestCase):
    def setUp(self):
        """Set up mock driver and example subpages."""
        self.mock_driver = MagicMock()

        self.mock_html = """
        <html>
            <body>
                <div class="mathquill-rendered-math">∫ x^2 dx</div>
                <div class="mathquill-rendered-math">∫ sin(x) dx</div>
            </body>
        </html>
        """

        self.subpages = {
            "https://mockurl.com/Basic": {"difficulty": "Basic", "category": "Constant Rule"},
            "https://mockurl.com/Moderate": {"difficulty": "Moderate", "category": "Power Rule"},
        }

    @patch("Symbolab_Crawler.webdriver.Chrome")
    def test_setup_driver(self, mock_chrome):
        """Test that the WebDriver is set up correctly."""
        driver = setup_driver()
        self.assertTrue(mock_chrome.called)
        self.assertIsNotNone(driver)

    def test_scrape_page(self):
        """Test that scrape_page extracts formulas correctly."""
        self.mock_driver.page_source = self.mock_html
        self.mock_driver.find_elements.return_value = [
            MagicMock(text="∫ x^2 dx"),
            MagicMock(text="∫ sin(x) dx"),
        ]

        problems = scrape_page(self.mock_driver, "https://mockurl.com/Basic", "Basic", "Constant Rule")
        
        self.assertEqual(len(problems), 2)

        self.assertEqual(problems[0]["difficulty"], "Basic")
        self.assertEqual(problems[0]["category"], "Constant Rule")
        self.assertEqual(problems[0]["question"], "∫ x^2 dx")

        self.assertEqual(problems[1]["question"], "∫ sin(x) dx")

    def test_scrape_all_pages(self):
        """Test that scrape_all_pages aggregates data correctly."""
        with patch("Symbolab_Crawler.scrape_page") as mock_scrape_page:
            mock_scrape_page.side_effect = [
                [{"difficulty": "Basic", "category": "Constant Rule", "question": "∫ x^2 dx"}],
                [{"difficulty": "Moderate", "category": "Power Rule", "question": "∫ x^3 dx"}],
            ]
            problems = scrape_all_pages(self.mock_driver, self.subpages)

        self.assertEqual(len(problems), 2)

        self.assertEqual(problems[0]["question"], "∫ x^2 dx")
        self.assertEqual(problems[1]["question"], "∫ x^3 dx")


if __name__ == "__main__":
    unittest.main()
