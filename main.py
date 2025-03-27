import hampus 
import alex
import kevin
import louisian 


def main():
    print("Ange en siffra: 1. Kevin, 2. Hampus, 3. Alex, 4. Louisian")
    name = input("Ange namn: ")

    if name.isdigit != True and int(name)>4 or int(name)<1:
        print("Du måste ange ett nummer")
        return main()
    
    if name == "1":
        return kevin.food()
    elif name == "2":
        return hampus.food()
    elif name == "3":
        return alex.alex_food()
    else:
        return louisian.food()

main()