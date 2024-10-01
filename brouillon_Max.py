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
    if target_base_entry == base_list:
        return True
    else:
        return False

def ask_for_target_base ():
    target_base_entry 
    for target_base_entry in base_list:
        if target_base_entry == base_list:
            return target_base_entry
        else: 
            # print (text_error_base_entry)
            ask_for_target_base ()