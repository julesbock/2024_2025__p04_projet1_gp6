# Data ask_for_init_number

init_number_entry_is_not_a_number = True
ask_for_init_number_text = "Entrez un nombre entier : "
Error_number_entry = "Ceci n'est pas un nombre entier valide. Veuillez réessayer."

# Data ask_for_init_base

text_error_base_entry = "La base séléctionnée n'est pas supportée. Veuillez choisir une base de 2, 10 ou 16"
text_valid_base = "Base valide. Veuillez patienter"
ask_for_init_base_text = "Entrez la base d'origine du votre nombre : "
init_base_entry_is_a_base = True

# Data ask_for_target_base

target_base_entry_is_a_base = True
ask_for_target_base_text = "Entrez la base finale de votre nombre : "

# Data base

binary_list = ["2", "bin", "binary", "binaire"]
hexa_list = ["16", "hexa", "hex", "hexadecimal", "hexadécimal"]
decimal_list = ["10", "dec", "decimal", "décimal"]
base_list = [binary_list, hexa_list, decimal_list]

# Data caractères hexadécimaux

binary_character_list = "01"
dec_character_list = "0123456789"
hex_character_list = "0123456789ABCDEF"

# Data main fonctions

target_number = 0 
thank_you_text = "Merci d'avoir utilisé notre outil de conversion. "
restart_text = "Souhaitez vous convertir un autre nombre ? "
goodbye_text = thank_you_text + "A bientôt !"
input_error_text = 'Veuillez répondre par "oui" ou par "non", sans espace'
error_between_base_and_number_text = \
    "Désolé, le nombre et la base de celui-ci que nous vous avez donné ne sont pas compatibles (peut-être avez-vous mis un caractere superflu, espace ou autre)"
authorized_base_character_dic = {
    "2"  : binary_character_list,
    "10" : dec_character_list,
    "16" : hex_character_list
}