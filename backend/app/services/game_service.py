from app.models.steam.types import Data
import requests
from app.models.config import config
import random
from app.db.db import jsonData


def get_game_by_id(game_id: int) -> Data:
    api_url = config.STEAM_API_GET_GAME + str(game_id)
    res = requests.get(api_url).json()
    print("get_Game", res, api_url)
    if not res:
        return {"err": "try again"}
    if not res[str(game_id)]["success"]:
        return {"err": "not found"}

    game = Data.model_validate(res[str(game_id)]["data"])
    return game


async def get_random_game():
    while True:
        if not jsonData or "applist" not in jsonData or not jsonData["applist"]["apps"]:
            return {"error": "Cache data not yet available. Try again soon."}

        res = random.choice(jsonData["applist"]["apps"])
        game = get_game_by_id(res["appid"])

        if isinstance(game, dict) and game.get("err"):
            continue
        if "Playtest" in game.name:
            continue
        if not game.recommendations:
            continue
        if game.recommendations.total < 5:
            continue

        if game and game.type not in [
            "dlc",
            "demo",
            "music",
            "mod",
            "advertising",
            "episode",
        ]:
            return game
