import sys
from datetime import datetime
from ohce import Ohce

def main():
    if len(sys.argv) < 2:
        print("Uso: python -m src.main <nombre>")
        return

    name = sys.argv[1]
    ohce = Ohce(name=name)
    print(ohce.greet())

    while True:
        user_input = input()
        response = ohce.process_input(user_input)
        print(response)
        if user_input.lower() == "stop":
            break

if __name__ == "__main__":
    main()
