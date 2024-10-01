# tools

def ask_for_init_number ():
    while init_number_is_not_a_number:
        init_number_entry = input(ask_for_init_number_question)
        if int_convert_try(init_number_entry) or hexa_base_convert_try(init_number_entry):

            return init_number_entry

        else :
            print(Error_number_entry)

def int_convert_try(the_number):
    try : 
        the_int_number = int(the_number)
        return True
    except ValueError:
        return False
    
def hexa_base_convert_try(the_experimented_number):
        try :
            the_experimented_number_int  = int(the_experimented_number, 16)
            return True
        except ValueError:
            return False




#data
init_number_is_not_a_number = True
ask_for_init_number_question = "Entrez un nombre entier : "
Error_number_entry = "Ceci n'est pas un nombre entier valide. Veuillez réessayer."


ask_for_init_number()
