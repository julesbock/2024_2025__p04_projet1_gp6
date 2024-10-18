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
