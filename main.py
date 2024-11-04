from data import *
from tools_main import *


def run_main():
    execute_convertion_and_give_result()
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
