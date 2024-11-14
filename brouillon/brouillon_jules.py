from data import *
from ..tools import *
from main import *


def dec_to_hex (init_number):
    target_number = ""
    if init_number == 0:
        return "0"
    
    while init_number > 0:
        remainder = init_number % 16
        target_number = hexa_list [remainder] + target_number
        init_number = init_number // 16
    
    return target_number


print(dec_to_hex (1000))

# data
target_number = 0
thank_you_text = "Merci d'avoir utilisé notre outil de conversion."
restart_text = "Souhaitez vous convertir un autre nombre ?"
goodbye_text = thank_you_text + "A bientot !"
input_error_text = "Veuillez répondre par oui ou par non"

#tools
def ask_for_restart ():
    answer = input(restart_text).lower()
    while True:
        if answer == "oui":
            execute_convertion_and_give_result()
        elif answer == "non":
            print(goodbye_text)
        else:
            print(input_error_text)


def give_result ():
    print (f"Le nombre converti est : {target_number}"
           + "\n"
           + thank_you_text)