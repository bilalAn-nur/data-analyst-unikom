from typing import List
from fastapi import FastAPI
from pydantic import BaseModel
import json


app = FastAPI()


jsondataChannel = open('../data/channels.json', encoding="utf8")
channel = json.load(jsondataChannel)

jsondataSuperchat = open('../data/superchat_stats.json', encoding="utf8")
superchat = json.load(jsondataSuperchat)

#untuk mengfilter hanya hololive yang tampil
def hololiveFilter(talent):
    return talent['affiliation'] == "Hololive"
hololiveTalent = list(filter(hololiveFilter, channel))

# untuk mengurutkan jumlah subscriber terbanyak
sortedsubs = sorted(hololiveTalent, key=lambda x: x['subscriptionCount'], reverse=True)

#hapus channel hololive
for i, item in enumerate(sortedsubs):
    if item["channelId"] == "UCJFZiqLMntJufDCHc6bQixg":
        del sortedsubs[i]

jumlahAgensiVtuber = {}

for vtuber in channel:
    affiliation = vtuber["affiliation"]
    if affiliation in jumlahAgensiVtuber:
        jumlahAgensiVtuber[affiliation] += 1
    else:
        jumlahAgensiVtuber[affiliation] = 1

sorted_jumlahAgensiVtuber = sorted(jumlahAgensiVtuber.items(), key=lambda x: x[1], reverse=True)

totalagensi = sum(jumlahAgensiVtuber.values())

other = totalagensi - (jumlahAgensiVtuber["Independents"] + jumlahAgensiVtuber["Nijisanji"]+ jumlahAgensiVtuber["Hololive"]+ jumlahAgensiVtuber["Twitch Independents"])

result = []
for item in sorted_jumlahAgensiVtuber:
    temp = {}
    temp["id"] = item[0]
    temp["value"] = item[1]
    result.append(temp)

Independents = round((jumlahAgensiVtuber["Independents"] / totalagensi) * 100, 1)
hololive = round((jumlahAgensiVtuber["Hololive"] / totalagensi) * 100, 1)
nijisanji = round((jumlahAgensiVtuber["Nijisanji"] / totalagensi) * 100, 1)
TwitchIndependents = round((jumlahAgensiVtuber["Twitch Independents"] / totalagensi) * 100, 1)
Other_persen = round((other / totalagensi) * 100, 1)

persenbar = []
persenbar.append({"id": "Independen", "value": Independents})
persenbar.append({"id": "Hololive", "value": hololive})
persenbar.append({"id": "Nijisanji", "value": nijisanji})
persenbar.append({"id": "Twitch Independents", "value": TwitchIndependents})
persenbar.append({"id": "Other", "value": Other_persen})



@app.get("/api")
async def read_root():
    return channel

@app.get("/api/superchat")
async def read_root():
    return persenbar
#
@app.get("/api/hololive")
async def read_root():
    return hololiveTalent

@app.get("/api/hololive/barchart")
async def read_root():
    return sortedsubs[:10]


#======================================================================
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
