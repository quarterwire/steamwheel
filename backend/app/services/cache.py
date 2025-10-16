import httpx
from datetime import datetime
import json
from app.models.config import config


async def download_file(url=config.STEAM_API_ALL_GAMES):
    print("Running cache on Steam Endpoint" + datetime.today().strftime("%Y-%m-%d"))
    path = "app/db/"
    async with httpx.AsyncClient() as client:
        r = await client.get(url)
        data = r.json()
        print(data)
        filename = path + "steamgames.json"
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
