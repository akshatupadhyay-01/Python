import random 
number = random.randint(1,10)
while True:
  userInput = int(input("Guess a number between 1 to 10 :"))
  
  if userInput == number: 
      print("number is correct")
 
  elif 0<=number<=5 and 5<=userInput<=10:
    print("number is too far")
  elif 5<=number<=10 and 0<=userInput<=5:
    print("number is too far")
 
  elif 0<=number<=5 and 0<=userInput<=5:
      print("too close")
  elif 5<=number<=10 and 5<=userInput<=10:
      print("too close")
  elif(userInput!=number):
      print("wrong input")
  else:
    print("invalid input")
    break