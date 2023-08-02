from manager import Manager #importuje namager i run z pliku manager

#To jest jedyny main porgramu tzw. finalny main. wszystkob ędzie uruchamiane z tego maina....

def main():
    "main launching method"
    #tu dodac buffera i file handler,menu
    manager = Manager()
    manager.run()


if __name__ == "__main__":
    main()