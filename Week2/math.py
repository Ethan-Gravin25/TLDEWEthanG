# Factorial of a number using recursion
def recur_factorial(n):
  if n == 1 or n == 0:
    return 1
  else:
    num = n * recur_factorial(n-1)
    return num

# this is test driver or code that plays when executed directly, versus import which will not run these statements
def factorial():
  num = int(input("Enter number to find factorial of: "))
  # check if the number is negative
  if num < 0:
      print("Sorry, factorial doesn't exist for negative numbers.")
  else:
      print("The factorial of", num, "is", recur_factorial(num))

# Math Function
def square():
  num = int(input("Enter number to find square of: "))
  print("Imperative: The squared value of", num, "is", func_square(num))
  obj = squared(num)
  s = obj.findsquare()
  print("OOP: Squared value of", num, "is", s)

def func_square(n):
  num = n * n
  return num

class squared():
  def __init__(self,num):
    self.num=num
  def findsquare(self):
    s = self.num * self.num
    return s