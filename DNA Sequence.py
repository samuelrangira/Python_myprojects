#Samuel Rangira
#10/01/2021
DNA_sequence = input("write your DNA sequence here:")
weight = 0
code = " "
for i in range (0, len(DNA_sequence), 3):
    x = DNA_sequence[i:i+3]
    
    if x == "ATT" or x == "ATC" or x == "ATA":
        code += "I"
        weight+= 131.2
    elif x == "ACT" or x == "ACC" or x == "ACA" or x == "ACG":
        code += "T"
        weight+= 119.1
    elif x == "AAT" or x == "AAC":
        code += "N"
        weight+= 132.1

print("The three letter code is: ", code)
print("The weight of the sequence is: ", weight)
        



        
    
    

    
