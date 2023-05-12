import json

class Data:
    def __init__(self) -> None:
        pass

    def load_user_profile(self, id):
        with open("./data/users.json") as f:
            data = json.load(f)
            for discordid in data:
                if discordid["discord_id"] == id:
                    return discordid["profile_link"]

    def save_user_profile(self, id, profile):
        with open("./data/users.json") as f:
            data = json.load(f)
            data.append({"discord_id": id, "profile_link": profile})
        with open("./data/users.json", "w") as f:
            json.dump(data, f)

    def check_user_existence(self, id):
        with open("./data/users.json") as f:
            data = json.load(f)
            for discordid in data:
                if discordid["discord_id"] == id:
                    return True
            return False

