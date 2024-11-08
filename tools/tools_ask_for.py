from data import * 
from tools.tools_side import *

def ask_for_init_number ():
    global sign 
    sign = ""
    while init_number_entry_is_not_a_number:
        init_number_entry = input(ask_for_init_number_text)
        if is_valid(init_number_entry):
            init_number = str(init_number_entry)
            if init_number[0] == "-" :
                init_number = init_number.replace("-", "") 
                sign = "-"
            return init_number
        else :
            print(Error_number_entry)


def ask_for_init_base ():
    init_base_entry = input (ask_for_init_base_text)
    valid_base = check_base (init_base_entry)
    if valid_base:
        return valid_base
    else:
        print (text_error_base_entry)
        ask_for_init_base ()

def ask_for_target_base ():
    target_base_entry = input (ask_for_target_base_text)
    valid_base = check_base (target_base_entry)
    if valid_base:
        return valid_base
    else:
        print (text_error_base_entry)
        ask_for_target_base ()       