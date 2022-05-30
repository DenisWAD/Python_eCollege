# Sample Question Mr.Bunty's Wild Ride
max_capacity = 5
current_capacity = 0
eligible = True
age_card = ""
total_rides = 0

age = 0

while eligible == True :
  current_capacity = int(input("How many people are already on the ride?"))

  # Check space on ride
  if current_capacity > max_capacity :
    print("Sorry, the ride is full!")
    eligible = False
    break

  # Check age of customer
  age = int(input("What age are you?"))
  if age < 12 :
    print("Sorry, you're too young for this ride")  
    eligible = False
  elif age > 17 :
    print("Enjoy your ride!")
    eligible = True
  else :
    age_card = str(input("Has the customer a valid age card?"))
    if age_card != "Y" :
      print("You must have a valid age card for this ride")
      eligible = False
    else :
      total_rides += 1
      print("Enjoy your ride! As a minor you can only ride the SpookyTrain a maximum of 3 times")
      print("This is ride number : ", total_rides)
      if total_rides == 3 :
        print("You are not allowed to ride anymore due to the risk of nausea")
      elif total_rides > 3 :
        print("You cannot ride anymore, max rides already taken")
        eligible = False
        break