from typing import List
from fastapi import FastAPI
from pydantic import BaseModel
import json
import pandas as pd


app = FastAPI()


jsondataChannel = open('../data/channels.json', encoding="utf8")
channel = json.load(jsondataChannel)
jsondataSuperchat = open('../data/superchat_stats.json', encoding="utf8")
superchat = json.load(jsondataSuperchat)
jsondataChatStats = open('../data/chat_stats.json', encoding="utf8")
chat_stats = json.load(jsondataChatStats)


# untuk mengfilter hanya hololive yang tampil
def hololiveFilter(talent):
    return talent['affiliation'] == "Hololive"


hololiveTalent = list(filter(hololiveFilter, channel))

# untuk mengurutkan jumlah subscriber terbanyak
sortedsubs = sorted(
    hololiveTalent, key=lambda x: x['subscriptionCount'], reverse=True)

sorted_video_count = sorted(
    hololiveTalent, key=lambda x: x['videoCount'], reverse=True)

# sorted_livechart

# hapus channel hololive
for i, item in enumerate(sortedsubs):
    if item["channelId"] == "UCJFZiqLMntJufDCHc6bQixg":
        del sortedsubs[i]


chat_counts = {}


def add_chat(data):
    channelId = data["channelId"]
    chats = data["chats"]
    if channelId in chat_counts:
        chat_counts[channelId] += chats
    else:
        chat_counts[channelId] = chats


for data in chat_stats:
    add_chat(data)

jumlahchat = []
for item in chat_counts:
    temp = {}
    temp["channelId"] = item
    temp["valuechat"] = chat_counts[item]
    jumlahchat.append(temp)

channelvidcout = []
for item1 in hololiveTalent:
    for item2 in jumlahchat:
        if item1['channelId'] == item2['channelId']:
            item2.update(item1)
            channelvidcout.append(item2)

sortedchat = sorted(channelvidcout, key=lambda x: x['valuechat'], reverse=True)


##########################################
jumlahAgensiVtuber = {}

for vtuber in channel:
    affiliation = vtuber["affiliation"]
    if affiliation in jumlahAgensiVtuber:
        jumlahAgensiVtuber[affiliation] += 1
    else:
        jumlahAgensiVtuber[affiliation] = 1

sorted_jumlahAgensiVtuber = sorted(
    jumlahAgensiVtuber.items(), key=lambda x: x[1], reverse=True)

totalagensi = sum(jumlahAgensiVtuber.values())

other = totalagensi - (jumlahAgensiVtuber["Independents"] + jumlahAgensiVtuber["Nijisanji"] +
                       jumlahAgensiVtuber["Hololive"] + jumlahAgensiVtuber["Twitch Independents"])

result = []
for item in sorted_jumlahAgensiVtuber:
    temp = {}
    temp["id"] = item[0]
    temp["value"] = item[1]
    result.append(temp)

Independents = round(
    (jumlahAgensiVtuber["Independents"] / totalagensi) * 100, 1)
hololive = round((jumlahAgensiVtuber["Hololive"] / totalagensi) * 100, 1)
nijisanji = round((jumlahAgensiVtuber["Nijisanji"] / totalagensi) * 100, 1)
TwitchIndependents = round(
    (jumlahAgensiVtuber["Twitch Independents"] / totalagensi) * 100, 1)
Other_persen = round((other / totalagensi) * 100, 1)

persenbar = []
persenbar.append({"id": "Independen", "value": Independents})
persenbar.append({"id": "Hololive", "value": hololive})
persenbar.append({"id": "Nijisanji", "value": nijisanji})
persenbar.append({"id": "Twitch Independents", "value": TwitchIndependents})
persenbar.append({"id": "Other", "value": Other_persen})

#############################################################

jumlahmatauang = {}

for matauang in superchat:
    curency = matauang["mostFrequentCurrency"]
    if curency in jumlahmatauang:
        jumlahmatauang[curency] += 1
    else:
        jumlahmatauang[curency] = 1

colors = [
    "#ff0000", "#00d4ff", "#16ff00", "#ffd600", "#ff7c00",
    "#ff00db", "#267fb1", "#2b7a1d", "#ffffff", "#A52A2A",
    "#84cd22", "#786209", "#073739", "#8ce74e", "#FF8C00",
    "#383c04", "#BDB76B", "#8FBC8F", "#2F4F4F", "#008000",
    "#4B0082", "#7CFC00", "#20B2AA", "#00FF00", "#7B68EE",
    "#FF4500", "#DB7093", "#DDA0DD"
]

superchatcurency = []
c = 0
for currency in jumlahmatauang:
    tempuang = {}
    tempuang["id"] = currency
    tempuang["value"] = jumlahmatauang[currency]
    tempuang["color"] = colors[c]
    superchatcurency.append(tempuang)
    c = c + 1


@app.get("/api")
async def read_root():
    return channel


@app.get("/api/agensi")
async def read_root():
    return persenbar
#


@app.get("/api/hololive")
async def read_root():
    return hololiveTalent


@app.get("/api/hololive/most_subscribers")
async def read_root():
    return sortedsubs


@app.get("/api/hololive/most_active_channels")
async def read_root():
    return sorted_video_count


@app.get("/api/hololive/chat")
async def read_root():
    return sortedchat


@app.get("/api/map")
async def read_root():
    return superchatcurency


# ======================================================================
# Generation 1
def hololiveGen1(talent):
    return talent['affiliation'] == "Hololive" and talent['group'] == "1st Generation"


Gen1 = list(filter(hololiveGen1, channel))


@app.get("/api/hololive/gen1")
async def read_root():
    return Gen1,

# Generation 1


def hololiveGen1(talent):
    return talent['affiliation'] == "Hololive" and talent['group'] == "1st Generation"


Gen1 = list(filter(hololiveGen1, channel))


@app.get("/api/hololive/gen1")
async def read_root():
    return Gen1,

# Generation 2


def hololiveGen2(talent):
    return talent['affiliation'] == "Hololive" and talent['group'] == "2nd Generation"


Gen2 = list(filter(hololiveGen2, channel))


@app.get("/api/hololive/gen2")
async def read_root():
    return Gen2

# Generation 3


def hololiveGen3(talent):
    return talent['affiliation'] == "Hololive" and talent['group'] == "3rd Generation"


Gen3 = list(filter(hololiveGen3, channel))


@app.get("/api/hololive/gen3")
async def read_root():
    return Gen3

# Generation 4


def hololiveGen4(talent):
    return talent['affiliation'] == "Hololive" and talent['group'] == "4th Generation"


Gen4 = list(filter(hololiveGen4, channel))


@app.get("/api/hololive/gen4")
async def read_root():
    return Gen4

# Generation 5


def hololiveGen5(talent):
    return talent['affiliation'] == "Hololive" and talent['group'] == "5th Generation"


Gen5 = list(filter(hololiveGen5, channel))


@app.get("/api/hololive/gen5")
async def read_root():
    return Gen5

# Generation 6


def hololiveGen6(talent):
    return talent['affiliation'] == "Hololive" and talent['group'] == "6th Generation (HoloX)"


Gen6 = list(filter(hololiveGen6, channel))


@app.get("/api/hololive/gen6")
async def read_root():
    return Gen6

# Indonesia Generation 1


def hololiveIndonesiaGen1(talent):
    return talent['affiliation'] == "Hololive" and talent['group'] == "Indonesia 1st Gen"


IndonesiaGen1 = list(filter(hololiveIndonesiaGen1, channel))


@app.get("/api/hololive/indonesiagen1")
async def read_root():
    return IndonesiaGen1

# Indonesia Generation 2


def hololiveIndonesiaGen1(talent):
    return talent['affiliation'] == "Hololive" and talent['group'] == "Indonesia 2nd Gen"


IndonesiaGen1 = list(filter(hololiveIndonesiaGen1, channel))


@app.get("/api/hololive/indonesiagen1")
async def read_root():
    return IndonesiaGen1

# Indonesia Generation 3


def hololiveIndonesiaGen1(talent):
    return talent['affiliation'] == "Hololive" and talent['group'] == "Indonesia 3th Gen"


IndonesiaGen1 = list(filter(hololiveIndonesiaGen1, channel))


@app.get("/api/hololive/indonesiagen1")
async def read_root():
    return IndonesiaGen1

# English Generation 1


def hololiveIndonesiaGen1(talent):
    return talent['affiliation'] == "Hololive" and talent['group'] == "Indonesia 1st Gen"


IndonesiaGen1 = list(filter(hololiveIndonesiaGen1, channel))


@app.get("/api/hololive/indonesiagen1")
async def read_root():
    return IndonesiaGen1

# Indonesia Generation 2


def hololiveIndonesiaGen1(talent):
    return talent['affiliation'] == "Hololive" and talent['group'] == "Indonesia 1st Gen"


IndonesiaGen1 = list(filter(hololiveIndonesiaGen1, channel))


@app.get("/api/hololive/indonesiagen1")
async def read_root():
    return IndonesiaGen1
