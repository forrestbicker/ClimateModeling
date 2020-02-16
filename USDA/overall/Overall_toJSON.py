
from collections import defaultdict
from json import dump

inpath = "/Users/forrestbicker/Documents/Code/Python/Garbage/MiniPrograms/MTF/insuranceData/overall/RAW/countyDataIOWA.txt"
outpath = "/Users/forrestbicker/Documents/Code/Python/Garbage/MiniPrograms/MTF/insuranceData/overall/OUT/OverallInsuranceUSDAee.json"

# jsonDict[countyID][year][dataID]
jsonDict = defaultdict(lambda: defaultdict(list))  

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
    "O Brien": "141",
    "Osceola": "143",
    "Page": "145",
    "Palo Alto": "147",
    "Plymouth": "149",
    "Pocahontas": "151",
    "Polk": "153",
    "Pottawattamie": "155",
    "E Pottawattamie": "155",
    "East Pottawattamie": "155",
    "West Pottawattamie": "155",
    "W Pottawattamie": "155",
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

with open(inpath, "r") as infile:
    rows = infile.readlines()[1:]

for row in rows:
    cols = row.split("|")
    rawCountyID = cols[3]

    year = cols[0]

    totalPolicies = int(cols[4])
    indemnifiedPolicies = int(cols[6])
    acres = int(float(cols[9]))

    if rawCountyID != "All Other Counties" and rawCountyID != "Unknown" and year != "2020":

        countyID = countyDict[rawCountyID]

        if len(jsonDict[countyID][year]) == 0:
            jsonDict[countyID][year] = [0]

        # jsonDict[countyID][year][0] += indemnifiedPolicies
        jsonDict[countyID][year][0] += totalPolicies
        # jsonDict[countyID][year][2] += acres

with open(outpath, "w+") as outfile:
    rows = outfile.readlines()
    dump(jsonDict, outfile, indent=4)
