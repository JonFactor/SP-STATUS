#imports
from requests import request
import json
import pandas as pd

# get data
CIK = '0000320193'
req = request(url=f'https://data.sec.gov/submissions/CIK{CIK}.json',
            method='GET',
            headers={"User-Agent": "Mozilla/5.0"})

#mk raw db
db = pd.DataFrame.from_dict(req.json()['filings']['recent'])

#rm non-form 4s
count = 0
for i in db['form']:
     if i != '4':
          db = db.drop(count)
     count += 1
        

print(db)