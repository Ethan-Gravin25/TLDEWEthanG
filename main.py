from Week0 import Animation
from Week0.christmastree import Tree
from Week1 import infoDB
from Week2 import math

main_menu = []

w0_list = [["Swap", "Swap.py"], ["Matrix", "Matrix.py"],
           ["Christmas Tree", Tree],
           ["Animation", Animation.ship]]

w1_list = [["InfoDB Loops", infoDB.InfoDb_loops],
           ["Fibonacci", infoDB.output_fibonacci]]

w2_list = [["Factorial", math.factorial], ["Math", math.square]]

border = "=" * 25
banner = f"\n{border}\nPlease Select An Option\n{border}"


def menu():
    title = "Function Menu" + banner
    menu_list = main_menu.copy()
    menu_list.append(["Week 0", w0_func])
    menu_list.append(["Week 1", w1_func])
    menu_list.append(["Week 2", w2_func])
    buildMenu(title, menu_list)


def w0_func():
    title = "Week 0" + banner
    buildMenu(title, w0_list)


def w1_func():
    title = "Week 1" + banner
    buildMenu(title, w1_list)


def w2_func():
    title = "Week 2" + banner
    buildMenu(title, w2_list)


def buildMenu(banner, options):
    print(banner)
    prompts = {0: ["Exit", None]}
    for op in options:
        index = len(prompts)
        prompts[index] = op

    for key, value in prompts.items():
        print(key, '->', value[0])

    choice = input("Type your choice: ")

    try:
        choice = int(choice)
        if choice == 0:
            return
        try:
            action = prompts.get(choice)[1]
            action()
        except TypeError:
            try:
                exec(open(action).read())
            except FileNotFoundError:
                print(f"File not found!: {action}")
    except ValueError:
        print(f"Not a number: {choice}")
    except UnboundLocalError:
        print(f"Invalid choice: {choice}")
    except TypeError:
        print(f"Not callable {action}")

    buildMenu(banner, options)


if __name__ == "__main__":
    menu()
