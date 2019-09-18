import json

info = '''
{   "Personal_information":
    {
    "Name": "Anastasiia Ishchenko",
    "Phone": "052483078",
    "Age": 17,
    },
    "Personality":
    {
    "Hobbys": "swimming, reading",
    "Favorite music": "indie and alternirive",
    "Guilty pleasure": "The Try Guys videos",
    "I am obsessed with cats": true,
    "My dream": "to visit my best friend in Egypt",
    "My goal": "to have a trip with my another friend to Saint Petersburg"
    }
}
'''

file = 'info.json'
with open(file, 'w') as a:
    json.dump(info, a)

file = 'info.json'
with open(file,) as b:
    info2 = json.load(b)
    print(info2)
