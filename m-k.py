RED = '\033[31m'
WHITE = '\033[37m'
os.system("clear")
print(RED+"""
 __       __          __    __ 
/  \     /  |        /  |  /  |
$$  \   /$$ |        $$ | /$$/ 
$$$  \ /$$$ | ______ $$ |/$$/  
$$$$  /$$$$ |/      |$$  $$<   
$$ $$ $$/$$ |$$$$$$/ $$$$$  \  
$$ |$$$/ $$ |        $$ |$$  \ 
$$ | $/  $$ |        $$ | $$  |
$$/      $$/         $$/   $$/ 
Programado por -> Balta""")


def menu_selection():
    print(WHITE+"\n~~~~", "CONVERTIR KM A MILLAS | MILLAS A KM", 4 * "~")
    print("1) KM A MILLAS")
    print("2) MILLAS A KM")

main_loop = True

while not main_loop == False:
    menu_selection()
    user_selection = str(input(RED+"\n-> Seleccione: "))

    if (user_selection == "1"):
        user_in_km = int(input(RED+"\n-> Ingrese el número de KILÓMETROS que le gustaría convertir: "))
        to_miles = round(user_in_km / 1.6093, 3)

        print(WHITE+"\n", 30 * "~%")
        print(" {} Km se convierte en {} Millas.".format(user_in_km, to_miles))
        print("", 30 * "%~", "\n")
        keep_converting = input(RED+"-> ¿Le gustaría seguir convirtiendo? [ si  |  no ] ")
        if (keep_converting == "si"):
            continue
        elif (keep_converting == "no"):
            main_loop = False

        else:
            print(WHITE+"\n¡Mala decisión! ¡Adiós!")
            break


    elif (user_selection == "2"):
        user_in_miles = int(input(RED+"\n-> Ingrese la cantidad de MILLAS que desea convertir: "))
        to_kilometers = round(user_in_miles * 1.6093, 3)

        print(WHITE+"\n",30 * "~%")
        print(" {} Millas se comvierte en {} Km.".format(user_in_miles, to_kilometers))
        print("", 30 * "%~", "\n")
        keep_converting = input(RED+"-> ¿Le gustaría seguir convirtiendo? [ si  |  no ] ")
        if (keep_converting == "si"):
            continue
        elif (keep_converting == "no"):
            main_loop = False

        else:
            print(WHITE+"\n¡Mala decisión! ¡Adiós!")
            break
