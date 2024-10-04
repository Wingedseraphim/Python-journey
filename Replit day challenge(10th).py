print("Tip calculator")
print( )
print( )
totalBill = float(input("how much did you spend?"))
tipPercentage = float(input("what percentage do you want to tip?"))
tip = totalBill + tipPercentage
tip = round(tip, 2)
totalGuests = int(input("how many people in your group?"))
overallTip = tip / totalGuests

print("you owe $", overallTip)

