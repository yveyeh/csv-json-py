import csv
import json

def csvToJSON(csvFile):
    with open(csvFile) as csv_file:
        return json.dumps([lines for lines in csv.DictReader(csv_file)], indent=4)

# def jsonToCSV(jsonFile):
    # code


# driver code
csv_file = r'file.csv'
json_file = r'file.json'

with open(json_file, 'w') as file:
    file.write(csvToJSON(csv_file))
