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

        csvfile = open('aggregate_data.csv', 'wb')
        csv.DictWriter(csvfile, headers)

        for key in d_keys:
            #for each subject
            curr_data = d[key]
            for trial in curr_data:
                rowDict = {}
                print trial
                return



        csvfile.close()
        # for key in d.keys():
        #     print d[key].keys




if __name__ == "__main__":
    json_to_csv()
