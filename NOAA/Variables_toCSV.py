import os
from json import load
from collections import defaultdict

inpath = "/Users/forrestbicker/Documents/Code/Python/WorkInProgress/MTF/data/NOAA/OUT/climateNOAA.json"
outdir = "/Users/forrestbicker/Documents/Code/Python/WorkInProgress/MTF/data/NOAA/OUT/"

with open(inpath, "r") as infile:
    climateNOAA_dict = load(infile)

for dataID, variableName in enumerate(["tMax", "tAvg", "tMin", "pcpt"]):
    with open(outdir + variableName + ".csv", "w+") as outfile:
        outfile.write("countyID,")
        for year in climateNOAA_dict["001"]:
            for month in climateNOAA_dict["001"][year]:
                outfile.write(year + ",")
        outfile.write("\n")

        outfile.write(",")
        for year in climateNOAA_dict["001"]:
            for month in climateNOAA_dict["001"][year]:
                outfile.write(month + ",")
        outfile.write("\n")

        for countyID in climateNOAA_dict:
            outfile.write(countyID)
            
            for year in climateNOAA_dict[countyID]:
                for month in climateNOAA_dict[countyID][year]:
                    datapoint = str(climateNOAA_dict[countyID][year][month][dataID])
                    outfile.write("," + datapoint)
            outfile.write("\n")
