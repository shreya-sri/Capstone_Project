import json, requests
import os

#secret_path = os.path.join(os.getcwd(), 'SECRET.json')
secret_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'SECRET.json')

data = json.loads(open(secret_path).read()) # Opens the file
# Secret here:
secret = data['id']

# Database information here:
database = data['database']

# Headers
headers = {
    'Authorization': f'Bearer {secret}',
    'Content-Type': 'application/json',
    'Notion-Version': '2021-05-13'
}

def readDatabase(database, headers):
    readUrl = f"https://api.notion.com/v1/databases/{database}/query"

    res = requests.request("POST", readUrl, headers=headers)
    data = res.json()
    data_dict = dict()
    for records in data['results']:
        temp = dict()
        record = records['properties']
        index = record["Aadhar_number"]['title'][0]['plain_text']
        for key in record.keys():
            if key == "Aadhar_number":
                continue
            if key == "Photo":
                val = record[key]['files'][0]['file']['url']
            elif key == 'Date of birth':
                val = record[key]['date']['start']
            else:
                val = record[key]['rich_text'][0]['plain_text']
            temp[key] = val
        
        data_dict[index] = temp
        

    #print(res.status_code)
    #print(res.text)

    with open('db.json', 'w', encoding='utf8') as f:
        json.dump(data_dict, f, indent=4, ensure_ascii=False)

readDatabase(database, headers)