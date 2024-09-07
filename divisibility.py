# This program asks for an integer and checks its divisibility with the numbers 2, 3, and 5.
# The output must be (x) is divisible by 2, 3, 5, or none at all.

divisibleby = []

def divisibility(x):
  if(x%2 == 0):
    divisibleby.append("2")
  if(x%3 == 0):
    divisibleby.append("3")
  if(x%5 == 0):
    divisibleby.append("5")
  if(len(divisibleby) == 0):
    print(x,"is neither divisible by 2, 3, nor 5.")
  elif(len(divisibleby) != 0):
    print(x, "is divisible by", ", and ".join(divisibleby))
  else:
    print(x, "is divisible by 2, 3, and 5")



x = int(input("Insert Integer: "))

divisibility(x)
