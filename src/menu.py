class Menu:
    """Class connected to the main menu of the cipher program"""

    START_MENU = """This is the main menu of cipher program. Please choose the right option to continue: """

    @staticmethod
    def show_menu_options():
        """Crude menu text TBD: adding more menu text"""
        print(
            "This is the main menu of cipher program. Please choose the right option to continue: "
        )
        print("            1: for text coding")
        print("            2: for text decoding")
        print("            3: for save data to a file")
        print("            4: for load data from a file")
        print("            5: to show the buffer")
        print("            6: to end the program!")
