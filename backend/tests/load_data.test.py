import json
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

from models.types_ import Data


# Load JSON file
with open("template.json", "r", encoding="utf-8") as f:
    data = json.load(f)

# Parse JSON into the model
parsed = Data.model_validate(data["8930"]["data"])
print(parsed.about_the_game)
