# Json to Csv Converter
A python script that will turn a bunch of json files into csv files, and one aggregate csv.

# How to use
NOTE: This was designed specifically for processing data from experiments, and names files after the subject ids from those experiments. IF you just wanna get the aggregate file from this, comment out lines 41-43 and 48 (all the ones beginning with "subject"). Hopefully I can make a less narrow version in the future.

1. Download the files into a folder.
2. Put all your json files into one folder named "json"
3. Put the "json" folder in the same directory as the python script
4. Create another folder in the same directory as the python script, and name that one "csv"
5. Run the python script (in terminal, use cd to navigate to the script directory, then use the command "python json-to-csv.py")
