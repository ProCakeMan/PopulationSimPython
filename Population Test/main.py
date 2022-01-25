from math import inf
from posixpath import split
import random
import os
import json

startingPopulation = 50

infantMortality = 5
agriculture = 5
disasterChance = 10
food = 0
fertilityx = 18 # Min age at which a woman can become pregnant
fertilityy = 35 # Max age at which a woman can become pregnant
year = 0

peopleDictionary = []

results = []

class Person:
    def __init__(self, age):
        self.gender = random.randint(0, 1)
        self.age = age
        self.pregnant = 0   

def harvest(food, agriculture):
    ablePeople = 0
    for person in peopleDictionary:
        if person.age > 8:
            ablePeople += 1

    food += ablePeople * agriculture

    if food < len(peopleDictionary):
        del peopleDictionary[0:int(len(peopleDictionary) - food)]
        food = 0
    else:
        food -= len(peopleDictionary)

def reproduce(fertilityx, fertilityy, infantMortality):
    for person in peopleDictionary:
        if person.gender == 1:
            if person.age > fertilityx:
                if person.age < fertilityy:
                    if random.randint(0, 5) == 1:
                        person.pregnant = 1
                        if random.randint(0, 100) > infantMortality:
                            peopleDictionary.append(Person(0))
                            

def beginSim():
    for x in range(startingPopulation):
        peopleDictionary.append(Person(random.randint(18, 50)))

def writeDoc(peopleDict, year):
    pregnants = 0
    avrgAge = 0
    numPeople = len(peopleDict)
    male = 0
    female = 0
    for person in peopleDict:
        avrgAge += person.age
        if person.pregnant == 1:
            pregnants += 1
        if person.gender == 1:
            female += 1
        if person.gender == 0:
            male += 1
    avrgAge = avrgAge / numPeople
    avrgAge = round(avrgAge, 0)
    returnList = {"Age": str(avrgAge), "Pregnant": str(pregnants),
                "People": str(numPeople), "Males": str(male), "Females": str(female), 
                "Years": str(year)}
    return returnList
    


def runYear(food, agriculture, fertilityx, fertilityy, infantMortality, disasterChance, year):
    harvest(food, agriculture)
    year += 1
    for person in peopleDictionary:
        if person.age > 80:
            peopleDictionary.remove(person)
        else:
            person.age += 1
    reproduce(fertilityx, fertilityy, infantMortality)
    if random.randint(0, 100) < disasterChance:
        del peopleDictionary[0:int(random.uniform(0.05, 0.2) * len(peopleDictionary))]
    
    print(peopleDictionary[0].age)
    infantMortality *= 0.985
    return infantMortality


beginSim()



while len(peopleDictionary) < 1000 and len(peopleDictionary) > 1:
    runYear(food, agriculture, fertilityx, fertilityy, infantMortality, disasterChance, year)
    year += 1
    results.append(writeDoc(peopleDictionary, year))
    
    
print(str(writeDoc(peopleDictionary, year)))
print(results)

with open('Data/Data.json', 'w', encoding='utf-8') as f:
    json.dump(results, f, ensure_ascii=False, indent=4)
