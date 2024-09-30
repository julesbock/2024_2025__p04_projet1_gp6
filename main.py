def convert_b2b (init_number, init_base, target_base):
    pass
    target_number = None
    return target_number

from utils import *

assert convert_b2b ("101", 2, 10) == "5"

def execute_convertion ():
    init_number = ask_for_the_init_number ()
    init_base = ask_for_the_init_base ()
    target_base = ask_for_the_target_base ()
    target_number = \
      convert_b2b (init_number, \
                                    init_base, \
                                    target_base)

execute_convertion ()
