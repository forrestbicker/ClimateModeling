from collections import defaultdict
from json import dump
from os.path import isfile, join
from os import listdir

indir = "/Users/forrestbicker/Documents/Code/Python/WorkInProgress/MTF/data/USDA/indemnified/RAW/"
outfile = "/Users/forrestbicker/Documents/Code/Python/WorkInProgress/MTF/data/USDA/indemnified/OUT/IndemnifiedInsuranceUSDA_Lossless.json"

# jsonDict[countyID][year][month][dataID]
# DataID: 1 for lostAcres, 2 for plantedAcres, 3 for policitesIndemnified
jsonDict = defaultdict(lambda: defaultdict(lambda: defaultdict(lambda: defaultdict(list))))


inpaths = [indir + f for f in listdir(indir) if f[0] != "."]

lossDict = {
    "Cold Wet Weather": 0,
    "Drought": 1,
    "Excess Moisture/Precipitation/Rain": 2,
    "Freeze": 3,
    "Frost": 4,
    "Hail": 5,
    "Heat": 6,
    "Hot Wind": 7,
}


for inpath in inpaths:
    print(inpath.split("/")[-1])

    with open(inpath, "r") as infile:
        lines = infile.readlines()
        for line in lines:
            elements = line.split("|")

            year = elements[0]
            month = elements[13]

            state = elements[2]
            county = elements[3].strip()

            crop = elements[6].strip()
            causeOfLoss = elements[12].strip()

            if (crop == "CORN" and state == "IA" and causeOfLoss in lossDict.keys()):

                plantedAcres = float(elements[18].strip())
                lostAcres = float(elements[27].strip())
                policiesIndemnified = int(elements[17].strip())

                if len(jsonDict[county][year][month]) == 0:
                    jsonDict[county][year][month] = [0, 0, 0]

                jsonDict[county][year][month][0] += lostAcres
                jsonDict[county][year][month][1] += plantedAcres
                jsonDict[county][year][month][2] += policiesIndemnified

for county in jsonDict:
    for year in jsonDict[county]:
        for month in jsonDict[county][year]:
            for dataID in [0, 1]:
                n = round(jsonDict[county][year][month][dataID], 2)
                jsonDict[county][year][month][dataID] = n

with open(outfile, "w+") as outfile:
    dump(jsonDict, outfile, indent=4)
