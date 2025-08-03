name =input(" what is your name? ")
match name:
    case "Harry" | "Hermione" | "Ron":
        print("Gryffindor")
    case "draco":
        print("slytherin")
    case  _:
        print("who? ")
    