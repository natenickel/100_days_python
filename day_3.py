print("Welcome to the rollercoaster")
height = int(input("what is your height in CM? "))
ticket = False
bill = 0

if height >= 120 :
  age = int(input("You are tall enough to ride. How old are you "))
  if age < 12 :
    buying = input("Kids tickets will be $5")
    bill = 5
  elif age <= 18:
    buying = input("Youth tickets will be $7")
    bill = 7
  else: 
    if age > 45 & age < 55:
        buying = input("Your Ticket is on us!")
        bill = 0
    else: 
        input("Adult tickets will be $10")
        bill = 10

  wants_photo = input("Would you like to have your photo taken? Y or N\n")
  if wants_photo == "Y":
    bill += 3
  print(f"Your final bill will be ${bill}")

    
else:
  print("Sorry, you cant ride") 
 