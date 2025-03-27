import hampus
import alex
import Kevin
import Louisian


def main():
    print("Ange en siffra: 1. Kevin, 2. Hampus, 3. Alex, 4. Louisian")
    name = input("Ange namn: ")

    if not name.isdigit or int(name)>4 or int(name)<1:
        print("Du måste ange ett nummer")
        return main()

    if name == "1":
        print("Vill du se 1)mat eller 2)dryck")
        choice = input("ange siffra: ")
        if choice == "1":
            return Kevin.food()
        elif choice == "2":
            return Kevin.drink()
    elif name == "2":
        print("Vill du se 1)mat eller 2)dryck")
        choice = input("ange siffra: ")
        if choice == "1":
            return hampus.food()
        elif choice == "2":
            return hampus.drink()
    elif name == "3":
        print("Vill du se 1)mat eller 2)dryck")
        choice = input("ange siffra: ")
        if choice == "1":
            return alex.food()
        elif choice == "2":
            return alex.drink()
    else:
        print("Vill du se 1)mat eller 2)dryck")
        choice = input("ange siffra: ")
        if choice == "1":
            return Louisian.food()
        elif choice == "2":
            return Louisian.drink()

main()