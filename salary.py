salary = int(input("Nabiha, Please enter your salary: "))
month = input("Nabiha, Please enter the name of the month of your salary: ")
savings = int(input("Nabiha, Please enter the savings percentage : "))
rent = int(input("Nabiha, Please enter the rent percentage: "))
electricity = int(input("Nabiha, Please enter the electricity percentage: "))

#The amount allocated to savings, rent, and electricity.
savingsamount = salary * savings // 100
print("Nabiha, your savings value is: " + str(savingsamount) + "$$$") 

rentamount = salary * rent // 100
print("Nabiha, your rent value is: " + str(rentamount) + "$$$")

electricityamount = salary * electricity // 100
print("Nabiha, your electricity value is: " + str(electricityamount) + "$$$")

#The total amount Nabiha spends on savings, rent, and electricity combined.
totalsum = savingsamount + rentamount + electricityamount
print("Nabiha, your total sum of expenses is: " + str(totalsum) + "$$$")

# The remainder of Nabiha’s salary after these expenses.
remaining= salary - totalsum
print("Nabiha, the remainder of your salary after these expenses is: " + str(remaining) + "$$$")

# The monthly rent and electricity multiplied by 12 to estimate Nabiha's yearly rent and electricity costs.
yearlyrent= rentamount * 12
print("Nabiha, your yearly rent value is: " + str(yearlyrent) + "$$$")

yearlyelectricity = electricityamount * 12
print("Nabiha, your yearly electricity value is: " + str(yearlyelectricity+yearlyrent   ) + "$$$")

print("Nabiha, your yearly rent and electricity expenses are: " + str(yearlyelectricity) + "$$$")

# Nabiha's total salary for the month raised to the power of 2 (just for fun).
squaredsalary = salary**2
print("Nabiha, your squared salary fun value is: " + str(squaredsalary) + "$$$")

# Assume Nabiha saves an additional random amount (e.g., $50) each month, 
# and you need to calculate how much would be left if this amount is divided by the total amount 
# allocated to savings. 
extrasaving = int(input("Nabiha, please enter your extra saving: "))
amountleft = extrasaving / savingsamount
print("Nabiha, your extra savings ratio is: " + str(amountleft))

#print a fun message to Nabiha
print("Nabiha, you're gonna be rich")