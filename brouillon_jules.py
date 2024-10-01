from data import *


    
def ask_for_init_base ():
    init_base_entry
    if check_base (init_base_entry) == True:
        return 
    else:
        print (text_error_base_entry)
        ask_for_init_base ()


def check_base (init_base_entry):
    for init_base_entry in base_list:
        return check_base (init_base_entry) == True
    else:
        return False
    
ask_for_init_base ()