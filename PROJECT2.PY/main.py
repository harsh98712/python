import random
n = random.randint(1,100)
a = -1
guesses = 0
while(a !=n):
 guesses +=1   
 a = int(input("Guess the number: "))
 if(a>n):
  print("number is lower")
 else:
  print("number is greater")

print(f"you have guesed the right number in {guesses} attempt")
