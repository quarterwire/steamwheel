import json

global jsonData
try:
    with open("app/db/steamgames.json", "r") as f:
        jsonData = json.load(f)
    print("Initial JSON data loaded.")
except FileNotFoundError:
    print("WARNING: Initial JSON file not found. Cache will populate soon.")
    jsonData = {"applist": {"apps": []}}  # Set a safe default
