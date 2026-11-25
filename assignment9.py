import csv
import json

with open("input.csv", "r") as csv_file:  #  it will Read data from CSV file
    csv_reader = csv.DictReader(csv_file)

    data = list(csv_reader)

with open("output.json", "w") as json_file:    # it will Write data to JSON file
    json.dump(data, json_file, indent=4)

print("CSV data successfully converted to JSON.")
