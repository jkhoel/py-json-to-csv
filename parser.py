import csv
import os
import json

# GLOBAL CONSTANTS
DATA_DIR = './json/'
OUTPUT_FILENAME = 'output.csv'
DELIMITER = ';'

# Define the header of each column
TABLE_HEADERS = ['File Name', 'Color', 'Description']

# List of key-names for the key-value pairs to pull from each file to populate the rows. Note that these have to exactly match the keys in the JSON files
TABLE_KEYS = ['color', 'description']

# Instantiate the csv writer and the output file
outputFile = open(OUTPUT_FILENAME, 'wb')
csvFile = csv.writer(outputFile, delimiter=DELIMITER)

# Define and add header row to the csvFile
csvFile.writerow(TABLE_HEADERS)

# Iterate trough all files in the folder DATA_DIR so that their JSON can be read, parsed and written as a new row in the CSV file
for filename in os.listdir(DATA_DIR):
    # Skip all non-JSON files
    if not filename.endswith('.json'):
        continue

    # Read the JSON file, then parse it
    file=open(DATA_DIR + filename)
    contents=json.load(file)

    # Log the filename to the console for user feedback
    print('Filename: ' + filename)

    # This list (array) will hold the values from each key-value pair defined in TABLE_KEYS
    rowData = [filename]

    # Iterate over all keys found in the JSON, and populate 'rowData' with each key-value if they exist in the TABLE_KEY list
    for key in contents.keys():
      if key in TABLE_KEYS:
        print('true! '+ key)
        rowData.append(contents[key])
      else:
        print('false! '+ key)
        rowData.append(DELIMITER)

    # Add a new row to the CSV file with the data from the current *.JSON file
    csvFile.writerow(rowData)
