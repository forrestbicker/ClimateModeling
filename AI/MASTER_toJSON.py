from json import load, dump
import numpy as np

#---------------------#
# Specify input paths #
#--------------A-------#
ClimateNOAA_path = "/Users/forrestbicker/Documents/Code/Python/WorkInProgress/MTF/data/AI/RAW/ClimateVariablesNOAA.json"
OverallUSDA_path = "/Users/forrestbicker/Documents/Code/Python/WorkInProgress/MTF/data/AI/RAW/OverallUSDA.json"
IndemnifiedUSDA_path = "/Users/forrestbicker/Documents/Code/Python/WorkInProgress/MTF/data/AI/RAW/IndemnifiedUSDA.json"

#---------------------#
# Specify output path #
#---------------------#
output_path = "/Users/forrestbicker/Documents/Code/Python/WorkInProgress/MTF/data/AI/OUT"

#-------#
# Setup #
#-------#
with open(ClimateNOAA_path, "r") as ClimateNOAA_file:
    ClimateNOAA_dict = load(ClimateNOAA_file)

with open(IndemnifiedUSDA_path, "r") as IndemnifiedUSDA_file:
    IndemnifiedUSDA_dict = load(IndemnifiedUSDA_file)

with open(OverallUSDA_path, "r") as OverallUSDA_file:
    OverallUSDA_dict = load(OverallUSDA_file)

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
            datapointID = countyID + year + str(month)

            try:
                inputData = ClimateNOAA_dict[countyID][year][month]

                indemnifiedAcres = IndemnifiedUSDA_dict[countyID][year][month][0]
                totalAcres = IndemnifiedUSDA_dict[countyID][year][month][1]
                severity = round(indemnifiedAcres / totalAcres, 2)

                indemnifiedPolicies = OverallUSDA_dict[countyID][year][0]
                totalPolicies = OverallUSDA_dict[countyID][year][1]
                frequency = round(indemnifiedPolicies / totalPolicies, 2)

                outputData = [severity, frequency]

                MASTER_dict[datapointID] = [inputData, outputData]
            except KeyError:
                print(datapointID)

with open(output_path, "w+") as outfile:
    dump(MASTER_dict, outfile)
