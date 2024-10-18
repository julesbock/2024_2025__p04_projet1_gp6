from data import *
from side_tools import * 

base_data_dictionnary = {
    ("2", "16") : bin_to_hex();
    


}

def bin_to_hex(init_number):
    hex_number = bin_to_dec(init_number)
    target_number = dec_to_hex(hex_number)
    return target_number

def hex_to_bin(init_number):
    hex_number = hex_to_dec(init_number)
    target_number = dec_to_bin(hex_number)
    return target_number

def execute_convertion ():

    init_number = ask_for_init_number ()
    init_base = ask_for_init_base ()
    target_base = ask_for_target_base ()
    target_number = \
      convert_b2b (init_number, init_base, target_base)
    
def convert_b2b (init_number, init_base, target_base):
    target_number = 0

    return target_number

def ask_for_init_number ():
    while init_number_entry_is_not_a_number:
        init_number_entry = input(ask_for_init_number_text)
        if is_valid(init_number_entry):
            # init_number_is_a_number()
            return init_number_entry

        else :
            print(Error_number_entry)


def ask_for_init_base ():
    init_base_entry = input (ask_for_init_base_text)
    if check_base (init_base_entry):
        return init_base_entry
    else:
        print (text_error_base_entry)
        ask_for_init_base ()


def ask_for_target_base ():
    target_base_entry = input (ask_for_target_base_text)
    if check_base (target_base_entry):
        return target_base_entry
    else:
        print (text_error_base_entry)
        ask_for_target_base ()        










def int_convert_try(the_number):
    try : 
        the_int_number = int(the_number)
        return True
    except ValueError:
        return False
    

def hexa_base_convert_try(the_experimented_number):
        try :
            the_experimented_number_int  = int(the_experimented_number, 16)
            return True
        except ValueError:
            return False







def convert_if_b_is_b (init_number, init_base, target_base):
    target_number = 0
    if init_base == target_base:
        target_number = init_number
        return target_number
    else:
        pass


def execute_convertion ():
    # init_number = ask_for_init_number ()
    # init_base = ask_for_init_base ()
    # target_base = ask_for_target_base ()
    # target_number = \
    #   convert_b2b (init_number, init_base, target_base)
    



def dec_to_bin(init_number):#le init_number doit etre un int
    bin_number = ""
    while init_number > 0: # faudra check les reponses imédiates : =0 et si le nombre n est pas négatif
        number_conversion = init_number % 2
        bin_number = str(number_conversion) + bin_number
        init_number //= 2
    print(bin_number)
    


def bin_to_dec(init_number):
    dec_number = 0

    if init_number[0] == "-" :
        init_number = init_number.replace("-", "0") 
        sign = "-"
    
    init_number_size = len(init_number)
    
    for i in range(init_number_size):
        dec_number += int(init_number[i]) * (2 ** (init_number_size - i - 1))
    
    return sign + str(dec_number)