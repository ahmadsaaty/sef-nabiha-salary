salary = int(input("Nabiha, Please enter your salary: "))
month = input("Nabiha, Please enter the name of the month of your salary: ")
savings = int(input("Nabiha, Please enter the savings percentage : "))
rent = int(input("Nabiha, Please enter the rent percentage: "))
electricity = int(input("Nabiha, Please enter the electricity percentage: "))

savingsamount = salary * savings // 100
print("Nabiha, your savings value is: " + str(savingsamount) + "$$$")

rentamount = salary * rent // 100
print("Nabiha, your rent value is: " + str(rentamount) + "$$$")

electricityamount = salary * electricity // 100
print("Nabiha, your electricity value is: " + str(electricityamount) + "$$$")

totalsum = savingsamount + rentamount + electricityamount
print("Nabiha, your total sum of expenses is: " + str(totalsum) + "$$$")

remaining= salary - totalsum
print("Nabiha, the remainder of your salary after these expenses is: " + str(remaining) + "$$$")

yearlyrent= rentamount * 12
print("Nabiha, your yearly rent value is: " + str(yearlyrent) + "$$$")

yearlyelectricity = electricityamount * 12
print("Nabiha, your yearly electricity value is: " + str(yearlyelectricity+yearlyrent   ) + "$$$")

print("Nabiha, your yearly rent and electricity expenses are: " + str(yearlyelectricity) + "$$$")

squaredsalary = salary**2
print("Nabiha, your squared salary fun value is: " + str(squaredsalary) + "$$$")

extrasaving = int(input("Nabiha, please enter your extra saving: "))
amountleft = extrasaving / savingsamount
print("Nabiha, your extra savings ratio is: " + str(amountleft))