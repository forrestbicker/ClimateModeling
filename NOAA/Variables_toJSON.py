import os
import json
from collections import defaultdict

indir = "/Users/forrestbicker/Documents/Code/Python/WorkInProgress/MTF/data/NOAA/DOWNLOADS"
outpath = "/Users/forrestbicker/Documents/Code/Python/WorkInProgress/MTF/data/NOAA/OUT/climateNOAA_ALL_Month-Specific.json"

# jsonDict[countyID][year][month][dataID]
# dataID: 0 for tMax, 1 for tAvg, 2 for tMin, 3 for pcpt
jsonDict = defaultdict(lambda: defaultdict(lambda: defaultdict(list)))

countyDict = {
    "Adair": "001",
    "Adams": "003",
    "Allamakee": "005",
    "Appanoose": "007",
    "Audubon": "009",
    "Benton": "011",
    "Black Hawk": "013",
    "Boone": "015",
    "Bremer": "017",
    "Buchanan": "019",
    "Buena Vista": "021",
    "Butler": "023",
    "Calhoun": "025",
    "Carroll": "027",
    "Cass": "029",
    "Cedar": "031",
    "Cerro Gordo": "033",
    "Cherokee": "035",
    "Chickasaw": "037",
    "Clarke": "039",
    "Clay": "041",
    "Clayton": "043",
    "Clinton": "045",
    "Crawford": "047",
    "Dallas": "049",
    "Davis": "051",
    "Decatur": "053",
    "Delaware": "055",
    "Des Moines": "057",
    "Dickinson": "059",
    "Dubuque": "061",
    "Emmet": "063",
    "Fayette": "065",
    "Floyd": "067",
    "Franklin": "069",
    "Fremont": "071",
    "Greene": "073",
    "Grundy": "075",
    "Guthrie": "077",
    "Hamilton": "079",
    "Hancock": "081",
    "Hardin": "083",
    "Harrison": "085",
    "Henry": "087",
    "Howard": "089",
    "Humboldt": "091",
    "Ida": "093",
    "Iowa": "095",
    "Jackson": "097",
    "Jasper": "099",
    "Jefferson": "101",
    "Johnson": "103",
    "Jones": "105",
    "Keokuk": "107",
    "Kossuth": "109",
    "Lee": "111",
    "Linn": "113",
    "Louisa": "115",
    "Lucas": "117",
    "Lyon": "119",
    "Madison": "121",
    "Mahaska": "123",
    "Marion": "125",
    "Marshall": "127",
    "Mills": "129",
    "Mitchell": "131",
    "Monona": "133",
    "Monroe": "135",
    "Montgomery": "137",
    "Muscatine": "139",
    "O'Brien": "141",
    "Osceola": "143",
    "Page": "145",
    "Palo Alto": "147",
    "Plymouth": "149",
    "Pocahontas": "151",
    "Polk": "153",
    "Pottawattamie": "155",
    "Poweshiek": "157",
    "Ringgold": "159",
    "Sac": "161",
    "Scott": "163",
    "Shelby": "165",
    "Sioux": "167",
    "Story": "169",
    "Tama": "171",
    "Taylor": "173",
    "Union": "175",
    "Van Buren": "177",
    "Wapello": "179",
    "Warren": "181",
    "Washington": "183",
    "Wayne": "185",
    "Webster": "187",
    "Winnebago": "189",
    "Winneshiek": "191",
    "Woodbury": "193",
    "Worth": "195",
    "Wright": "197",
}

monthDict = {
    12: "Winter",
    1: "Winter",
    2: "Winter",
    3: "Spring",
    4: "Spring",
    5: "Spring",
    6: "Summer",
    7: "Summer",
    8: "Summer",
    9: "Autum",
    10: "Autum",
    11: "Autum",
}

for folderName in ["tMax", "tAvg", "tMin", "pcp"]:
    if folderName != ".DS_Store":
        print(folderName)
    # if folderName == "test":
        path = os.path.join(indir, folderName)
        for fileName in os.listdir(path):
            with open(os.path.join(path, fileName), "r") as f:
                jsonData = json.load(f)
                rawCountyID = jsonData["description"]["title"].split(",")[0]

                countyID = countyDict[rawCountyID[:-7]]

                for timeString in jsonData["data"]:
                    year = timeString[0:4]
                    if int(year) >= 0:
                        month = timeString[4:]
                        seasonID = monthDict[int(month)]
                        value = float(jsonData["data"][timeString]["value"])
                        jsonDict[folderName][month][year].append(value)


# for countyID in jsonDict["17"]:
#     outpath = os.path.join(outpath, countyID) + ".json"
#     with open(outpath, "w+") as outfile:
#         json.dump(jsonDict["17"][countyID], outfile)

with open(outpath, "w+") as outfile:
    json.dump(jsonDict, outfile, indent=4)
