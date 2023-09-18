from colorama import Fore

class Menu:
    """Class connected to the main menu of the cipher program"""

    START_MENU = """This is the main menu of cipher program. Please choose the right option to continue: """

    @staticmethod
    def show_menu_options():
        """Creates a menu that is shown after start of the program"""
        print(
            f"{Fore.CYAN}This is the main menu of cipher program. Please choose the right option to continue: {Fore.WHITE}"
        )
        print(f"            {Fore.BLUE}1: for text coding")
        print("            2: for text decoding")
        print("            3: for save data to a file")
        print("            4: for load data from a file")
        print("            5: to show the buffer")
        print(f"            6: to end the program!{Fore.WHITE}")
