import requests
import json
import os

db_path="db.json"
faces_path='faces'

data  = json.loads(open(db_path).read())


print(len(data), "records")

#pp=data['results'][0]['properties']['Aadhar_number']['title'][0]['text']['content']
#print(pp)

#each in list of records
for aadhar_number in data.keys():
    aadhar_number=aadhar_number
    photo_url=data[aadhar_number]['Photo']

    #print(type(aadhar_number),type(photo))

    folder_path = os.path.join(faces_path, aadhar_number)
    #print(folder_path)

    if not os.path.exists(folder_path):
        print("creating", folder_path)
        os.makedirs(folder_path)
    


    img_path=os.path.join(folder_path,'image.jpg')

    
    print("downloading ",img_path)
    r = requests.get(photo_url, allow_redirects=True)
    open(img_path, 'wb').write(r.content)

    


    
'''
url = data['results'][0]['properties']['Photo']['files'][0]['file']['url']

r = requests.get(url, allow_redirects=True)

open('image.jpg', 'wb').write(r.content)
'''