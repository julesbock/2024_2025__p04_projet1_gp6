from data import *
from tools import *

def execute_convertion_and_give_result ():
    init_number = ask_for_init_number ()
    init_base = ask_for_init_base ()
    if second_check_is_ok(init_number, init_base):
        target_base = ask_for_target_base ()
        if init_number_is_0(init_number):
            target_number = "0"
        else : 
            target_number = \
            convert_b2b (init_number, init_base, target_base)
        give_result(init_number, init_base, target_base, target_number)
    else:
        print(error_between_base_and_number_text)

def give_result (init_number, init_base, target_base, target_number):
    
    print (f"Vous avez demandé de changer le nombre {sign + str(init_number)} en base {init_base} vers la base {target_base}. "
           + "\n"
           f"Le résultat est : {target_number}"
           + "\n"
           + thank_you_text)