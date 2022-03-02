#Samuel Rangira
#10/01/2021


Income = int(input("Enter how much you made last year: "))#generating inputs
tax = 0
x = Income


if 0 < x <= 9950:# if statements for tax calculation
    tax+= x*(0.10)
elif 9951 < x <= 40525:
    tax += 995 + (x - 9950)*(0.12)
elif 40526 < x < 86376:
    tax += 4664 + (x - 40525)*(.22)
elif 86377 < x < 164925:
    tax+= 14751 + (86376 - 40526)*(.22) + (x - 86376)*(0.24)
elif 164926 < x < 209425:
    tax+= 33602.76 + (164925 - 86376)* 0.24 + (x - 164925)*(0.32)
elif 209426 < x < 523600:
    tax+= 47842.44  + (209425 -164926)*0.32 + (x - 209426)*(0.35)
elif x > 523601:
    tax+= 157804.25 + (x - 523601)*(0.37)

netx = x - tax


print("You owe: ", tax)#generating final tax owed 
print("Your net income is: ", netx)#generating the net income
