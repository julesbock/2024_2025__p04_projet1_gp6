from data import *
from tools_side import * 

# on doit faire en sorte de check le nombre rentré et la base (si 224 et 2 ca marche) 
# on doit aussi faire les valeurs négatives

# Fonctions de conversion

def dec_to_hex (init_number):
    target_number = ""
    init_number = int(init_number)
    if init_number == 0:
        return "0"
    
    while init_number > 0:
        remainder = init_number % 16
        target_number = hex_character_list [remainder] + target_number
        init_number = init_number // 16
    
    return target_number

def dec_to_bin(init_number):#le init_number doit etre un int
    bin_number = ""
    init_number = int(init_number)
    while init_number > 0: # faudra check les reponses imédiates : =0 et si le nombre n est pas négatif
        number_conversion = init_number % 2
        bin_number = str(number_conversion) + bin_number
        init_number //= 2
    return bin_number


def bin_to_hex(init_number):
    hex_number = bin_to_dec(init_number)
    target_number = dec_to_hex(hex_number)
    return target_number

def bin_to_dec(init_number):
    dec_number = 0
    sign = ""

    if init_number[0] == "-" :
        init_number = init_number.replace("-", "0") 
        sign = "-"
    
    init_number_size = len(init_number)
    
    for i in range(init_number_size):
        dec_number += int(init_number[i]) * (2 ** (init_number_size - i - 1))
    
    return sign + str(dec_number)


def hex_to_bin(init_number):
    hex_number = hex_to_dec(init_number)
    target_number = dec_to_bin(hex_number)
    return target_number

def hex_to_dec (init_number):
    target_number = 0
    init_number = str(init_number).upper()
    for digit in init_number:
        reverse_pos_digit = len(init_number) - init_number.index(digit) - 1
        target_number += hex_character_list.index(digit) * (16**reverse_pos_digit)
    return target_number 


def convert_if_b_is_b (init_number, init_base, target_base):
    target_number = 0
    if init_base == target_base:
        return True
    else:
        return False


base_data_dictionnary_to_convert = {

    ("2", "10") : bin_to_dec,
    ("2", "16") : bin_to_hex,

    ("10", "2") : dec_to_bin,
    ("10", "16") : dec_to_hex,

    ("16", "2") : hex_to_bin,
    ("16", "10") : hex_to_dec

}


# Fonctions d'execution

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


def convert_b2b (init_number, init_base, target_base):

    fonction = base_data_dictionnary_to_convert.get((init_base, target_base))
    if convert_if_b_is_b(init_number, init_base, target_base):
        return init_number
    else :
        return fonction(init_number)



# Main fonctions

def execute_convertion ():
    init_number = ask_for_init_number ()
    init_base = ask_for_init_base ()
    if second_check_is_(init_number, init_base):
        target_base = ask_for_target_base ()
        target_number = \
        convert_b2b (init_number, init_base, target_base)
        give_result(init_number, init_base, target_base, target_number)
    else:
        print(Error_between_base_and_number)

def give_result (init_number, init_base, target_base, target_number):
    
    print (f"Vous avez demandé de changer le nombre {init_number} en base {init_base} vers la base {target_base}. "
           + "\n"
           f"Le résultat est : {target_number}"
           + "\n"
           + thank_you_text)
    

