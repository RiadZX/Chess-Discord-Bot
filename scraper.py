import requests, json

class Scraper:
    def __init__(self):
        pass

    def get_profile(self, link):
        link = link.replace("https://www.chess.com/member/", "")
        url = "https://www.chess.com/callback/member/stats/" + link
        print(url)
        response = requests.get(url)
        return response.json()

    def parse_profile(self, profile):
        pass