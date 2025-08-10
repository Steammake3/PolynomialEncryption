from termcolor import colored, cprint
import msg_handling, time, random, lagrange

def not_accepted(choice):
    return (colored(f"The choice {choice} is not supported- Please try again", "red", attrs=["bold"]))

def case_alpha():
    text = input("Unformatted text- ")
    key = input("Unformatted key length- ")
    time.sleep(0.5)
    retval = msg_handling.MSG_Handler().minGF_calc(len(text), int(key))
    print("\nField size should be", colored(str(retval), "blue"), "to accomodate\n")

    if input("Would you also like to generate a key? (Y/N) - ").lower()[0]=="y":
        handler = msg_handling.MSG_Handler()
        handler.accommodate(0, retval) #Now the randkey will be printed and its a sussy oneliner
        cprint(handler.get_str_of_points([random.randint(0, retval-1) for useless in "+"*int(key)]), "blue")
    else:
        print("Thank you anyhow")

def case_beta():
    text = input("Unformatted text- ")
    size = int(input("Field size - "))
    time.sleep(0.5)

    handler = msg_handling.MSG_Handler()
    handler.accommodate(0, size)

    final = ""
    for i in range(len(text)):
        final += text[i]
        final += handler.BASE97[random.randint(0, handler.possibilities(handler.BASE97.index(text[i]))-1)]

    print("\nFormatted text is-\n", colored(final, "blue")+"\n")

def case_kappa():
    text = input("Formatted text- ")
    print("\nUnformatted text is\n" + colored(text[::2], "blue") + "\n")

def case_delta():
    cprint("WARNING - text and key must be formatted correctly; Otherwise, behavior will be entirely unexpected\n", color="red")
    time.sleep(1)
    text = input("Formatted text- ")
    key = input("Formatted key- ")
    handler = msg_handling.MSG_Handler()
    handler.accommodate(len(text)/2, len(key)/2)
    text = handler.get_points_of_str(text)
    key = handler.get_points_of_str(key)

    #Interpolation time
    field = handler.field
    k_off = len(text)+len(key)
    txt_points = [[field(x), text[x-k_off]] for x in range(k_off, len(text)+k_off)]
    t_off = len(txt_points)
    key_points = [[field(x+t_off), key[x]] for x in range(len(key))]

    interpolater = lagrange.Lagrange(handler.field)
    poly = interpolater.interpolate(key_points+txt_points)

    retvals = [poly.eval(f) for f in range(len(text))]
    print("The decrypted formatted text is,\n\n", colored(handler.get_str_of_points(retvals), "blue"))

    #Ask if should be unformatted
    if input("\n\nWOuld you like an unformatted version of the text? (Y/N) - ").lower()[0] == "y":
        for i in range(20):
            print("-", flush=True, end=""); time.sleep(0.01)
        print(""); cprint(handler.get_str_of_points(retvals)[::2], "blue")

def case_epsilon():
    cprint("WARNING - text and key must be formatted correctly; Otherwise, behavior will be entirely unexpected\n", color="red")
    time.sleep(1)

    #Input handling
    text = input("Formatted text- ")
    key = input("Formatted key- ")
    handler = msg_handling.MSG_Handler()
    handler.accommodate(len(text)/2, len(key)/2)
    text = handler.get_points_of_str(text)
    key = handler.get_points_of_str(key)

    #Interpolation time
    field = handler.field
    txt_points = [[field(x), text[x]] for x in range(len(text))]
    t_off = len(txt_points)
    key_points = [[field(x+t_off), key[x]] for x in range(len(key))]

    interpolater = lagrange.Lagrange(handler.field)
    poly = interpolater.interpolate(txt_points+key_points)

    retvals = [poly.eval(f) for f in range(len(text)+len(key), 2*len(text)+len(key))]
    cprint("The encrypted formatted text is,\n\n" + handler.get_str_of_points(retvals), "blue")