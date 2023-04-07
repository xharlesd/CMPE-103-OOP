# import modules
import pyfiglet
import colorama
from colorama import Fore, Style
import time

# Create a try-again function to use the program again if the user wants to 
def try_again():
    retry = None
    while retry is None:
        time.sleep(1)
        again = input(Fore.MAGENTA + "\n\t\t\tDo you want to try again? (YES/NO)  ")
        # the program will run again
        if again == "Y" or again == "Yes" or again == "YES" or again == "yes":
            retry = str(again)
            continue
        # the program will stop
        if again == "N" or again == "No" or again == "NO" or again == "no":
            time.sleep(0.5)
            print(Fore.GREEN + "\t\t\t[Program will be terminated..............]")
            time.sleep(1.5)
            print("\n")
            print("\033[0;34m" + "\033[1m-" * 140 + '\033[0m')
            print(" ")
            lab = pyfiglet.figlet_format("   THANK YOU !!   ", font = "banner3",  width = 140, justify = "center")
            print(Style.BRIGHT + Fore.CYAN + lab)
            exit()
        else:
            print(Fore.RED + "\t\t\t[ERROR] Please choose either YES or NO only.")


# Use pyfiglet formatting to "Lab. Exercise No. 1"
print("")
lab = pyfiglet.figlet_format("LAB EXERCISE # 1", font = "banner3-d", width = 141, justify = "center")
print(Style.BRIGHT + Fore.CYAN + lab)

# format introductory message
print("\033[0;34m" + "\033[1m-" * 140 + '\033[0m')
intro = "THIS DECRYPTION PROGRAM WILL ACCEPT A STRING AS ENCRYPTED TEXT AND THEN THE PROGRAM WILL DECRYPT IT." 
intro_centered = intro.center(140)
print( "\033[1m" + intro_centered) 
print("\033[0;34m" + "\033[1m-" * 140 + '\033[0m')

# insert time delay
time.sleep(1.5)

while True:
    #  ask user to input the encrypted text
    encrypted_string = input(Fore.CYAN + "\033[1m\n\t\t\tENCRYPTED TEXT: \033[0m" + Fore.YELLOW)

    # replace each character ( '* to a', '& to e', '# to i', '+ to o', '! to u' )
    decrypted_string = encrypted_string.replace('*', 'a').replace('&', 'e').replace('#', 'i').replace('+', 'o').replace('!', 'u')
    time.sleep(0.5)
    print(Fore.GREEN + "\t\t\t[Decrypting..............................]")
    time.sleep(2.5)

    # display decrypted text
    print(Fore.CYAN + "\033[1m\n\t\t\tDECRYPTED TEXT: \033[0m" + Fore.YELLOW + decrypted_string)
    print(Fore.GREEN + "\t\t\t[Decryption Successful...................]")

    try_again()

    # th& q!#ck br+wn f+x j!mps +v&r th& l*zy d+g