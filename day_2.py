print("Welcome to the tip calculator.")
bill = float(input("How much was the total bill?\n"))
tip = int(input("How much would You like to tip 12, 15, or 20?\n"))
split = int(input("How many people were dining with you?\n"))
Bill_Total =  (tip / 100 + 1) * bill / split
Final_Bill = "{:.2f}".format(Bill_Total)
print(f"Each person should pay: ${Final_Bill}")
