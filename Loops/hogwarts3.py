students=[
    {"name":"hermione", "house":"Gryffindor", "patronous":"Otter"},
    {"name":"Harry", "house":"Gryffindor", "patronous":"stag"},
    {"name":"Ron", "house":"Gryffindor", "patronous":"Jack russel terrir"},
    {"name":"Draco", "house":"Slytherin", "patronous":None},
    
]

for student in students:
    print(student["name"], student["house"], student["patronous"], sep=" , ")