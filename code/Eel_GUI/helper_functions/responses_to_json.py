import json
import requests

data = json.loads(open('helper_functions/responses_secret.json').read()) # Opens the file
# Secret here:
secret = data['id']

# Database information here:
database = data['database']

geturl = f"https://api.notion.com/v1/databases/{database}/query"
url = 'https://api.notion.com/v1/pages'
headers = {
    'Authorization': f'Bearer {secret}',
    'Content-Type': 'application/json',
    'Notion-Version': '2021-05-13'
}

geturl = f"https://api.notion.com/v1/databases/{database}/query"

res = requests.request("POST", geturl, headers=headers)
columns = list(res.json()['results'][0]['properties'].keys())
#rint(res.json())
#print(columns)

def create_json_db(response_dict,columns=columns,database= database):
    
    parent={}
    parent["database_id"]= f"{database}"

    properties={}

    for col in columns:
        for key in response_dict.keys():
            if col in key:

                """if(col=='Date of birth'):
                    dob={}
                    date={}
                    date['start']=response_dict[key]
                    
                    dob['date']=date
                    properties[col]=dob"""

                if(col=='Aadhar_number'):
                    title={}
                    title['title']=[]
                    text={}
                    content={}

                    content['content']=response_dict[key]
                    text['text']=content
                    title['title'].append(text)
                    
                    properties[col]=title
            
                else:
                    rich_text={}
                    rich_text['rich_text']=[]
                    text={}
                    content={}

                    content['content']=response_dict[key]
                    text['text']=content
                    rich_text['rich_text'].append(text)
                    
                    properties[col]=rich_text

    db_dict={}
    db_dict["parent"]=parent
    db_dict["properties"]=properties
    #return db_dict

    response = requests.post(url, headers=headers, json=db_dict)
    print(response.status_code)
    # Serializing json 
    #json_object = json.dumps(db_dict, indent = 4)
    
    # Writing to sample.json
    #with open("to_responses_db.json", "w") as outfile:
    #    outfile.write(json_object)
    
    #return db_dict


        
if __name__=="__main__":
    response_dict={'Aadhar_number':'7720 5883 9966', ' is this your Name ?': 'Pranav', ' is this your Date of birth ?': '1985-02-01', ' is this your Address ?': 'SRMAB', ' is this your Gender ?': 'Male', 'Please select your Category.': 'General'}
    #columns=['Aadhar_number','Disability type', 'Gender', 'Address', 'Date of birth', 'Disability Certificate', 'Category', 'Name']

    create_json_db(response_dict)
