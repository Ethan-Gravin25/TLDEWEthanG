{% include navigation.html %}

# Data Structure
## <a href="https://github.com/Ethan-Gravin25/TLDEW"> Github Link</a>
## <a href="https://replit.com/@Ethan-Gravin25"> Replit Link</a>
## <a href="https://github.com/Ethan-Gravin25/TLDEWEthanG/blob/main/reviewtickets.md"> Review Ticket</a>

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

