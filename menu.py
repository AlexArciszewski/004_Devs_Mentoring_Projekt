from typing import Callable


class Menu:


    @staticmethod
    def code_the_file():
        print("code the file")

    def uncode_the_file():
        print("uncode the file")


    def remove_from_list():
        print("")


    options: dict[int, Callable] = {
        1: code_the_file,
            #("""To create new file press: "n". To open existing file press "o". To get back to main menu press "b".""" )
            # jak wybierze nowy to powstanie notepad do zapisania....i prosba o pdoanie tekstu do zapisu lub powrót do menu
            #jak wybierze o to uruchamia się wyszukiwarka lub nacisnij ba aby wrocic do poprzedniego menu...


        2: uncode_the_file,
            #po wybraniu bedzie wybierz plik do odkodowania jak w opcji wyżej : To open existing file press "o".
            # To get back to main menu press "b".""" )
            # jak wybierze o to uruchamia się wyszukiwarka lub nacisnij ba aby wrocic do poprzedniego menu...
        3: remove_from_list,
    }

    user_choice = int(input("Welcome to code generator. Please choose right option from menu"))

    if user_choice in options:
        options.get(user_choice)

    else:
       print("Invalid option")


