from data_projet_1 import *

def ask_for_the_init_number ():
    init_number_entry = input("Donnez le nombre que vous voulez transformer : ")
    while init_number_entry_is_not_a_number:
        try:
            init_number_entry 
            init_number_int 
            return init_number_int
        except ValueError:
            print("Ce n'est pas un nombre entier valide. Veuillez réessayer.")

def convert_b2b (init_number, init_base, target_base):
    pass
    target_number = None
    return target_number

def execute_convertion ():
    init_number = ask_for_the_init_number ()
    init_base = ask_for_the_init_base ()
    target_base = ask_for_the_target_base ()
    target_number = \
      convert_b2b (init_number, \
                                    init_base, \
                                    target_base)