import pandas as pd
from datetime import datetime, timedelta


class Animal: # Create Animal class to store attributes for each animal
    def __init__(self,species,name,age):
        self.species = species
        self.name = name
        self.age = age

class Zoo:
    def __init__(self):
        self.animals = [] # This will hold data for animals in a list of lists
        self.creatures = {} # This will be a dictionary giving info on the number of each species of animal

    
    def add_animal(self,species,name,age):
        return self.animals.append([species,name,age]) # Adds animal data to the list


    def get_all_animals(self):
        for idx,val in enumerate(self.animals):
            return val # Returns every animal in the list

    def get_zoo_hours(self,opening_hours,closing_hours):
        o = datetime.strptime(opening_hours, '%H:%M').time()
        c = datetime.strptime(closing_hours, '%H:%M').time()
        self.hours = (o,c)
        # This function allows you to input opening abd closing times for the zoo
    
    def get_species_count(self):
        for animal_data in self.animals:
            self.creatures[animal_data[0]] = self.creatures.get(animal_data[0],0) + 1
        return self.creatures # Gives the number of each species

l = Animal('Lion','Barry',20)
e = Animal('Elephant','Tiana',15)
t = Animal('Tiger','Terry',7)
d = Animal('Dog','Dora',4)
c = Animal('Cat','Theo',11)

zoo = Zoo()
zoo.add_animal(l.species,l.name,l.age)
zoo.add_animal(e.species,e.name,e.age)
zoo.add_animal(t.species,t.name,t.age)
zoo.add_animal(d.species,d.name,d.age)
zoo.add_animal(c.species,c.name,c.age)

zoo.get_species_count()

# print(zoo.creatures)

def find_animal(instance,file):
    df = pd.read_csv(file)
    for idx,row in df.iterrows():
        instance.add_animal(row['species'],row['name'],row['age'])
    # Goes through every row and adds each animal to the list of zoo animals

find_animal(zoo,'animals.csv') 

# print(zoo.animals)

zoo.get_zoo_hours('09:00','17:00')

def time_arrival(instance,time):
    t = datetime.strptime(time, '%H:%M').time()
    if  instance.hours[0] <= t <=  instance.hours[1]: # If time is further in the day then the opening time and further back in the day than the closing time then the zoo is open.

        return print('Zoo is Open!')

    else:
       return print('Zoo is Closed')

# time_arrival(zoo,'13:00') 

def no_of_animals(instance):
    return len(instance.creatures.keys()) # Tells you the number of animals in the zoo by counting the number of animals added to the dictionary
    
def oldest(instance):
    oldest_age = 0
    oldest_animal = []
    for data in instance.animals:
        if data[2] > oldest_age:
            oldest_age = data[2]
            oldest_animal = data
        else:
            continue
    return oldest_animal # Gives the oldest animal in the Zoo

# print(oldest(zoo))

def combined(instance):
    total_age = 0
    for data in instance.animals:
        total_age += data[2]
    return total_age # Adds up the ages of all animals in the zoo

print(combined(zoo))

