import json

def create_json_db(response_dict,columns,database):
    
    parent={}
    parent["database_id"]= f"{database}"

    properties={}

    for col in columns:
        for key in response_dict.keys():
            if col in key:

                if(col=='Date of birth'):
                    dob={}
                    date={}
                    date['start']=response_dict[key]
                    
                    dob['date']=date
                    properties[col]=dob

                elif(col=='Aadhar_number'):
                    title={}
                    title['title']=[]
                    text={}
                    content={}

                    content['content']=response_dict[key]
                    text['text']=content
                    title['title'].append(text)
                    
                    properties[col]=title
                elif(col=='Aadhar_number'):
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

    
    # Serializing json 
    json_object = json.dumps(db_dict, indent = 4)
    
    # Writing to sample.json
    with open("to_responses_db.json", "w") as outfile:
        outfile.write(json_object)
        
if __name__=="__main__":
    
    response_dict={'Aadhar_number':'7720 5883 9966', ' is this your Name ?': 'Pranav', ' is this your Date of birth ?': '1985-02-01', ' is this your Address ?': 'SRMAB', ' is this your Gender ?': 'Male', 'Please select your Category.': 'General'}
    columns=['Aadhar_number','Disability type', 'Gender', 'Address', 'Date of birth', 'Disability Certificate', 'Category', 'Name']

    create_json_db(response_dict,columns,0)
