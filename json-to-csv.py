import json
import csv
from os import listdir
from os.path import isfile, join
import Tkinter as tk



def json_to_csv():
    directory = "json/"

    files = [f for f in listdir(directory) if isfile(join(directory, f))]
    filepaths = []
    data = []
    for f in files:
        if f[-5:] == ".json":
            filepaths += [directory + f]
        else:
            print "File " + f + " isn't a json file! It won't be included."

    for f in filepaths:
        jsonfile = open(f)
        data += [json.load(jsonfile)]

    for d in data:
        d_keys = d.keys()
        headers = []
        for x in xrange(0,len(d[d_keys[0]])):
            headers += [d[d_keys[0]][x].keys()]

        headers = [item for sublist in headers for item in sublist]
        headers = list(set(headers))

        csvfile = open('csv/aggregate_data.csv', 'wb')
        aggregatewriter = csv.DictWriter(csvfile, headers)
        aggregatewriter.writeheader()

        for data_key in d_keys:
            #for each subject
            curr_data = d[data_key]
            subjectfile = open("csv/" + str(data_key) + '.csv', 'wb')
            subjectwriter = csv.DictWriter(subjectfile, headers)
            subjectwriter.writeheader()
            for trial in curr_data:
                rowDict = {}
                for trial_key in trial.keys():
                    rowDict[trial_key] = trial[trial_key]
                subjectwriter.writerow(rowDict)
                aggregatewriter.writerow(rowDict)
            subjectfile.close()

            break



        csvfile.close()
        return




if __name__ == "__main__":
    json_to_csv()
