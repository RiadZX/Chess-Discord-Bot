import scraper

class Chess:
    def __init__(self):
        self.scraper = scraper.Scraper()
        pass

    def get_stats(self, profile):
        data = self.scraper.get_profile(profile)
        returnData = {}
        print(data)
        for stat in data["stats"]:
            if stat["key"] == "bullet":
                returnData["bulletRating"] = stat["stats"]["rating"]
                returnData["bulletGames"] = stat["gameCount"]
            elif stat["key"] == "rapid":
                returnData["rapidRating"] = stat["stats"]["rating"]
                returnData["rapidGames"] = stat["gameCount"]
            elif stat["key"] == "blitz":
                returnData["blitzRating"] = stat["stats"]["rating"]
                returnData["blitzGames"] = stat["gameCount"]

        return returnData