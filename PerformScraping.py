from bs4 import BeautifulSoup
import requests

class Scraper:

    def getAcademicCalander():
        url =  "https://www.xula.edu/academics/academiccalendar/index.html"
        headers = {
            "User-Agent": "Mozilla/5.0"
        }
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, "html.parser")

        if response.status_code == 200:
            print("Fetched webpage")
            print (soup)
        else:
            print("Could not find page")

   
        