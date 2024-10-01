from data import *


def ask_for_init_base ():
    init_base_entry #= input (ask_for_init_base)
    if check_base (init_base_entry):
        return 
    else:
        print ("La base séléctionnée n'est pass supportée. Veuillez choisir une base de 2, 10 ou 16")
        ask_for_init_base ()




def check_base (init_base_entry):
    if init_base_entry == base_list:
        return True
    else:
        return False
    

ask_for_init_base ()