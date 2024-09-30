from data import *

def ask_for_init_number ():
    init_number_entry = input("Donnez le nombre que vous voulez transformer : ")
    while init_number_entry_is_not_a_number:
        try:
            init_number_entry 
            init_number_int 
            return init_number_int
        except ValueError:
            print("Ceci n'est pas un nombre entier valide. Veuillez réessayer.")

def ask_for_init_base ():
    init_base_entry = input ("Entrez la base d'origine du votre nombre")
    while init_base_entry_is_a_base:
        try:
            init_base_entry_is_a_base == True
            return init_base_entry
        except ValueError:
            print ("La base séléctionée est non supportée. Veuillez choisir une base de 2, 10 ou 16")


def convert_b2b (init_number, init_base, target_base):
    target_number = 0
    return target_number

def execute_convertion ():
    init_number = ask_for_init_number ()
    init_base = ask_for_init_base ()
    target_base = ask_for_target_base ()
    target_number = \
      convert_b2b (init_number, init_base, target_base)
    
































