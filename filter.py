import os, pathlib, json

with open(r'C:\Users\jonfa\AppData\Local\Temp\Temp1_companyfacts.zip\CIK0000001750.json', 'r') as file:
    data = json.load(file)

facts = data['facts']

print(len(facts['dei']))