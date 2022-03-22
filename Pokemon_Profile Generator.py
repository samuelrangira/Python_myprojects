#Samuel Rangira
#10/21/2021

f = open("Pokemon.txt","r")
lines = f.readlines()

pokemon = {}#saves by ID
pokemon2 = {}#saves by name
for i in lines:
    i = i.split(",")
    pokemon[i[0]] = {}
    pokedex = pokemon[i[0]]
    #print(pokedex)
    pokedex["name"] = i[1]
    pokedex["height"] = i[3]
    pokedex["weight"] = i[4]
    

for i in lines:
    i = i.split(",")
    pokemon2[i[1]] = {}
    pokedex = pokemon2[i[1]]
    pokedex["ID"]= i[2]
    pokedex["height"] = i[3]
    pokedex["weight"] = i[4]


foo = input("look up by name, number or print all?(name, number, all)")

#generating inputs

if foo== "number":
    bar= input("Please enter the pokemon's number you want to look up:")
    print(pokemon[bar])
    y = pokemon[bar]
    print("Name = " + y["name"])
    print("Height  = " + y["height"])
    print("Weight = " + y["weight"])
    
if foo == "name":
    bar = input("Please enter the pokemon's name you want to look up:")
    x = pokemon2[bar]
    print("ID = ", x["ID"])
    print("Height = " + x["height"])
    print("Weight = " + x["weight"])
    
    
if foo == "all":
    #printing the dictionary
    for key in pokemon.keys():#gets each "key"/pokedex name from the dictionary
         foo = pokemon[key]
         for values in foo:
              print(values, "=", foo[values])#prints the value of the values  


flag = True 
while flag:#executes the function as long as flag(condition) is true 
    x = input("Do you want to exit?(y/n)")
    if x == "n":
        foo = input("look up by name, number or print all?(name, number, all)")
        if foo== "number":
            bar= input("Please enter the pokemon's number you want to look up:")
            print(pokemon[bar])
            y = pokemon[bar]
            print("Name = " + y["name"])
            print("Height  = " + y["height"])
            print("Weight = " + y["weight"])
    
        if foo == "name":
            bar = input("Please enter the pokemon's name you want to look up:")
            x = pokemon2[bar]
            print("ID = ", x["ID"])
            print("Height = " + x["height"])
            print("Weight = " + x["weight"])
            
    
        if foo == "all":
            #printing the dictionary
            for key in pokemon.keys():#gets each "key"/pokedex name from the dictionary
                 foo = pokemon[key]
                 for values in foo:
                      print(values, "=", foo[values])#prints the value of the values  

    if x == "y":
        flag = False #stops the function from running/looping again
        

    

