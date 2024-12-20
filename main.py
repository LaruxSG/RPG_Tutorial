import os

run = True
menu = True
play = True
rules = False
key = False

HP = 50
ATK = 5
pot = 1
elix = 0
gold = 0
x = 0
y = 0

def clear():
    os.system("cls")

def draw():
    print("xX----------------------Xx")

def save():
    list = [
        name,
        str(HP),
        str(ATK),
        str(pot),
        str(elix),
        str(gold),
        str(x),
        str(y),
        str(key)
    ]

    f = open("load.txt", "w")

    for item in list:
        f.write(item + "\n")
    f.close()

while run:
    while menu:
        draw()
        print("1, NUEVO JUEGO")
        print("2,CARGAR JUEGO")
        print("3, REGLAS")
        print("4,SALIR DEL JUEGO")
        draw()

        if rules:
            draw()
            print("Yo soy el creador de este juego y estas son mis reglas")
            draw()

            rules = False
            choice = ""
            input("> ")
        else:
            choice = input("# ")

        if choice == "1":
            clear()

            draw()
            name = input("Cual es tu nombre, Heroe?")
            clear()

            menu = False
            play = True
        elif choice == "2":
            try:
                f = open("load.txt", "r")
                load_list = f.readlines()
                name = (load_list[0][:-1])
                HP = int(load_list[1][:-1])
                ATK = int(load_list[2][:-1])
                pot = int(load_list[3][:-1])
                elix = int(load_list[4][:-1])
                gold = int(load_list[5][:-1])
                x = int(load_list[6][:-1])
                y = int(load_list[7][:-1])
                key =bool(load_list[8][:-1])
                clear()
                draw()
                print("Bienvenido de vuelta Heroe, " + name + "!")
                draw()
                input("> ")
                mane = False
                play = True
            except OSError:
                print("No hay ninguna partida guardada")
                input("> 2")
        elif choice == "3":
            rules = True
        elif choice == "4":
            quit()

    while play:
        save() #Autoguardado

        clear()

        draw()
        print("Guardar y Salir")
        draw()

        dest = input("# ")

        if dest == "0":
            play = False
            menu = True