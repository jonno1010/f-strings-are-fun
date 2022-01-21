people = [{
        'name': 'Jonny',
        'age': 46,
        'gender': 'Male'
    },
    {
        'name': 'Riley',
        'age': 50,
        'gender': 'Unknown'
    }
]


for person in people:
    print(f"{person.get('name')} is {person.get('age')} years old. {person.get('gender')}")