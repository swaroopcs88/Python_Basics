


import json

"""
python_data = json.loads(response.text)
#print(python_data)
#print(type(python_data))
all_courses = python_data['data']['courses']
print(type(all_courses))

for i in all_courses:
    print(i['title'])
    
print(len(all_courses))
"""

"""
p = requests.get('https://dog.ceo/api/breeds/list/all')
#print(p.text)
python_data = p.json()
#print(type(python_data))
#print(python_data)

#for key, val in python_data['message'].items():
    #print(key, ":", len(val))

for i in python_data['message']['spaniel']:
     print(i)                       
"""    