def ask_for_the_init_number ():
    init_number_entry = input("Donnez le nombre que vous voulez transformer : ")
    while init_number_entry_is_not_a_number:
        try:
            init_number_entry = input("Entrez un nombre entier : ")
            init_number_int = int(init_number_entry)
            return init_number_int
        except ValueError:
            print("Ce n'est pas un nombre entier valide. Veuillez réessayer.")
ask_for_the_init_base = 
ask_for_the_target_base = 