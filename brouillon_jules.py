from data import *
from main_tools import *


def dec_to_hex (init_number):
    target_number = ""
    if init_number == 0:
        return "0"
    
    while init_number > 0:
        remainder = init_number % 16
        target_number = hex_list [remainder] + target_number
        init_number = init_number // 16
    
    return target_number


print(dec_to_hex (1000))