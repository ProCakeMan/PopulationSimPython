from os import read
from main import *
import json


def split():
    age = []
    pregnant = []
    people = []
    males = []
    females = []
    years = []
    filenames = {"Age.json": age, 
                "Pregnant.json": pregnant, 
                "People.json": people, 
                "Males.json": males, 
                "Females.json": females, 
                "Years.json": years}

    with open("Data/data.json", "r") as read_file:
        data = json.load(read_file)


    for i in data:
        print(i)
        age.append(i["Age"])
        pregnant.append(i["Pregnant"])
        people.append(i["People"])
        males.append(i["Males"])
        females.append(i["Females"])
        years.append(i["Years"])
        


    for i in filenames:
        with open('Data/' + i, 'w', encoding='utf-8') as f:
            json.dump(filenames[i], f, ensure_ascii=False, indent=4)