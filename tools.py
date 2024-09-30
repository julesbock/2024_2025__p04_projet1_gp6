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
    if check_base (init_base_entry):
        return 
    else:
        print ("La base séléctionnée n'est pass supportée. Veuillez choisir une base de 2, 10 ou 16")
        ask_for_init_base ()

def check_base (init_base_entry):
    if init_base_entry == base_list:
        return True
    else:
        return False


def convert_b2b (init_number, init_base, target_base):
    target_number = 0
    return target_number

def execute_convertion ():
    init_number = ask_for_init_number ()
    init_base = ask_for_init_base ()
    target_base = ask_for_target_base ()
    target_number = \
      convert_b2b (init_number, init_base, target_base)
    

<<<<<<< Updated upstream
=======
def dec_to_bin(init_number):#le init_numebr doit etre un int
    bin_number = ""
    while init_number > 0: # faudra check les reponses imédiates : =0 et si le nombre n est pas négatif
        number_conversion = init_number % 2
        bin_number = str(number_conversion) + bin_number
        init_number //= 2
    print(bin_number)
    



>>>>>>> Stashed changes



def ask_for_target_base ():
    target_base_entry = input ("Entrez la base souhaitée du votre nombre")
    if check_base (target_base_entry):
        return target_base_entry
    else:
        print ("La base donnée n'est pass supportée. Veuillez choisir une base de 2, 10 ou 16")
        ask_for_target_base ()
























































































