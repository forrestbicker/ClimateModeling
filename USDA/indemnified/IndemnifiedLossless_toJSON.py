from collections import defaultdict
from json import dump
from os.path import isfile, join
from os import listdir

indir = "/Users/forrestbicker/Documents/Code/Python/WorkInProgress/MTF/data/USDA/indemnified/RAW/"
outfile = "/Users/forrestbicker/Documents/Code/Python/WorkInProgress/MTF/data/USDA/indemnified/OUT/IndemnifiedUSDA_ESZTER.json"

# jsonDict[countyID][year][month][dataID]
# DataID: 1 for lostAcres, 2 for plantedAcres, 3 for policitesIndemnified
jsonDict = defaultdict(lambda: defaultdict(lambda: defaultdict(lambda: defaultdict(list))))


inpaths = [indir + f for f in listdir(indir) if f[0] != "."]

lossDict = {
    # # cold
    # "Cold Wet Weather": 0,
    # "Freeze": 3,
    # "Frost": 4,
    
    # # wet
    # "Excess Moisture/Precipitation/Rain": 2,

    # # hot
    # "Heat": 6,
    # "Hot Wind": 7,

    # dry
    "Drought": 1,

    # # "Hail": 5,
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
                indemnifiedPolicies = int(elements[17].strip())
                indemnity = float(elements[28].strip())
                lossRatio = float(elements[29].strip())

                if len(jsonDict[county][year][month]) == 0:
                    jsonDict[county][year][month] = [0, 0, 0, 0, 0]

                jsonDict[county][year][month][0] += lostAcres
                jsonDict[county][year][month][1] += plantedAcres
                jsonDict[county][year][month][2] += indemnifiedPolicies
                jsonDict[county][year][month][3] += indemnity
                jsonDict[county][year][month][4] += lossRatio


for county in jsonDict:
    for year in jsonDict[county]:
        for month in jsonDict[county][year]:
            for dataID in [0, 1]:
                n = round(jsonDict[county][year][month][dataID], 2)
                jsonDict[county][year][month][dataID] = n

with open(outfile, "w+") as outfile:
    dump(jsonDict, outfile, indent=4)
