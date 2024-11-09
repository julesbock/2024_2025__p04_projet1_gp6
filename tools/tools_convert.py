from .tools_side import *

def dec_to_hex (init_number):
    target_number = ""
    init_number = int(init_number)
    while init_number > 0:
        remainder = init_number % 16
        target_number = hex_character_list [remainder] + target_number
        init_number = init_number // 16
    return target_number


def dec_to_bin (init_number):
    bin_number = ""
    init_number = int(init_number)
    while init_number > 0: 
        number_conversion = init_number % 2
        bin_number = str(number_conversion) + bin_number
        init_number //= 2
    return bin_number


def bin_to_hex (init_number):
    hex_number = bin_to_dec(init_number)
    target_number = dec_to_hex(hex_number)
    return target_number


def bin_to_dec (init_number):
    dec_number = 0
    init_number_size = len(init_number)
    for i in range(init_number_size):
        dec_number += int(init_number[i]) * (2 ** (init_number_size - i - 1))
    return dec_number


def hex_to_bin (init_number):
    hex_number = hex_to_dec(init_number)
    target_number = dec_to_bin(hex_number)
    return target_number


def hex_to_dec (init_number):
    target_number = 0
    init_number = str(init_number).upper()
    for i, digit in enumerate(reversed(init_number)):  # On utilise enumerate pour avoir l'index exact
        target_number += hex_character_list.index(digit) * (16 ** i)
    return target_number 


def convert_if_b_is_b (init_number, init_base, target_base):
    target_number = 0
    if init_base == target_base:
        return True
    else:
        return False

def convert_b2b (init_number, init_base, target_base):
    fonction = base_data_dictionnary_to_convert.get((init_base, target_base))
    if convert_if_b_is_b(init_number, init_base, target_base):
        return sign + str(init_number)
    else :
        return sign + str(fonction(init_number))



base_data_dictionnary_to_convert = {

    ("2", "10") : bin_to_dec,
    ("2", "16") : bin_to_hex,

    ("10", "2") : dec_to_bin,
    ("10", "16") : dec_to_hex,

    ("16", "2") : hex_to_bin,
    ("16", "10") : hex_to_dec
}