#Samuel Rangira
#9/15/2021

#Getting inputs

adjective = input("Enter an adjective")
name = input("Enter a name")
number = int(input("Enter a number"))
another_number = int(input("Enter another number"))
different_name = input("Enter a different name")
count = input("Enter how many fled")
town_name = input("Enter a town_name")
different_town = input("Enter a different_town")
verb = input("Enter a verb ending in -ing")
another_adjective = input("Enter another adjective")


#Displaying inputs or getting outputs to form a complete madlib

print("A new and " + adjective.lower() + " fairy princess movie is coming out soon! \n")
print("It will be about " + name.capitalize() + " and the " + str(number + another_number) + " dwarfs. \n")
print( name.capitalize() + " is a princess whose beauty threatens " + different_name.capitalize() + ", \n")
print("the queen. The " + count + " of them are forced to flee from " + town_name.capitalize() + "\n")
print("and hide in nearby " + different_town.capitalize() + " by " + verb.lower() + ". Eventually, the queen finds " + name.capitalize() + "\n")
print("and casts a " + another_adjective.lower() + " spell on her.")


      

