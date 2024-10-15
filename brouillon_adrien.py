# # tools

# def ask_for_init_number ():
#     while init_number_is_not_a_number:
#         init_number_entry = input(ask_for_init_number_question)
#         if int_convert_try(init_number_entry) or hexa_base_convert_try(init_number_entry):

#             return init_number_entry

#         else :
#             print(Error_number_entry)

# def int_convert_try(the_number):
#     try : 
#         the_int_number = int(the_number)
#         return True
#     except ValueError:
#         return False
    
# def hexa_base_convert_try(the_experimented_number):
#         try :
#             the_experimented_number_int  = int(the_experimented_number, 16)
#             return True
#         except ValueError:
#             return False




# #data
# init_number_is_not_a_number = True
# ask_for_init_number_question = "Entrez un nombre entier : "
# Error_number_entry = "Ceci n'est pas un nombre entier valide. Veuillez réessayer."


# ask_for_init_number()

# text_error_base_entry = "La base séléctionnée n'est pas supportée. Veuillez choisir une base de 2, 10 ou 16"
# text_valid_base = "Base valide. Veuillez patienter"
# binary_list = ["2", "bin", "binary", "binaire"]
# hexa_list = ["16", "hexa", "hex", "hexadecimal", "hexadécimal"]
# decimal_list = ["10", "dec", "decimal", "décimal"]
# base_list = [binary_list, hexa_list, decimal_list]
# init_base_entry_is_a_base = True
# is_not_a_base = True

# def check_base (get_init_base_entry):
#     for base in base_list :
#         if get_init_base_entry in base:
#             return True
#     return False

# def ask_for_init_base ():
#     is_not_a_base = True
#     while is_not_a_base:
#         init_base_entry = input ("Entrez la base d'origine du votre nombre : ")
#         if check_base (init_base_entry):
#             is_not_a_base  = False
#             return "2"
#         else:
#             print (text_error_base_entry)




# print(ask_for_init_base ())


# def dec_to_bin(init_number):#le init_number doit etre un int
#     bin_number = ""
#     while init_number > 0: # faudra check les reponses imédiates : =0 et si le nombre n est pas négatif
#         number_conversion = init_number % 2
#         bin_number = str(number_conversion) + bin_number
#         init_number //= 2
#     print(bin_number)

# def dec_to_hexa(init_number):
#     hexa_number = ""
#     while init_number > 0: # faudra check les reponses imédiates : =0 et si le nombre n est pas négatif
#         number_conversion = init_number % 16
#         hexa_number = str(number_conversion) + hexa_number
#         init_number //= 2
#     print(bin_number)
# 
def bin_to_dec():
    init_number = int(input("hi : "))
    dec_number = ""
    init_number_size = len(init_number)
    for i in range(init_number_size):
        dec_number += init_number[i]*(init_number_size-i)
    return dec_number

print(bin_to_dec())

# 
# 
