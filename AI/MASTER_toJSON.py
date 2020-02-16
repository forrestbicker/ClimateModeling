from json import load, dump
import numpy as np

#---------------------#
# Specify input paths #
#--------------A-------#
climateNOAA_path = "/Users/forrestbicker/Documents/Code/Python/WorkInProgress/MTF/data/AI/RAW/ClimateVariablesNOAA.json"
OverallUSDA_path = "/Users/forrestbicker/Documents/Code/Python/WorkInProgress/MTF/data/AI/RAW/OverallUSDA.json"
IndemnifiedUSDA_path = "/Users/forrestbicker/Documents/Code/Python/WorkInProgress/MTF/data/AI/RAW/IndemnifiedUSDA.json"

#---------------------#
# Specify output path #
#---------------------#
output_path = "/Users/forrestbicker/Documents/Code/Python/WorkInProgress/MTF/data/AI/OUT"

#-------#
# Setup #
#-------#
climateNOAA_dict = load(climateNOAA_path)
IndemnifiedUSDA_dict = load(IndemnifiedUSDA_path)
OverallUSDA_dict = load(OverallUSDA_path)

MASTER_dict = {}
# final JSON to be in the following form
#
#   {
#       "countyID-yyyy-mm": [
#           [tMax, tAvg, tMin, pcpt],
#           [severity, frequency],
#       ]
#   }
#

#-----------#
# Execution #
#-----------#

for countyID in OverallUSDA_dict:
    for year in OverallUSDA_dict[countyID]:
        for month in OverallUSDA_dict[countyID][year]:
            datapointID = countyID + year + month

            inputData = climateNOAA_dict[countyID][year][month]

            lostAcres = IndemnifiedUSDA_dict[countyID][year][month][0]
            totalAcres = IndemnifiedUSDA_dict[countyID][year][month][1]
            severity = round(lostAcres / totalAcres, 2)

            outputData = [severity]  # temp dummy

            MASTER_dict[datapointID] = [inputData, outputData]

with open(output_path, "w+") as outfile:
    dump(MASTER_dict, outfile)
