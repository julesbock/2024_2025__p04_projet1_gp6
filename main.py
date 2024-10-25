from data import *
from tools_main import *


def run_main():
    execute_convertion()
    ask_for_restart ()
 
def ask_for_restart ():
    while True:
        answer = input(restart_text).lower()
        if answer_is_yes(answer):
            run_main()
            return  
        elif answer_is_no(answer):
            print(goodbye_text)
            return  
        else:
            print(input_error_text)

run_main()



# def bin_dec_hex__to__bin_dec_hex (init_number, init_base, target_base):
#     pass
#     target_number = None
#     return target_number



# assert bin_dec_hex__to__bin_dec_hex ("101", 2, 10) == "5"

# def do_the_job ():
#     init_number = ask_for_init_number ()
#     init_base = ask_for_init_base ()
#     target_base = ask_for_target_base ()
#     target_number = bin_dec_hex__to__bin_dec_hex (init_number, \
#                                     init_base, \
#                                     target_base)

