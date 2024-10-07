from data import *

def ask_for_init_number ():
    while init_number_entry_is_not_a_number:
        init_number_entry = input(ask_for_init_number_question)
        if int_convert_try(init_number_entry) or hexa_base_convert_try(init_number_entry):
            # init_number_is_a_number()
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

# def init_number_is_a_number():
#     init_number_entry_is_not_a_number = False


def ask_for_init_base ():
    init_base_entry
    if check_base (init_base_entry):
        return 
    else:
        print (text_error_base_entry)
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
    

def dec_to_bin(init_number):#le init_number doit etre un int
    bin_number = ""
    while init_number > 0: # faudra check les reponses imédiates : =0 et si le nombre n est pas négatif
        number_conversion = init_number % 2
        bin_number = str(number_conversion) + bin_number
        init_number //= 2
    print(bin_number)
    

def ask_for_target_base ():
    target_base_entry #= input ("Entrez la base finale pour votre nombre")
    if check_base (target_base_entry):
        return target_base_entry
    else:
        print (text_error_base_entry)
        ask_for_target_base ()



