#Here,  the brouillon fichier
from data import *
from tools import *
# def hex_to_bin (init_number_entry):
#     int(init_number_entry, 16)


def dec_to_bin(init_number):#le init_number doit etre un int
    bin_number = ""
    while init_number > 0: # faudra check les reponses imédiates : =0 et si le nombre n est pas négatif
        number_conversion = init_number % 2
        bin_number = str(number_conversion) + bin_number
        init_number //= 2
        
            # a = a ** 2 => a **= 2

def hex_to_bin(hex_number):
    bin_number = ""
    while hex_number > 0:
        number_conversion = hex_number % 16
        bin_number = str(number_conversion) + bin_number
        hex_number //= 16

# petit test cpdt il y a sûrement une erreur car je n'arrive pas à intégrer les lettres, tu peux essayer de le faire Adrien. 




def ask_for_init_number ():
    while init_number_entry_is_not_a_number:
        init_number_entry = input(ask_for_init_number_text)
        if is_valid(init_number_entry):
            if int_convert_try(init_number_entry) or hexa_base_convert_try(init_number_entry):
            # init_number_is_a_number()
            return init_number_entry

        else :
            print(Error_number_entry)
