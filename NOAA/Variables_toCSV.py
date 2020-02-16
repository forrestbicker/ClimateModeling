import os
import json
from collections import defaultdict

inpath = "/Users/forrestbicker/Documents/Code/Python/Garbage/MiniPrograms/MTF/NOAA/DOWNLOADS/"
outbasepath = "/Users/forrestbicker/Documents/Code/Python/Garbage/MiniPrograms/MTF/NOAA/OUT_CSV/"
jsonDict = defaultdict(lambda: defaultdict(lambda: defaultdict(lambda: defaultdict(list))))


stateID = "17"

for dataID, folderName in enumerate(["tMax", "tAvg", "tMin", "pcp"]):
    if folderName != ".DS_Store":
        print(folderName)
    # if folderName == "test":
        path = os.path.join(inpath, folderName)
        for fileName in os.listdir(path):
            with open(os.path.join(path, fileName), "r") as f:
                jsonData = json.load(f)
                countyID = jsonData["description"]["title"].split(",")[0]

                for timeString in jsonData["data"]:
                    year = timeString[0:4]
                    month = timeString[4:]
                    value = jsonData["data"][timeString]["value"]
                    jsonDict[stateID][countyID][year][month].append(value)

    with open(outbasepath + str(dataID) + ".csv", "a+") as outfile:
        for countyID in jsonDict["17"]:
            for year in jsonDict["17"][countyID]:
                for month in jsonDict["17"][countyID][year]:
                    outfile.write(jsonDict["17"][countyID][year][month][dataID])
                    outfile.write(", ")
            outfile.write("\n")
