# import random
#define needed input values

#check if the salary is an integer
while True:
    salary =input("Nabiha, Please enter your salary: ")
    try:
        salary= int(salary)
        break
    except ValueError:
        print("The salary should be an integer!!!")

#check if the month is entered correctly (a string from the given list )
while True:          
    month = input("Nabiha, Please enter the name of the month of your salary: ")
    monthlist = ["january","february","march","april","may","june","july","august","september","october","november","december"]
    try:
        month= int(month)
        print(f"{month} is not a month, enter name correctly")
    
    except ValueError:
        
        if month.lower() in monthlist :
            print(month.capitalize() + " is the best month in the year")
            break
        else:
            print(f"{month} is not a month, enter name correctly from the following list: {monthlist}")
            print(f" Enter month from the following list: {monthlist}")

index = monthlist.index(month)             
print (int(index) +1)
remainingmonths = 11 - int(index)
print(remainingmonths)
#check if the savings is an integer
# while True:
#     savings = input("Nabiha, Please enter the savings percentage : ")
#     try:
#         savings = int(savings)
#         if 0<= savings <=100 :
#             break
#         else:
#             print("The savings percentage should be an integer between 0 and 100!!!")
#     except ValueError:
#         print ("The savings percentage should be an integer between 0 and 100!!!")


# #check if the rent is an integer
# while True:
#     rent = input("Nabiha, Please enter the rent percentage : ")
#     try:
#         rent = int(rent)
#         if 0<= rent <=100 :
#             break
#         else:
#             print("The rent percentage should be an integer between 0 and 100!!!")
#     except ValueError:
#         print ("The rent percentage should be an integer between 0 and 100!!!")

# #check if the electricity is an integer
# while True:
#     electricity = input("Nabiha, Please enter the electricity percentage : ")
#     try:
#         electricity = int(electricity)
#         if 0<= electricity <=100 :
#             break
#         else:
#             print("The electricity percentage should be an integer between 0 and 100!!!")
#     except ValueError:
#         print ("The electricity percentage should be an integer between 0 and 100!!!")        

# totalpercentage= savings+rent + electricity
# print (totalpercentage)
# if totalpercentage >100 :
#     print("the sum of percentages should be less than 100")


#check if sum of percentages is less or equal to 100
while True:  
#check if the savings is an integer

    while True:
        savings = input("Nabiha, Please enter the savings percentage : ")
        try:
            savings = int(savings)
            if 0<= savings <=100 :
                break
            else:
                print("The savings percentage should be an integer between 0 and 100!!!")
        except ValueError:
            print ("The savings percentage should be an integer between 0 and 100!!!")


#check if the rent is an integer
    while True:
        rent = input("Nabiha, Please enter the rent percentage : ")
        try:
            rent = int(rent)
            if 0<= rent <=100 :
                break
            else:
                print("The rent percentage should be an integer between 0 and 100!!!")
        except ValueError:
            print ("The rent percentage should be an integer between 0 and 100!!!")

#check if the electricity is an integer
    while True:
        electricity = input("Nabiha, Please enter the electricity percentage : ")
        try:
            electricity = int(electricity)
            if 0<= electricity <=100 :
                break
            else:
                print("The electricity percentage should be an integer between 0 and 100!!!")
        except ValueError:
            print ("The electricity percentage should be an integer between 0 and 100!!!")        

    totalpercentage= savings+rent + electricity
    
    if totalpercentage > 100 :
        print(f"The sum of percentages is {totalpercentage},but it should be less than 100, please re-enter the values: ")
    else:
        break
    


    #The amount allocated to savings, rent, and electricity.
savingsamount = salary * savings // 100
print("Nabiha, your savings value is: " + str(savingsamount) + " $") 

rentamount = salary * rent // 100
print("Nabiha, your rent value is: " + str(rentamount) + " $")

electricityamount = salary * electricity // 100
print("Nabiha, your electricity value is: " + str(electricityamount) + " $")

#The total amount Nabiha spends on savings, rent, and electricity combined.
totalsum = savingsamount + rentamount + electricityamount
print("Nabiha, your total sum of expenses is: " + str(totalsum) + " $")

# The remainder of Nabiha’s salary after these expenses.
remaining = salary - totalsum
print("Nabiha, the remainder of your salary after these expenses is: " + str(remaining) + " $")

# The monthly rent and electricity multiplied by 12 to estimate Nabiha's yearly rent and electricity costs.
yearlyrent= rentamount * 12
print("Nabiha, your yearly rent value is: " + str(yearlyrent) + " $")

yearlyelectricity = electricityamount * 12
print("Nabiha, your yearly electricity value is: " + str(yearlyelectricity) + " $")

print("Nabiha, your yearly rent and electricity expenses are: " + str(yearlyelectricity+yearlyrent) + " $")

# Nabiha's total salary for the month raised to the power of 2 (just for fun).
squaredsalary = salary**2
print("Nabiha, your squared salary fun value is: " + str(squaredsalary) + " $$")

# Assume Nabiha saves an additional random amount (e.g., $50) each month, 
# and you need to calculate how much would be left if this amount is divided by the total amount 
# allocated to savings. 
# extra = random.randint(0,100)
# print(extra)
extrasaving = int(input("Nabiha, please enter your extra saving: "))
amountleft = extrasaving + savingsamount
print(f"Nabiha, if we add an additional {extrasaving}$ each month, your savings will be: {amountleft} $")
# print(f"Your total savings till the end of the year will be: {amountleft*12} $")
print(f"The remaining months till the end of this year is {remainingmonths} months")
print(f"Your total savings till the end of the year will be {amountleft*remainingmonths} $")
#print a fun message to Nabiha
print("Nabiha, you're gonna be rich")