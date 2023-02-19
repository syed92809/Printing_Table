# Printing Table No 2


count=1
for i in range (2,21,2):
    print("2 *",count,"=",i)
    count=count+1
print("-----------print any table--------------")
print()


# printing Table according to user input

inputCount=1
tableNumber = int(input("Enter Table Number You Want To Print:"))
convertTableInput=str(tableNumber)

for i in range(tableNumber,tableNumber*10+1,tableNumber):
    print(tableNumber,"*",inputCount,"=",i)
    inputCount=inputCount+1