salary = int(input("Please enter your salary: "))
month = input("Please enter the month: ")
savings = int(input("Please enter the savings percentage : "))
rent = int(input("Please enter the rent percentage: "))
electricity = int(input("Please enter the electricity: "))
savingsamount = salary * savings / 100
rentamount = salary * rent /100
electricityamount = salary * electricity /100
print (savingsamount,rentamount,electricityamount)
totalsum = savingsamount + rentamount + electricityamount
print( totalsum)
remaining= salary - totalsum
print (remaining)
yearlyrent= rentamount * 12
print (yearlyrent)
yearlyelectricity = electricityamount * 12
print(yearlyelectricity)
squaredsalary = salary**2
print(squaredsalary)
extrasaving = int(input("please enter your extra saving: "))
amountleft = extrasaving / remaining
print (amountleft)