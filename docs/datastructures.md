{% include navigation.html %}

# Data Structure
## <a href="https://github.com/Ethan-Gravin25/TLDEW"> Github Link</a>
## <a href="https://github.com/Ethan-Gravin25/TLDEWEthanG/blob/main/reviewtickets.md"> Review Ticket</a>

## Accounts and Login
Crud Stuff

Hack 1
![image](https://user-images.githubusercontent.com/89223558/162492416-822de6b9-4453-4f65-ac78-d01e7740c26e.png)
![image](https://user-images.githubusercontent.com/89223558/162492371-d59773c8-6662-4949-a681-cd47d9a2d76b.png)

Hack 2
![image](https://user-images.githubusercontent.com/89223558/163854263-f001143b-57ea-4153-9361-17faaf184b8e.png)

Hack 3
![image](https://user-images.githubusercontent.com/89223558/162492736-3de91ac8-51c7-4247-9e63-656a6cef6ea5.png)


<iframe frameborder="0" width="100%" height="800px" src="https://replit.com/@Ethan-Gravin25/practice-stuff?embed=true">

# Code
## TT0
### Menu
````
# menuy.py - function style menu
# Imports typically listed at top
# each import enables us to use logic that has been abstracted to other files and folders
import Animation

# Main list of [Prompts, Actions]
# Two styles are supported to execute abstracted logic
# 1. file names will be run by exec(open("filename.py").read())
# 2. function references will be executed directly file.function()
main_menu = [
    ["Swap", "Swap.py"],
    ["Matrix", "Matrix.py"], 
    ["Tree", "Tree.py"],
    ["Animation", Animation.ship],
]

# Submenu list of [Prompt, Action]
# Works similarly to main_menu
sub_menu = [
    ["Factors", None],
    ["GCD", None],
    ["LCM", None],
    ["Primes", None],
]

random_sub_menu = [
    ["Random1", None],
    ["Random2", None],
    ["Random3", None],
]

# Menu banner is typically defined by menu owner
border = "=" * 25
banner = f"\n{border}\nPlease Select An Option\n{border}"


# def menu
# using main_menu list:
# 1. main menu and submenu reference are created [Prompts, Actions]
# 2. menu_list is sent as parameter to menuy.menu function that has logic for menu control
def menu():
    title = "Function Menu" + banner
    menu_list = main_menu.copy()
    buildMenu(title, menu_list)

# def submenu
# using sub menu list above:
# sub_menu works similarly to menu()
def submenu():
    title = "Function Submenu" + banner
    buildMenu(title, sub_menu)
def Random_submenu():
    title = "Function Submenu" + banner
    buildMenu(title, random_sub_menu)

def buildMenu(banner, options):
    # header for menu
    print(banner)
    # build a dictionary from options
    prompts = {0: ["Exit", None]}
    for op in options:
        index = len(prompts)
        prompts[index] = op

    # print menu or dictionary
    for key, value in prompts.items():
        print(key, '->', value[0])

    # get user choice
    choice = input("Type your choice> ")

    # validate choice and run
    # execute selection
    # convert to number
    try:
        choice = int(choice)
        if choice == 0:
            # stop
            return
        try:
            # try as function
            action = prompts.get(choice)[1]
            action()
        except TypeError:
            try:  # try as playground style
                exec(open(action).read())
            except FileNotFoundError:
                print(f"File not found!: {action}")
            # end function try
        # end prompts try
    except ValueError:
        # not a number error
        print(f"Not a number: {choice}")
    except UnboundLocalError:
        # traps all other errors
        print(f"Invalid choice: {choice}")
    except TypeError:
        print(f"Not callable {action}")
    # end validation try

    buildMenu(banner, options)  # recursion, start menu over again


if __name__ == "__main__":
    menu()
````
### Tree
````
print("Christmas Tree")
#tree
tree = [("        ","*"," "),
        ("       ","* *"," "),
        ("      ","* * *"," "),
        ("     ","* * * *"," "),
        ("    ","* * * * *"," "),
        ("   ","* * * * * *"," "),
        ("  ","* * * * * * *"," "),
        (" ","* * * * * * * *"," "),
        ("","* * * * * * * * *"," "),
        ("       ","***"," "),
        ("       ","***"," "),
        ("       ","***"," "),
  ]
for x in tree:
    for y in x:
        print(y, end = " ")
    print()
````
### Animation
````
import time

# terminal print commands
ANSI_CLEAR_SCREEN = u"\u001B[2J"
ANSI_HOME_CURSOR = u"\u001B[0;0H\u001B[2"
OCEAN_COLOR = u""
SHIP_COLOR = u"\u001B[32m\u001B[2D"
RESET_COLOR = u"\u001B[0m\u001B[2D"

def ocean_print():
    # print ocean
    print(ANSI_CLEAR_SCREEN, ANSI_HOME_CURSOR)
    print("\n\n\n\n")
    print(OCEAN_COLOR + "  " * 35)

# print ship with colors and leading spaces
def ship_print(position):
    print(ANSI_HOME_CURSOR)
    print(RESET_COLOR)
    sp = " " * position
    print(sp + " ───▄▄▄      ")
    print(sp + " ─▄▀░▄░▀▄    ")
    print(sp + " ─█░█▄▀░█    ")
    print(sp + " ─█░▀▄▄▀█▄█▄▀")
    print(sp + " ▄▄█▄▄▄▄███▀ ")
    print(RESET_COLOR)

# ship function, iterface into this file
def ship():
  ocean_print()
  # loop control variables
  start = 0  # start at zero
  distance = 50  # how many times to repeat
  step = 1  # count by 2

  # loop purpose is to animate ship sailing
  for position in range(start, distance, step):
      ship_print(position)  # call to function with parameter
      time.sleep(.1)

ship()
````
### InfoDB Loops
````
# List with dictionary records placed in a list  
InfoDb.append({  
               "FirstName": "Ethan",  
               "LastName": "Gravin",  
               "DOB": "April 10",  
               "Residence": "San Diego",  
               "Favorite_Colors":["Red","Purple"]  
              })  

InfoDb.append({  
               "FirstName": "Morgan",  
               "LastName": "Gravin",  
               "DOB": "May 29",  
               "Residence": "San Diego",   
               "Favorite_Colors":["Green"] 
              })  

# given an index this will print InfoDb content
def print_data(n):
    print(InfoDb[n]["FirstName"], InfoDb[n]["LastName"])  # using comma puts space between values
    print("\t", "Favorite_Colors: ", end="")  # \t is a tab indent, end="" make sure no return occurs
    print(", ".join(InfoDb[n]["Favorite_Colors"]))  # join allows printing a string list with separator
    print()

# Hack 2: InfoDB loops. Print values from the lists using three different ways: for, while, recursion

  # hack 2a: def for_loop()
# for loop iterates on length of InfoDb
def for_loop():
  for n in range(len(InfoDb)):
      print_data(n)

    
  # hack 2b: def while_loop(0)
# while loop contains an initial n and an index incrementing statement (n += 1)
def while_loop(n):
  while n < len(InfoDb):
      print_data(n)
      n += 1
  return

  # hack 2c : def recursive_loop(0)
# recursion simulates loop incrementing on each call (n + 1) until exit condition is met
def recursive_loop(n):
  if n < len(InfoDb):
      print_data(n)
      recursive_loop(n + 1)
  return # exit condition

def InfoDb_loops():
  print()
  print("For loop:")
  for_loop()
  print("While loop:")
  while_loop(0)  # requires initial index to start while
  print("Recursive loop:")
  recursive_loop(0)  # requires initial index to start recursion
````
### Factorial
````
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
````
### Fibonacci
````         
# Hack 3: Fibonacci.  Write a recursive program to create a fibonacci sequence including error handling(with try/except) for invalid input

def fibonacci(n):  
  if n < 0:
    print("Please enter a positive integer")
  elif n == 0:
    return 0
  elif n == 1 or n == 2:
    return 1
  elif n > 20:
    print("That's too many numbers, don't input over 20")
  else:  
    return(fibonacci(n-1) + fibonacci(n-2))  

def output_fibonacci():
  # take input from the user  
  nterms = int(input("How many terms would you like? "))  
  # check if the number of terms is valid  
  if nterms <= 0:  
     print("The Fibonacci sequence does not exist for negative numbers.")  
  else:  
     print("Your sequence:")
     for i in range(nterms):
         print(fibonacci(i), end=" ")
  print()
