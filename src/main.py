from manager import Manager  # importuje namager i run z pliku manager
from src.buffer import Buffer

# To jest jedyny main programu tzw. finalny main. wszystkob ędzie uruchamiane z tego maina....


def main():
    "main launching method"
    # tu dodac buffera i file handler,menu
    manager = Manager()
    manager.run()
    # buffer = Buffer()


if __name__ == "__main__":
    main()
