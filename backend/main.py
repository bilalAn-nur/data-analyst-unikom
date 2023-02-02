from typing import List

from fastapi import FastAPI
from pydantic import BaseModel

import json



app = FastAPI()


# json_data = open('../data/anime.json', encoding="utf8")
# anime = json_data.read()
# obj = json.loads(anime)

jsondataChannel = open('../data/channels.json', encoding="utf8")
channel = json.load(jsondataChannel)

@app.get("/api")
async def read_root():
    return channel