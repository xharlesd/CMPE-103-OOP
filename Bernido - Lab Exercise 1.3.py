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
        again = input(Fore.MAGENTA + "\n\t    Do you want to try again? (YES/NO)  ")
        # the program will run again
        if again == "Y" or again == "Yes" or again == "YES" or again == "yes":
            retry = str(again)
            main()
        # the program will stop
        if again == "N" or again == "No" or again == "NO" or again == "no":
            time.sleep(0.5)
            print(Fore.CYAN + "\t    [Program will be terminated..............]")
            time.sleep(1.5)
            print("\n")
            print(Fore.GREEN + "\033[1m-" * 140 + '\033[0m')
            print(" ")
            lab = pyfiglet.figlet_format("   THANK YOU !!   ", font = "banner3",  width = 140, justify = "center")
            print(Style.BRIGHT + Fore.GREEN + lab)
            exit()
        else:
            print(Fore.RED + "\t    [ERROR] Please choose either YES or NO only.")


letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def encrypt(key, message):
    cipher_text = []

    key_index = 0
    key = key.upper()

    for char in message: # Loop through each symbol in message.
        num = letters.find(char.upper())
        if num != -1: # -1 means symbol.upper() was not found in LETTERS.
            num += letters.find(key[key_index])
            num %= len(letters) 

            if char.isupper():
                cipher_text.append(letters[num])
                
            key_index += 1 # Move to the next letter in the key.
            if key_index == len(key):
                key_index = 0
        else:
            # Append the symbol without encrypting:
            cipher_text.append(char)

    return ''.join(cipher_text)


# Use pyfiglet formatting to "Lab. Exercise No. 1"
print("")
lab = pyfiglet.figlet_format("LAB EXERCISE # 1", font = "banner3-d", width = 141, justify = "center")
print("\033[1;32m" + lab)

# format introductory message
print(Fore.GREEN + "\033[1m-" * 140 + '\033[0m')
intro = "THIS ENCRYPTION PROGRAM WILL ACCEPT THE MESSAGE AND KEY FROM USER IN ORDER TO GENERATE CIPHER TEXT USING THE VIGENERE CIPHER." 
intro_centered = intro.center(140)
print( "\033[1m" + intro_centered) 
print(Fore.GREEN + "\033[1m-" * 140 + '\033[0m')

# time delay
time.sleep(1.5)

def main():
    while True:
        input_message = input(Fore.GREEN + "\033[1m" + "\n\t    ENTER PLAIN TEXT \033[0m" + "\033[0;32m(\033[4mALL UPPERCASE LETTERS, NO SPACES\033[0m\033[0;32m) :  " + Fore.YELLOW)
        time.sleep(0.5)
        input_key = input(Fore.GREEN + "\033[1m" + "\t    ENTER KEY \033[0m" + "\033[0;32m(\033[4mALL UPPERCASE LETTERS, NO SPACES\033[0m\033[0;32m) :  " + Fore.YELLOW)
        time.sleep(0.5)

        if input_message.islower() or not input_message.isalpha():
            print(Fore.RED + "\t    [ERROR] Message and Key should be in uppercase letters and should not contain spaces.")
            try_again()
        elif input_key.islower() or not input_key.isalpha():
            print(Fore.RED + "\t    [ERROR] Message and Key should be in uppercase letters and should not contain spaces.")
            try_again()

        #Message: THISISTHELASTTASKHOORDAY
        #Key: KNIGHTS

        vigenere_cipher = encrypt(input_key, input_message)
        
        print(Fore.CYAN + "\t    [Encrypting..............................]")
        time.sleep(2.5)

        # display cipher text
        print(Fore.GREEN + "\033[1m" + "\n\t    CIPHER TEXT: " + "\033[0m" + Fore.YELLOW + vigenere_cipher)
        print(Fore.CYAN + "\t    [Encryption Successful...................]")

        try_again()

main()