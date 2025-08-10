import sys, time, os
from termcolor import colored
import consts, functions

def clear_screen():
    if os.name == 'nt':  # For Windows
        os.system('cls')
    else:  # For Unix-based systems (Linux, macOS)
        os.system('clear')

def option_selection():
    print("Choose between options-\n")
    print(consts.prompt_selection, "\n")

    choice = input(">>> ")
    clear_screen()

    if choice == "QUIT": sys.exit()

    try:
        for char in consts.mappings[choice.lower()]:
            print(char, end="", flush=True)
            time.sleep(0.006)
    except KeyError:
        print(functions.not_accepted(choice)+"\n")
        raise UserWarning

    time.sleep(1); clear_screen()

    match choice.lower():

        case "a":
            functions.case_alpha(); time.sleep(0.5)
            
        case "b":
            functions.case_beta(); time.sleep(0.5)

        case "c":
            functions.case_kappa(); time.sleep(0.5)

        case "d":
            functions.case_delta(); time.sleep(0.5)

        case "e":
            functions.case_epsilon(); time.sleep(0.5)

        case _:
            print(functions.not_accepted(choice)+"\n")
            raise UserWarning

print("\n"*4)
print(colored("Welcome to, ", "green"))
print(colored(consts.cool_text, (0, 200, 25), attrs=["blink"]) + "\n"*2)

time.sleep(1)
clear_screen()
time.sleep(0.2)

while True:
    clear_screen(); time.sleep(0.1)
    try:
        option_selection()
    except UserWarning: pass
    except:
        print("\n\n----------------------------\n")
        print(colored(consts.rand_error, "red"))
        input(); clear_screen()
    print("\n"*4)
    if input("\nPress enter to use this tool again, type anything to exit\n\n>>> "):
        clear_screen()
        break