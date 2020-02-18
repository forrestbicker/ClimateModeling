from json import load
from os import listdir
import sys

in_dir = "/Users/forrestbicker/Documents/Code/Python/WorkInProgress/MTF/data/USDA/indemnified/OUT/Loss-Specific/json/"
out_dir = "/Users/forrestbicker/Documents/Code/Python/WorkInProgress/MTF/data/USDA/indemnified/OUT/Loss-Specific/csv/"

for in_name in listdir(in_dir):
    in_basename = in_name.split(".")[0]
    print(in_basename)  # good place for walrus

    in_path = in_dir + in_name
    out_path = out_dir + in_name

    with open(in_path, "r") as in_file:
        in_dict = load(in_file)

    with open(out_path, "w+") as out_file:
        for county in in_dict:
            for year in in_dict[county]:
                for month in in_dict[county][year]:
                    out_file.write(str(year) + ",")
                    out_file.write(str(month) + ",")
                    for datapoint in in_dict[county][year][month].values():
                        out_file.write("," + str(datapoint))
            

# jsonDict[county][year][month][0] += lostAcres
