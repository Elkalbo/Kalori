#Ask todays date
print("Today's date? ")
#User input date
date = input()
#ask Breakfast calories
print("Breakfast calories? ")
#User input amount of calories
Bcalories = int(input())
#Ask lunch calories
print("Lunch calories? ")
#User input amount of calories
Lcalories = int(input())
#Ask dinner calories
print("Dinner calories? ")
#User input amount of calories
Dcalories = int(input())
#Ask snack calories
print("Snack calories? ")
#User input amount of calories
Scalories = int(input())
#Calculate calories 
sum = Bcalories + Lcalories + Dcalories + Scalories
#Printing date and total number of calories
print("Calorie content for"+date+":"+str(sum))