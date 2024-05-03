eName = input("Enter employee name: ")
date = int(input("Enetr joining date: "))
month = int(input("Enter joining month: "))
year = int(input("Enter joining year: "))
print("Employee name: " ,eName)
for i in range (2):
    if(date == 15 and month ==8) or (date == 26 and month ==1):
        date = date + 1
        continue
    print("Joining date: ",date,"/",month,"/",year)