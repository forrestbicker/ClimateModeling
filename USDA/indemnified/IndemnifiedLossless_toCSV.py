from collections import defaultdict
from json import dump
from os.path import isfile, join
from os import listdir

indir = "/Users/forrestbicker/Documents/Code/Python/WorkInProgress/MTF/data/USDA/indemnified/RAW/"
outfile = "/Users/forrestbicker/Documents/Code/Python/WorkInProgress/MTF/data/USDA/indemnified/OUT/IndemnifiedInsuranceUSDA_Lossless.csv"

# jsonDict[countyID][year][month][dataID]
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

                if len(jsonDict[county][year][month]) == 0:
                    jsonDict[county][year][month] = [0, 0]

                jsonDict[county][year][month][0] += lostAcres
                jsonDict[county][year][month][1] += plantedAcres

with open(outfile, "w+") as outfile:
    for county in jsonDict:
        for year in jsonDict[county]:
            for month in jsonDict[county][year]:
                rawData = jsonDict[county][year][month]
                roundedData = [round(i, 2) for i in rawData]

                rawOutData = [year, month, county, *roundedData]
                parsedOutData = [str(i) for i in rawOutData]

                outfile.write(",".join(parsedOutData))
                outfile.write("\n")
