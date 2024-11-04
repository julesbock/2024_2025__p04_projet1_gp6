from data import * 

def is_valid(number):
    
    return int_convert_try(number) or hexa_base_convert_try(number)

def check_base (get_init_base_entry):
    for base in base_list :
        if get_init_base_entry in base:
            return base[0]
    return False

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


def answer_is_yes(answer):
    return answer == "oui"

def answer_is_no(answer):
    return answer == "non"


def second_check_is_ok(init_number, init_base):
    return is_authorized(str(init_number).upper(), init_base)

def is_authorized(number, base):
    is_in = True
    for char in number :
        maybe_is_in = char in authorized_base_character_dic.get(base)
        is_in = is_in and maybe_is_in
    return is_in
    