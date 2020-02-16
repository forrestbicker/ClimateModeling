from json import load, dump

climateNOAA_path = "/Users/forrestbicker/Documents/Code/Python/WorkInProgress/MTF/data/static/ClimateVariablesNOAA.json"
OverallUSDA_path = "/Users/forrestbicker/Documents/Code/Python/WorkInProgress/MTF/data/static/OverallUSDA.json"
IndemnifiedUSDA_path = "/Users/forrestbicker/Documents/Code/Python/WorkInProgress/MTF/data/static/IndemnifiedUSDA.json"

climateNOAA_dict = load(climateNOAA_path)
OverallUSDA_dict = load(OverallUSDA_path)
IndemnifiedUSDA_dict = load(IndemnifiedUSDA_path)
