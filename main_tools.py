from data import *
from side_tools import * 
# on doit faire en sorte de check le nombre rentré et la base (si 224 et 2 ca marche) 
# on doit aussi faire les valeurs négatives

def dec_to_hex (init_number):
    target_number = ""
    if init_number == 0:
        return "0"
    
    while init_number > 0:
        remainder = init_number % 16
        target_number = hex_list [remainder] + target_number
        init_number = init_number // 16
    
    return target_number

def hex_to_dec (init_number):
    hex_list
    target_number = 0
    for i in range(len(init_number)):
        list_result = hex_list[-(i+1)].lower()
        target_number += hex_list.index(list_result) * (16**i)
    return target_number


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
    give_result(init_number, init_base, target_base)
    


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



def convert_if_b_is_b (init_number, init_base, target_base):
    target_number = 0
    if init_base == target_base:
        target_number = init_number
        return target_number
    else:
        pass

    

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



base_data_dictionnary = {

    ("2", "10") : bin_to_dec,
    ("2", "16") : bin_to_hex,

    ("10", "2") : dec_to_bin,
    ("10", "16") : dec_to_hex,

    ("16", "2") : hex_to_bin,
    ("16", "10") : hex_to_dec

}

def convert_b2b (init_number, init_base, target_base):

    fonction = base_data_dictionnary.get((init_base, target_base))
    if convert_if_b_is_b(init_number, init_base, target_base):
        return init_number
    else :
        return fonction(init_number)
