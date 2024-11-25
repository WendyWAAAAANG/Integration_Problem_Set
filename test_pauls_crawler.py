import unittest
from unittest.mock import patch, MagicMock
from bs4 import BeautifulSoup
from selenium.common.exceptions import TimeoutException
from Pauls_Crawler import scrape_mathjax_problems


class TestMathJaxCrawler(unittest.TestCase):
    def setUp(self):
        """Set up mock driver and example HTML content."""
        self.mock_html = """
        <html>
            <body>
                <ol class="assign-problems">
                    <li>
                        <script type="math/tex">\\int_{0}^{\\infty }{\\frac{1}{{z{{\\left[ {\\ln \\left( z \\right)} \\right]}^2}}}\\,dz}</script>
                    </li>
                    <li>
                        <script type="math/tex">\\int_{0}^{\\infty }{\\frac{1}{{w - 1}}}\\,dw}</script>
                    </li>
                </ol>
            </body>
        </html>
        """
        self.mock_driver = MagicMock()
        self.mock_driver.page_source = self.mock_html

    def test_scrape_mathjax_problems(self):
        """Test the scraping of MathJax problems from a mock HTML page."""
        category = "Improper Integrals"
        problems = scrape_mathjax_problems(self.mock_driver, "mock_url", category)

        self.assertEqual(len(problems), 2)

        self.assertEqual(problems[0]["difficulty"], "Moderate")
        self.assertEqual(problems[0]["category"], category)
        self.assertEqual(
            problems[0]["question"],
            "\\int_{0}^{\\infty }{\\frac{1}{{z{{\\left[ {\\ln \\left( z \\right)} \\right]}^2}}}\\,dz}"
        )

        self.assertEqual(
            problems[1]["question"],
            "\\int_{0}^{\\infty }{\\frac{1}{{w - 1}}}\\,dw}"
        )

    @patch("Pauls_Crawler.WebDriverWait")
    def test_scraper_handles_timeout(self, mock_wait):
        """Test that the scraper handles a timeout scenario."""
        mock_wait.side_effect = TimeoutException("Timeout occurred")

        problems = scrape_mathjax_problems(self.mock_driver, "mock_url", "Category")
        self.assertEqual(len(problems), 0)

    def test_no_mathjax_problems_found(self):
        """Test scraper behavior when no MathJax problems are present."""
        self.mock_driver.page_source = "<html><body><p>No problems here!</p></body></html>"

        problems = scrape_mathjax_problems(self.mock_driver, "mock_url", "Empty Category")
        self.assertEqual(len(problems), 0)


if __name__ == "__main__":
    unittest.main()
