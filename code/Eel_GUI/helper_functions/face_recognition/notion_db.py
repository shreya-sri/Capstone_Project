import json, requests


data = json.loads(open('SECRET.json').read()) # Opens the file
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
    print(res.status_code)
    #print(res.text)

    with open('db.json', 'w', encoding='utf8') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

readDatabase(database, headers)