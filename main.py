from data import *

def bin_dec_hex__to__bin_dec_hex (init_number, init_base, target_base):
    pass
    target_number = None
    return target_number



assert bin_dec_hex__to__bin_dec_hex ("101", 2, 10) == "5"

def do_the_job ():
    init_number = ask_for_the_init_number ()
    init_base = ask_for_the_init_base ()
    target_base = ask_for_the_target_base ()
    target_number = bin_dec_hex__to__bin_dec_hex (init_number, \
                                    init_base, \
                                    target_base)

do_the_job ()


from data import *
from tools import *

def run_main():
    execute_convertion()
    give_result()


assert convert_b2b ("101", 2, 10) == "5"



if __name__ == "__main__":
    run_main()
