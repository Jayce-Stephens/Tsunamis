import unittest
import requests
from PerformScraping import Scraper
from bs4 import BeautifulSoup
from unittest.mock import patch, MagicMock

class ScaperTest(unittest.TestCase):

    @patch('PerformScraping.requests.get')
    def test_getAcademicCalander_success(self,mock_get):
        url = "https://sample.com"
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.text = "<html><head><title>Academic Calendar</title></head></html>"
        mock_get.return_value = mock_response

        soup = Scraper.getAcademicCalander(url)

        self.assertIsInstance(soup, BeautifulSoup)
        self.assertEqual(soup.text, "Academic Calendar")

    @patch('PerformScraping.requests.get')
    def test_getAcademicCalander_no_url_provided(self, mock_get):
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.text = "<html><head><title>Academic Calendar</title></head></html>"
        mock_get.return_value = mock_response

        soup = Scraper.getAcademicCalander()

        self.assertIsInstance(soup, BeautifulSoup)



if __name__=='__main__':
    unittest.main()