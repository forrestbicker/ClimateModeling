from json import load, dump
import numpy as np

#---------------------#
# Specify input paths #
#--------------A-------#
ClimateNOAA_path = "/Users/forrestbicker/Documents/Code/Python/WorkInProgress/MTF/data/AI/RAW/ClimateVariablesNOAA.json"
OverallUSDA_path = "/Users/forrestbicker/Documents/Code/Python/WorkInProgress/MTF/data/AI/RAW/OverallUSDA.json"
IndemnifiedUSDA_path = "/Users/forrestbicker/Documents/Code/Python/WorkInProgress/MTF/data/AI/RAW/IndemnifiedLosslessUSDA.json"

#---------------------#
# Specify output path #
#---------------------#
output_path = "/Users/forrestbicker/Documents/Code/Python/WorkInProgress/MTF/data/AI/OUT/MASTER.json"

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
# {
#     "countyID-yyyy-mm": [
#         [
#             tMax, 
#             tAvg, 
#             tMin, 
#             pcpt
#         ],
#         [
#             severity,
#             frequency
#         ],
#     ]
# }


counties = [f"{i:03}" for i in range(1, 199, 2)]
years = [str(i) for i in range(1991, 2020)]
months = [f"{i:02}" for i in range(1, 13)]

#----------#
# Function #
#----------#
def getData(countyID, year, month):
    datapointID = f"{countyID}-{year}-{month}"

    try:
        inputData = ClimateNOAA_dict[countyID][year][month]
    except KeyError:
        print(datapointID + " discarded, not found in IndemnClimateNOAA_dictifiedUSDA_dict")

    try:
        indemnifiedAcres, totalAcres, _ = IndemnifiedUSDA_dict[countyID][year][month]

        if totalAcres == 0:
            raise KeyError
        else:
            severity = min(1, round(indemnifiedAcres / totalAcres, 4))

    except KeyError:
        # print(datapointID + " discarded, not found in IndemnifiedUSDA_dict")
        severity = 0

    try:
        indemnifiedPolicies = IndemnifiedUSDA_dict[countyID][year][month][2]
    except KeyError:
        indemnifiedPolicies = 0

    try:
        totalPolicies = OverallUSDA_dict[countyID][year][0]
        frequency = round(indemnifiedPolicies / totalPolicies, 4)
    except KeyError:
        print(datapointID + " discarded, not found in OverallUSDA_dict")

    try:
        outputData = [severity, frequency]

        return [datapointID, [inputData, outputData]]
    except NameError:
        pass


#-----------#
# Execution #
#-----------#
for countyID in counties:
    for year in years:
        for month in months:
            try:
                datapointID, dataset = getData(countyID, year, month)
                MASTER_dict[datapointID] = dataset
            except TypeError:
                pass


with open(output_path, "w+") as outfile:
    print("Compeleted with " + str(len(MASTER_dict)) + " entries!")
    dump(MASTER_dict, outfile, indent=4)
