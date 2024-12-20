run = True
menu = True
play = True
rules = False

HP = 50
ATK = 3

def save():
    list = [
        name,
        str(HP),
        str(ATK)
    ]

    f = open("load.txt", "w")

    for item in list:
        f.write(item + "\n")
    f.close()

while run:
    while menu:
        print("1, NUEVO JUEGO")
        print("2,CARGAR JUEGO")
        print("3, REGLAS")
        print("4,SALIR DEL JUEGO")

        if rules:
            print("Yo soy el creador de este juego y estas son mis reglas")
            rules = False
            choice = ""
            input("# ")
        else:
            choice = input("# ")

        if choice == "1":
            name = input("Cual es tu nombre, Heroe?")
            menu = False
            play = True
        elif choice == "2":
            f = open("load.txt", "r")
            load_list = f.readlines()
            name = load_list[0]
            HP = load_list[1]
            ATK = load_list[2]
            print(name, HP)
        elif choice == "3":
            pass
        elif choice == "4":
            quit()

    while play:
        save() #Autoguardado

        dest = input("# ")

        if dest == "0":
            play = False
            menu = True