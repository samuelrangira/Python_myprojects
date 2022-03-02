#Samuel Rangira
#10/14/2021

phonebook = {}
 #creating the key without vallues initially
flag = True
while(flag):
# loops through the conditions as long as flag holds true
    bar = input("what would you like to do? (add/look up/quit) > ")
#generating inputs
    if (bar == 'add'):
          name = input("What is the person's name?")
          phone = input("What is their phone number?")
          phonebook[name] = phone
    elif (bar == 'look up'):
        name = input("Who do you want to look up?")
        print(name + "'s number is", phonebook[name])
    elif (bar == 'quit'):
        print("good by!")
        flag = False
    else:
        print("I am sorry. I do not recognize that input. ")
    


