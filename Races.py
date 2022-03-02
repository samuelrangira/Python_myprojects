#Samuel Rangira
#11/18/2021

import random

race = input("What race do you want your character to be? (human/elf/halforc/gnome)")
class Character:#creating classes with different characters
     def __init__(self,name,age,height,weight):# defines character's attributes
          self.name = name
          self.age = age
          self.height = height
          self.weight = weight
          self.race = "Human"
          self.intel = random.randint(8,18)
          self.strength = random.randint(8,18)
          self.dex = random.randint(8,18)
          self.wis = random.randint(8,18)
          self.con = random.randint(8,18)
          self.char = random.randint(8,18)
     def getName(self):
          return(self.name)
     def getAge(self):
          return(self.age)
     
     def getHeight(self):
          return(self.height)
          
     def getWeight(self):
          return(self.Weight)
     def getRace(self):
          return(self.race)
     def getInt(self):
          return(self.intel)
     
     def getStr(self):
          return(self.strength)
     def getDex(self):
          return(self.dex)
     def getWis(self):
          return(self.wis)
     
     def getCon(self):
          return(self.con)
     def getChar(self):
          return(self.char)
     def display(self):
          print("---------------------")
          print("Name : ", self.name)
          print("Race : ", self.race)
          print("Age : ", self.age)
          print("Height : ", self.height)
          print("Weight : ", self.weight)
          print("Int : ", self.intel)
          print("Str : ", self.strength)
          print("Dex : ", self.dex)
          print("Wis : ", self.wis)
          print("Con : ", self.con)
          print("Char : ", self.char)
class Elf(Character):#creating the function for Elf race 
     def __init__(self,name,age,height,weight):
          self.name = name
          self.age = age
          self.height = height
          self.weight = weight
          self.race = "Elf"
          self.intel = random.randint(8,18)
          self.strength = random.randint(8,18)
          self.dex = random.randint(8,18)+2
          self.wis = random.randint(8,18)
          self.con = random.randint(8,18)
          self.char = random.randint(8,18)
     def hasBow(self):
          print("Has a bow")
class HalfOrc(Character):#creating the function for halforc race
     def __init__(self,name,age,height,weight):
          self.name = name
          self.age = age
          self.height = height
          self.weight = weight
          self.race = "HalfOrc"
          self.intel = random.randint(8,18)
          self.strength = random.randint(8,18)+2
          self.dex = random.randint(8,18)
          self.wis = random.randint(8,18)
          self.con = random.randint(8,18)
          self.char = random.randint(8,18)
     def hasAxe(self):
          print("Has an axe")
class gnome(Character):#creating the funciton for gnome race
    def __init__(self,name,age,height,weight):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight
        self.race = "gnome"
        self.intel = random.randint(8,18)
        self.strength = random.randint(8,18)+2
        self.dex = random.randint(8,18)
        self.wis = random.randint(8,18)
        self.con = random.randint(8,18)
        self.char = random.randint(8,18)
    def hastrowel(self):
          print("Has an axe")

#if conditions/statements for different races
if race == "human":
    a = input("What is your character's name?")
    b = input("What is your character's age?")
    c = input("What is your character's height?")
    d = input("What i your character's weight?")
    
    C = Character(a,b,c,d)
    C.display()# displays character's attributes after putting in inputs

elif race =="elf":
    a = input("What is your character's name?")
    b = input("What is your character's age?")
    c = input("What is your character's height?")
    d = input("What i your character's weight?")
    C2 = Elf(a,b,c,d)
    C2.display()# displays character's attributes after putting in inputs
    C2.hasBow()
elif race =="halforc":
    a = input("What is your character's name?")
    b = input("What is your character's age?")
    c = input("What is your character's height?")
    d = input("What i your character's weight?")
    C3= HalfOrc (a,b,c,d)
    C3.display()# displays character's attributes after putting in inputs
    C3.hasAxe()

elif race =="gnome":
    a = input("What is your character's name?")
    b = input("What is your character's age?")
    c = input("What is your character's height?")
    d = input("What i your character's weight?")
    C4 = gnome(a,b,c,d)
    C4.display()# displays character's attributes after putting in inputs
    C4.hastrowel()

    





    
