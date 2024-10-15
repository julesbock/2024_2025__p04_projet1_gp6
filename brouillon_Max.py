#Here,  the brouillon fichier
from data import *
# def hex_to_bin (init_number_entry):
#     int(init_number_entry, 16)


def dec_to_bin(init_number):#le init_number doit etre un int
    bin_number = ""
    while init_number > 0: # faudra check les reponses imédiates : =0 et si le nombre n est pas négatif
        number_conversion = init_number % 2
        bin_number = str(number_conversion) + bin_number
        init_number //= 2
        
            # a = a ** 2 => a **= 2
