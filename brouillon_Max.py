#Here,  the brouillon fichier
from data import *
# def hex_to_bin (init_number_entry):
#     int(init_number_entry, 16)


def ask_for_init_base ():
    init_base_entry
    if check_base (init_base_entry):
        return 
    else:
        print (text_error_base_entry)
        ask_for_init_base ()


def check_base (init_base_entry):
    if init_base_entry == base_list:
        return True
    else:
        return False
    
def check_base_bis (target_base_entry):
    if target_base_entry in base_list:
        return True
    else:
        return False

def ask_for_target_base (n):
    target_base_entry = n 
    while check_base_bis(n) == False:
        print(text_error_base_entry)
        ask_for_init_base()
    else: 
        return target_base_entry  # Faux de la ligne 5 à 34