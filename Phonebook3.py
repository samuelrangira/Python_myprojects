#Samuel Rangira
#12/15/2021

A = open("breedingphonebook.txt","r")

lines = A.readlines()# save file as a list 


breedingphonebook = {} 
for i in lines:
    i = i.split(",")
    temp = i[1]
    breedingphonebook[i[0]] = temp[:-1]
A.close() 

flag = True
while(flag):# function loops as long as our condition (flag) is no longer true/is false

    # inputs for our function
    foo = input("Tell me what you want. (add breeding kind/look up kind/quit) > ")

    if (foo == 'add breeding kind'):
          breed=input("What kind of crop breeding do you want to add? ")
          Advantage = input("What is its advantage? ")
          breedingphonebook[breed] = Advantage
    elif (foo == 'look up kind'):
        breed = input("which kind of plant breeding do you want to look up? ")
        print(breedingphonebook[breed], "is one the benefits of " + breed)
    elif (foo == 'quit'):
        print("good bye!")
        flag = False # stop looking when flag is false or when function receives input 'quit' 
    else:
        print("Invalid input! Please try again. ")
    


A = open("breedingphonebook.txt", "w")# opens the file and makes it possible to write in more keys and values
for i in breedingphonebook:
    A.write(i + "," + breedingphonebook[i] + "\n")
A.close()


