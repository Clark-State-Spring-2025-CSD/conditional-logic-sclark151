#Updated 1 Feb 2025
#Create a program that will ask the user for a number between 1 and 12. You may assume the input is correct.
#After getting the number display which season it is. The ranges are:
#Spring: 3,4,5
#Summer: 6,7,8
#Fall: 9,10,11
#Winter 12,1,2
#Here is a sample output:
#What month is it? (1-12): 2
#The current season is Winter.
#For an extra 2 points, display the month as all. So the output becomes:
#What month is it? (1-12): 2
#The month is February and the current season is Winter.
#Remember to also complete the flowchart. It is strongly advised that you do the flowchart first,
#as this will help you write the code.

number = int(input("What month is it? (1-12): "))

season = "unknown"

if number > 2 and number < 6:
    season = "Spring"
elif number > 5 and number < 9:
    season = "Summer"
elif number > 8 and number < 12:
    season = "Fall"
elif number == 1 or number == 2 or number == 12:
    season = "Winter"
else:
    print("That is not a valid month.")
    
month = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

print(f"The month is {month[number - 1]} and the current season is {season}.")
