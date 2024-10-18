#Here,  the brouillon fichier
from data import *
from tools import *
# def hex_to_bin (init_number_entry):
#     int(init_number_entry, 16)


def dec_to_bin(init_number):#le init_number doit etre un int
    if init_number is not int:      # faudra check les reponses imédiates : =0 et si le nombre n est pas négatif
        raise ValueError ("Le nomnre doit être un entier")
    if init_number < 0:
        raise ValueError ("Le nombre est négatif, il doit être positif")
    if init_number == 0:
        return "0"
    bin_number = ""
    while init_number > 0:
        number_conversion = init_number % 2
        bin_number = str(number_conversion) + bin_number
        init_number //= 2
    return bin_number
 

def hex_to_dec (hex_number):
    hex_list