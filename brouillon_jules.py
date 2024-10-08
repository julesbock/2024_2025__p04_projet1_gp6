# Data ask_for_init_number

init_number_entry_is_not_a_number = True

# Data ask_for_init_base

init_base_entry = input ("Entrez la base d'origine du votre nombre : ")
text_error_base_entry = "La base séléctionnée n'est pas supportée. Veuillez choisir une base de 2, 10 ou 16"
text_valid_base = "Base valide. Veuillez patienter"

init_base_entry_is_a_base = True

binary_list = ["2", "bin", "binary", "binaire"]
hexa_list = ["16", "hexa", "hex", "hexadecimal", "hexadécimal"]
decimal_list = ["10", "dec", "decimal", "décimal"]
base_list = binary_list + hexa_list + decimal_list

# Data ask_for_target_base

target_base_entry = input ("Entrez la base finale pour votre nombre : ")
target_base_entry_is_a_base = True


def ask_for_init_base ():
    init_base_entry
    if check_base (init_base_entry):
        print (text_valid_base)
        return init_base_entry
    else:
        print (text_error_base_entry)
        ask_for_init_base ()


def check_base (init_base_entry):
    return init_base_entry in base_list
    

ask_for_init_base()