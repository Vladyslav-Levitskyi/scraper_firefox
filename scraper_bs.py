#   In this second part of code we use our source_file, that we get from "search_se.py" file,
#   now we can easily scrape html page on local machine without server load.
import json
from bs4 import BeautifulSoup

content = []

with open("source_file", "r", encoding="utf-8") as file:
    source_file = file.read()


#   Class BsScraper has one class method named general_scraper in this method we have four parameters
#   that we scrape from html pages. (Title, country, image link and link of movie)
#   The next step is to save all the necessary data in .json text format.
class BsScraper:

    def __init__(self, source):
        self.source = source

    @classmethod
    def general_scraper(cls):
        soup = BeautifulSoup(source_file, "html.parser")
        items = soup.find_all("div", class_="b-content__inline_item")
        for item in items:
            content.append({
                "title": item.find("div", class_="b-content__inline_item-link").find("a").get_text(),
                "country": item.find("div", class_="b-content__inline_item-link").find("div").get_text(),
                "image_link": item.find("div", class_="b-content__inline_item-cover").find("img").get("src"),
                "product_link": item.find("div", class_="b-content__inline_item-link").find("a").get("href")
            })
        with open("product_file.json", "a", encoding="utf-8") as file_json:
            json.dump(content, file_json, indent=4, ensure_ascii=False)
        print(*content, sep="\n")


data_scrape = BsScraper(source_file)
data_scrape.general_scraper()