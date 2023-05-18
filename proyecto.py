import time
import sys
import random
import os
##os.system('cls')

alquilar = None
proceso = None
register = None
rectificar = None
rectificar2 = None
realalquilar = None
edad = None
correcto = None
tiempo = None
correctotiempo = None

def juegosdisponibles(jueguitos, nombres):
    """Esta función elije entre una lista de nombres nombres aleatorios
    que no saldrán en pantalla al usuario simulando que ya están alquilados"""
    clientes_y_juegos = []
    juegos_disponibles = random.choices(jueguitos, k=random.randint(1,13))
    juegos_disponibles = sorted(set(juegos_disponibles))
    juegos_de_clientes = []
    for x in range(13):
        if not jueguitos[x] in juegos_disponibles:
            juegos_de_clientes += [jueguitos[x]]
    clientess = []

    for x in range(len(juegos_de_clientes)):
        num = random.randint(0,45)
        clientess += [nombres[num]]
    
    for x in range(len(clientess)):
        clientes_y_juegos += [[clientess[x], juegos_de_clientes[x]]]

    
    return (juegos_disponibles, clientes_y_juegos)

def comprobacion_dni(comprov ,Dni):
    """Esta función comprueba el dni introducido por el ususario
    y comprueba los dnis que luego serán puesto a las personas aleatorias que han alquilado juegos
    comprobandolos de la misma manera que lo hace con el usuario"""
    if comprov == 1:
        try:
            letras = "TRWAGMYFPDXBNJZSQVHLCKE"
            y = int(Dni[:8]) % 23
            dni = Dni[:8] + letras[y]
            dni_axiliar = Dni 
            if Dni == dni:
                return True
            else:
                return False
        except:
            return False

    if comprov == 2:
        aux = []
        for x in range(len(Dni)):
            letras = "TRWAGMYFPDXBNJZSQVHLCKE"
            y = int(Dni[x]) % 23
            dni = Dni[x] + letras[y]
            aux += [dni]
        return aux

def confirmacion_nombre(confirmacion1, nuevo_nombre):
    """Esta función se repite hasta el usuario esté de acuerdo
    con el nombre que ha introducido por si se ha equivocado"""
    confirmacion3 = None
    if confirmacion1 == 1:
        return nuevo_nombre
    if confirmacion1 == 2:
        nuevo_nombre2 = nuevo_nombre
        try:
            os.system('cls')
        except:
            try:
                os.system('clear')
            except:
                pass
        time.sleep(1)
        print ("El nombre introducido era:", nuevo_nombre)
        time.sleep(1)
        nuevo_nombre = input("Tu nombre es: ")
        time.sleep(1)
        print("-------------------------------------------------------")
        print("Has cambiado tu nombre de:", nuevo_nombre2, "a", nuevo_nombre)
        print("-------------------------------------------------------")
        time.sleep(2)
        confirmacion3 = int(input("1 = correcto, 2 = cambiar de nuevo\n"))
        confirmacion4 = confirmacion_nombre(confirmacion3, nuevo_nombre)
        return confirmacion4

def confirmacion_edad(confirmacion1, nueva_edad):
    """Esta función se repite hasta el usuario esté de acuerdo
    con la edad que ha introducido por si se ha equivocado"""
    confirmacion3 = None
    nueva_edad2 = None
    if confirmacion1 == 1:
        return nueva_edad
    if confirmacion1 == 2:
        try:
            os.system('cls')
        except:
            try:
                os.system('clear')
            except:
                pass
        time.sleep(1)
        nueva_edad3 = nueva_edad
        while nueva_edad2 == None or nueva_edad < 18 or nueva_edad >= 100:
            try:
                time.sleep(1)
                print ("La edad introducida era:", nueva_edad)
                time.sleep(1)
                nueva_edad = int(input("Tu edad es: "))
                if nueva_edad < 18:
                    time.sleep(1)
                    print("Debes ser mayor de edad para registrarte")
                    time.sleep(4)
                    try:
                        os.system('cls')
                    except:
                        try:
                            os.system('clear')
                        except:
                            pass
                elif nueva_edad >= 100:
                    time.sleep(1)
                    print("Valor incorrecto")
                    time.sleep(2)
                    try:
                        os.system('cls')
                    except:
                        try:
                            os.system('clear')
                        except:
                            pass
                else:
                    nueva_edad2 = nueva_edad
            except:
                time.sleep(1)
                print("Valor incorrecto")
                time.sleep(2)
                try:
                    os.system('cls')
                except:
                    try:
                        os.system('clear')
                    except:
                        pass

        time.sleep(1)
        print("-------------------------------------------------------")
        print("Has cambiado tu edad de:", nueva_edad3, "a", nueva_edad)
        print("-------------------------------------------------------")
        time.sleep(2)
        confirmacion3 = int(input("1 = correcto, 2 = cambiar de nuevo\n"))
        confirmacion4 = confirmacion_edad(confirmacion3, nueva_edad)
        return confirmacion4
        
def rectificacion(rectificar2, nombre, edad):
    """Esta función se repite hasta el usuario esté de acuerdo
    con el nombre o la edad que ha introducido por si se ha equivocado"""
    confirmacion = None
    if rectificar2 == 1:
        try:
            os.system('cls')
        except:
            try:
                os.system('clear')
            except:
                pass
        time.sleep(1)
        print ("El nombre introducido era:", nombre)
        time.sleep(1)
        nuevo_nombre = input("Tu nombre es: ")
        time.sleep(1)
        print("-------------------------------------------------------")
        print("Has cambiado tu nombre de:", nombre, "a", nuevo_nombre)
        print("-------------------------------------------------------")
        time.sleep(2)
        while confirmacion == None or confirmacion <= 0 or confirmacion >= 3:
            try:
                confirmacion = int(input("1 = correcto, 2 = cambiar de nuevo\n"))
                confirmacion2 = confirmacion_nombre(confirmacion, nuevo_nombre)
                return confirmacion2
                if confirmacion <= 0 or confirmacion >= 3 and confirmacion2 != str:
                    time.sleep(1)
                    print("Valor incorrecto")
                    time.sleep(2)
                    try:
                        os.system('cls')
                    except:
                        try:
                            os.system('clear')
                        except:
                            pass
            except:
                time.sleep(1)
                print("Valor incorrecto")
                time.sleep(2)
                try:
                    os.system('cls')
                except:
                    try:
                        os.system('clear')
                    except:
                        pass
    
    if rectificar2 == 2:
        nueva_edad = None
        try:
            os.system('cls')
        except:
            try:
                os.system('clear')
            except:
                pass
        time.sleep(1)
        while nueva_edad == None or nueva_edad < 18 or nueva_edad >= 100:
                try:        
                    time.sleep(1)
                    print ("La edad introducida era:", edad)
                    time.sleep(1)
                    nueva_edad = int(input("Tu edad es: "))
                    if nueva_edad < 18:
                        time.sleep(1)
                        print("Debes ser mayor de edad para registrarte")
                        time.sleep(4)
                        try:
                            os.system('cls')
                        except:
                            try:
                                os.system('clear')
                            except:
                                pass
                    elif nueva_edad >= 100:
                        time.sleep(1)
                        print("Valor incorrecto")
                        time.sleep(2)
                        try:
                            os.system('cls')
                        except:
                            try:
                                os.system('clear')
                            except:
                                pass
                except:
                    time.sleep(1)
                    print("Valor incorrecto")
                    time.sleep(2)
                    try:
                        os.system('cls')
                    except:
                        try:
                            os.system('clear')
                        except:
                            pass

        time.sleep(1)
        print("-------------------------------------------------------")
        print("Has cambiado tu edad de:", edad, "a", nueva_edad)
        print("-------------------------------------------------------")
        time.sleep(2)
        while confirmacion == None or confirmacion <= 0 or confirmacion >= 3:
            try:
                confirmacion = int(input("1 = correcto, 2 = cambiar de nuevo\n"))
                confirmacion2 = confirmacion_edad(confirmacion, nueva_edad)
                return confirmacion2
                if confirmacion <= 0 or confirmacion >= 3 and confirmacion2 != int:
                    time.sleep(1)
                    print("Valor incorrecto")
                    time.sleep(2)
                    try:
                        os.system('cls')
                    except:
                        try:
                            os.system('clear')
                        except:
                            pass
            except:
                time.sleep(1)
                print("Valor incorrecto")
                time.sleep(2)
                try:
                    os.system('cls')
                except:
                    try:
                        os.system('clear')
                    except:
                        pass

def admin(register):
    """Entrar en modo administrador de la tienda"""
    if register == 404 or register == "404":
        return True

def correctooo(correctoo, juegoaalquilar, alquilado, realalquilar):
    """Esta función se repite hasta el usuario esté de acuerdo
    con el juego que ha elejido por si se ha equivocado"""
    confirmacion2 = None
    confirmacion3 = None
    juegoaalquilar3 = None
    if correctoo == 2:
        return alquilado
    if correctoo == 1:
        confirmacion = None
        try:
            os.system('cls')
        except:
            try:
                os.system('clear')
            except:
                pass
        time.sleep(1)
        juegoaalquilar24 = realalquilar
        while juegoaalquilar3 == None or juegoaalquilar3 < 0 or juegoaalquilar3 > len(juegoaalquilar) or confirmacion2 == None:
            juegoaalquilar2 = juegoaalquilar[realalquilar]
            cont = 0
            print("-------------------------------------------------------")
            for x in range(len(juegos_disponibles[0])):
                time.sleep(0.5)
                print(cont, juegos_disponibles[0][x])
                time.sleep(0.5)
                cont += 1
            print("-------------------------------------------------------")
            try:
                time.sleep(1)
                print ("El juego seleccionado anteriormente era:", juegoaalquilar[realalquilar])
                time.sleep(1)
                alquilado = int(input("¿Cuál deseas alquilar?\n"))

                if alquilado < 0 or alquilado > len(juegoaalquilar)-1:
                    print("Valor incorrecto")
                    time.sleep(2)
                    juegoaalquilar3 = None
                    alquilado = juegoaalquilar24
                    confirmacion = 1
                else:
                    juegoaalquilar3 = juegoaalquilar[realalquilar]
                    juegoaalquilar1 = juegoaalquilar[alquilado]
                    print("-------------------------------------------------------")
                    print("Has cambiado el juego a alquilar de:", juegoaalquilar[realalquilar], "a", juegoaalquilar1)
                    print("-------------------------------------------------------")
                    confirmacion = None
                    time.sleep(2)
            except:
                time.sleep(1)
                print("Valor incorrecto")
                time.sleep(2)
                try:
                    os.system('cls')
                except:
                    try:
                        os.system('clear')
                    except:
                        pass
                hola = None

            while confirmacion == None or confirmacion <= 0 or confirmacion >= 3:
                juegoaalquilar2 = juegoaalquilar[realalquilar]
                try:
                    confirmacion = int(input("1 = correcto, 2 = cambiar de nuevo\n"))
                    
                    if confirmacion <= 0 or confirmacion >= 3:
                        time.sleep(1)
                        print("Valor incorrecto")
                        time.sleep(2)
                        try:
                            os.system('cls')
                        except:
                            try:
                                os.system('clear')
                            except:
                                pass
                        confirmacion2
                    else:
                        if confirmacion == 1:
                            confirmacion = 2
                        else:
                            confirmacion = 1
                        confirmacion2 = correctooo(confirmacion, juegoaalquilar, alquilado, alquilado)
                        return confirmacion2
                except:
                    time.sleep(1)
                    print("Valor incorrecto")
                    time.sleep(2)
                    try:
                        os.system('cls')
                    except:
                        try:
                            os.system('clear')
                        except:
                            pass
                
            juegoaalquilar2 = juegoaalquilar[realalquilar]
            
    return juegoaalquilar[alquilado]

def correctotiempooo(confirmaciondetiempo, tiempo):
    """Esta función se repite hasta el usuario esté de acuerdo
    con el tiempo para alquilar el juego que ha introducido por si se ha equivocado"""
    correctotiempo = None
    tiempo2 = None
    if confirmaciondetiempo == 2:
        return tiempo
    if confirmaciondetiempo == 1:
        while tiempo2 == None or tiempo2 <= 0 or tiempo2 >= 5:
            try:
                time.sleep(1)
                try:
                    os.system('cls')
                except:
                    try:
                        os.system('clear')
                    except:
                        pass
                tiempo = int(input("¿Cuanto tiempo quieres alquilar el juego?(1,2,3 o 4 semanas), (MÁXIMO 4 SEMANAS)\n"))
                if tiempo <= 0 or tiempo >= 5:
                    time.sleep(1)
                    print("Valor incorrecto")
                    time.sleep(2)
                    try:
                        os.system('cls')
                    except:
                        try:
                            os.system('clear')
                        except:
                            pass
                    tiempo2 = None
                else:
                    tiempo2 = 1
            except:
                time.sleep(1)
                print("Valor incorrecto")
                time.sleep(2)
                try:
                    os.system('cls')
                except:
                    try:
                        os.system('clear')
                    except:
                        pass

    if tiempo == 1:
        semanana = "semana"
    if tiempo > 1:
        semanana = "semanas"
    
    while correctotiempo == None or correctotiempo <= 0 or correctotiempo >= 3:
    
        try:
            print("El tiempo introducido para alquilar el juego es:", tiempo, semanana)
            time.sleep(1)
            print("¿Quieres Cambiarlo?")
            correctotiempo = int(input("1 = si 2 = No \n"))
            corrección = correctotiempooo(correctotiempo, tiempo)
            
            if correctotiempo <= 0 or correctotiempo >= 3:
                time.sleep(1)
                print("Valor incorrecto")
                time.sleep(2)
                try:
                    os.system('cls')
                except:
                    try:
                        os.system('clear')
                    except:
                        pass
        except:
            time.sleep(1)
            print("Valor incorrecto")
            time.sleep(2)
            try:
                os.system('cls')
            except:
                try:
                    os.system('clear')
                except:
                    pass
    return tiempo
    
for i in range(101):
    time.sleep(0.01)
    sys.stdout.write("\r%d%%" % i)
    sys.stdout.flush()

try:
    os.system('cls')
except:
    try:
        os.system('clear')
    except:
        pass
   
print("Bienvenido/a a la Tienda de Video Juegos: AMATEUR PLAYERS")
time.sleep(3)
print("¿Qué desea hacer?")
time.sleep(1)

while proceso == None or proceso <= 0 or proceso >= 2:
    try:
        time.sleep(1)
        print("Selecciona un número")
        time.sleep(1)
        proceso = int(input("1 = Alquilar un juego\n"))
        if proceso <= 0 or proceso >= 2:
            time.sleep(1)
            print("Valor incorrecto")
            time.sleep(2)
            try:
                os.system('cls')
            except:
                try:
                    os.system('clear')
                except:
                    pass
    except:
        time.sleep(1)
        print("Valor incorrecto")
        time.sleep(2)
        try:
            os.system('cls')
        except:
            try:
                os.system('clear')
            except:
                pass
           
if  proceso == 1:
    try:
        os.system('cls')
    except:
        try:
            os.system('clear')
        except:
            pass
    clientes = ['Abel', 'Andrés', 'Joel', 'Abelardo', 'Ángel', 'Jon','Abraham', 'Aníbal', 'Jordi', 'Adalberto', 'Antonio', 'Jorge', 'Adam', 'Arnau', 'José', 'Adán', 'Arturo', 'Jose', 'Antonio', 'Adiran', 'Asier', 'Jose Luis', 'Adolfo', 'Augusto', 'Jose Manuel', 'Aurelio', 'Jose Maria', 'Adrián', 'Baltasar', 'Juan Agustín', 'Bartolomé', 'Blas', 'Aimar', 'Basilio', 'Juan Antonio', 'Aitor', 'Benito', 'Boris', 'Alano Benjamín', 'Juan Carlos', 'Alberto', 'Bernardo', 'Borja', 'Aldo', 'Bienvenido', 'Brahim']
    juegos = ['Call of Duty', 'Fortnite', 
                'GTA V', 'League of Leguends', 
                'Just Cause 4', 'Minecraft', 
                'Final Fantasy', 'The last Guardian', 
                'nuclear throne', 'journey', 'P.T', 
                'Undertale', 'Titanfall 2']
    juegos_disponibles = juegosdisponibles(juegos, clientes)

    while alquilar == None or alquilar <= 0 or alquilar >= 3:
        try:
            time.sleep(1)
            print("Los juegos disponibles son: ")
            print("-------------------------------------------------------")
            for x in range(len(juegos_disponibles[0])):
                time.sleep(0.5)
                print("-", juegos_disponibles[0][x])
                time.sleep(0.5)
            print("-------------------------------------------------------")
            time.sleep(1)
            print("¿Desea alquilar alguno?")
            time.sleep(1)
            alquilar = int(input("Presione: 1 = Si, 2 = no \n"))
            if alquilar <= 0 or alquilar >= 3:
                time.sleep(1)
                print("Valor incorrecto")
                time.sleep(2)
                try:
                    os.system('cls')
                except:
                    try:
                        os.system('clear')
                    except:
                        pass
        except:
            time.sleep(1)
            print("Valor incorrecto")
            time.sleep(2)
            try:
                os.system('cls')
            except:
                try:
                    os.system('clear')
                except:
                    pass
    joinadmin = False
    if alquilar == 1:
        try:
            os.system('cls')
        except:
            try:
                os.system('clear')
            except:
                pass
        time.sleep(1)
        while register == None or register <= 0 or register >= 3:
            try:
                time.sleep(1)
                print("¿Quiere registrarse?")
                time.sleep(1)
                register = int(input("1 = si 2 = No \n"))
                joinadmin = admin(register)
                if joinadmin == True:
                    break
                else:
                    joinadmin = False
                
                time.sleep(1)
                if register <= 0 or register >= 3 and joinadmin != True:
                    print("Valor incorrecto")
                    time.sleep(2)
                    try:
                        os.system('cls')
                    except:
                        try:
                            os.system('clear')
                        except:
                            pass
            except:
                time.sleep(1)
                print("Valor incorrecto")
                time.sleep(2)
                try:
                    os.system('cls')
                except:
                    try:
                        os.system('clear')
                    except:
                        pass

    if alquilar == 2:
        try:
            os.system('cls')
        except:
            try:
                os.system('clear')
            except:
                pass
        print("Muchas gracias por alquilar juegos en AMATEUR PLAYERS")
        time.sleep(2)
        sys.exit()

    todo = juegos_disponibles[1]
    if joinadmin == True:
        dnisaleatorios = []
        edades = []
        tiempoalquilado = []
        for x in range(len(todo)):
            dnis1 = str(random.randint(1000, 9999))
            dnis2 = str(random.randint(1000, 9999))
            edades += [random.randint(18, 100)]
            dnisaleatorios += [dnis1 + dnis2]
            aux = random.randint(1 ,4)
            tiempoalquilado += [aux]
        
        dnies = comprobacion_dni(2, dnisaleatorios)
        try:
            os.system('cls')
        except:
            try:
                os.system('clear')
            except:
                pass
        time.sleep(1)
        print("Has entrado en modo administrador")
        time.sleep(1)
        print("verás las personas que han alquilado juegos, Nombre, edad, DNI, juego, tiempo alquilado")
        time.sleep(1)
        print("------------------------------------------------------------------------------")
        for x in range(len(todo)):
            time.sleep(1)
            if tiempoalquilado[x] == 1:
                t = "semana"
            else:
                t = "semanas"
            print(todo[x][0], "---------", edades[x], "---------", dnies[x], "-----------", todo[x][1], "-----------", tiempoalquilado[x], t)
            
        time.sleep(1)
        print("------------------------------------------------------------------------------")
        time.sleep(6)
        sys.exit()
    
    

    if register == 1:
        try:
            os.system('cls')
        except:
            try:
                os.system('clear')
            except:
                pass
        time.sleep(1)
        nombre = input("Introduce tu nombre: ")
        time.sleep(1)
        Dni = input("Introduce tu DNI: ")
        result = comprobacion_dni(1 ,Dni)
        if result == False:
            time.sleep(1)
            print("Valor incorrecto")
            
        while result != True:
            try:
                time.sleep(1)
                Dni = input("Introduce tu DNI: ")
                result = comprobacion_dni(1, Dni)
                if result != True:
                    time.sleep(1)
                    print("Valor incorrecto")
                    
            except:
                time.sleep(1)
                print("Valor incorrecto")
                    
                    
        while edad == None or edad < 18 or edad >= 100:
            try:
                time.sleep(1)
                edad = int(input("¿Cuantos años tienes?: "))
                if edad < 18:
                    time.sleep(1)
                    print("Debes ser mayor de edad para registrarte")
                    time.sleep(4)
                    try:
                        os.system('cls')
                    except:
                        try:
                            os.system('clear')
                        except:
                            pass
                elif edad >= 100:
                    time.sleep(1)
                    print("Valor incorrecto")
                    time.sleep(2)
                    try:
                        os.system('cls')
                    except:
                        try:
                            os.system('clear')
                        except:
                            pass
            except:
                time.sleep(1)
                print("Valor incorrecto")
                time.sleep(2)
                try:
                    os.system('cls')
                except:
                    try:
                        os.system('clear')
                    except:
                        pass
                        
        while rectificar == None or rectificar <= 0 or rectificar >= 3:
            try:
                time.sleep(1)
                try:
                    os.system('cls')
                except:
                    try:
                        os.system('clear')
                    except:
                        pass
                time.sleep(1)
                print("-------------------------------------------------------")
                print ("Nombre:", nombre, "\nDNI:", Dni, "\nEdad:", edad, "años")
                print("-------------------------------------------------------")
                time.sleep(1)
                rectificar = int(input("Si estos datos son correctos pulsa 1, sino pulsa 2\n"))
                if rectificar <= 0 or rectificar >= 3:
                    time.sleep(1)
                    print("Valor incorrecto")
                    time.sleep(2)
                    try:
                        os.system('cls')
                    except:
                        try:
                            os.system('clear')
                        except:
                            pass
            except:
                time.sleep(1)
                print("Valor incorrecto")
                time.sleep(2)
                try:
                    os.system('cls')
                except:
                    try:
                        os.system('clear')
                    except:
                        pass
                
        if rectificar == 2:
            while rectificar2 == None or rectificar2 <= 0 or rectificar2 >= 3:
                try:
                    try:
                        os.system('cls')
                    except:
                        try:
                            os.system('clear')
                        except:
                            pass
                    time.sleep(1)
                    print("-------------------------------------------------------")
                    print ("Nombre:", nombre, "\nDNI:", Dni, "\nEdad:", edad, "años")
                    print("-------------------------------------------------------")
                    time.sleep(1)
                    time.sleep(1)
                    rectificar2 = int(input("Si tu nombre está mal pulsa 1, si es tu edad pulsa 2\n"))
                    if rectificar2 <= 0 or rectificar2 >= 3:
                        time.sleep(1)
                        print("Valor incorrecto")
                        time.sleep(2)
                        try:
                            os.system('cls')
                        except:
                            try:
                                os.system('clear')
                            except:
                                pass
                except:
                    time.sleep(1)
                    print("Valor incorrecto")
                    time.sleep(2)
                    try:
                        os.system('cls')
                    except:
                        try:
                            os.system('clear')
                        except:
                            pass
            
            resulta2 = rectificacion(rectificar2, nombre, edad)
            if rectificar2 == 1:
                try:
                    os.system('cls')
                except:
                    try:
                        os.system('clear')
                    except:
                        pass
                time.sleep(1)
                print("-------------------------------------------------------")
                nombre = resulta2
                print ("Nombre:", nombre, "\nDNI:", Dni, "\nEdad:", edad, "años")
                print("-------------------------------------------------------")
                time.sleep(1)
                print("Tus Datos")
                time.sleep(4)
            if rectificar2 == 2:
                try:
                    os.system('cls')
                except:
                    try:
                        os.system('clear')
                    except:
                        pass
                time.sleep(1)
                print("-------------------------------------------------------")
                edad = resulta2
                print ("Nombre:", nombre, "\nDNI:", Dni, "\nEdad:", edad, "años")
                print("-------------------------------------------------------")
                time.sleep(1)
                print("Tus Datos")
                time.sleep(4)
                
            datos = cliente(nombre, Dni, edad)
        else:
            datos = cliente(nombre, Dni, edad)
    if register == 2:
        try:
            os.system('cls')
        except:
            try:
                os.system('clear')
            except:
                pass
        print("Debes registrarte para alquilar un juego")
        time.sleep(2)
        sys.exit()



try:
    os.system('cls')
except:
    try:
        os.system('clear')
    except:
        pass
time.sleep(1)       
print("Muy bien te has registrado correctamente")
time.sleep(1) 
print("Ahora procederás a elegir el juego")
time.sleep(1) 
print("Los juegos disponibles son: ")
juegoaalquilar = None

while realalquilar == None or (realalquilar < 0 or realalquilar > len(juegos_disponibles[0])) or juegoaalquilar == None:
    cont = 0
    print("-------------------------------------------------------")
    for x in range(len(juegos_disponibles[0])):
        time.sleep(0.5)
        print(cont, juegos_disponibles[0][x])
        time.sleep(0.5)
        cont += 1
    print("-------------------------------------------------------")
    try:
        time.sleep(1)
        realalquilar = int(input("¿Cuál deseas alquilar?\n"))
        if realalquilar < 0 or realalquilar > len(juegos_disponibles[0]):
            print("Valor incorrecto")
            time.sleep(2)
            try:
                os.system('cls')
            except:
                try:
                    os.system('clear')
                except:
                    pass
            juegoaalquilar = None
        else:
            juegoaalquilar = juegos_disponibles[0][realalquilar]
    except:
            time.sleep(1)
            print("Valor incorrecto")
            time.sleep(2)
            try:
                os.system('cls')
            except:
                try:
                    os.system('clear')
                except:
                    pass

try:
    os.system('cls')
except:
    try:
        os.system('clear')
    except:
        pass           
time.sleep(1)

while correcto == None or correcto <= 0 or correcto >= 3:
    try:
        print("El juego que quieres alquilar es:", juegoaalquilar)
        time.sleep(1)
        print("¿Quieres Cambiarlo?")
        correcto = int(input("1 = si 2 = No \n"))

        if correcto <= 0 or correcto >= 3:
            time.sleep(1)
            print("Valor incorrecto")
            time.sleep(2)
            try:
                os.system('cls')
            except:
                try:
                    os.system('clear')
                except:
                    pass
        else:
            
            corrección = correctooo(correcto, juegos_disponibles[0], juegoaalquilar, realalquilar)
    except:
        time.sleep(1)
        print("Valor incorrecto")
        time.sleep(2)
        try:
            os.system('cls')
        except:
            try:
                os.system('clear')
            except:
                pass

if correcto == 1:
    juegousuario = juegos_disponibles[0][corrección]
else:
    juegousuario = juegos_disponibles[0][realalquilar]

try:
    os.system('cls')
except:
    try:
        os.system('clear')
    except:
        pass
print("----------------------------------------------------------------------------------------------")
print ("Nombre:", nombre, "\nDNI:", Dni, "\nEdad:", edad, "años", "\nJuego a alquilar:", juegousuario)
print("----------------------------------------------------------------------------------------------")
time.sleep(2) 
print("Ahora procederás a introducir cuanto tiempo quieres alquilarlo")      
time.sleep(3)     

while tiempo == None or tiempo <= 0 or tiempo >= 5:
    try:
        time.sleep(1)
        try:
            os.system('cls')
        except:
            try:
                os.system('clear')
            except:
                pass
        tiempo = int(input("¿Cuanto tiempo quieres alquilar el juego?, (1,2,3 o 4 semanas), (MÁXIMO 4 SEMANAS)\n"))
        if tiempo <= 0 or tiempo >= 5:
            time.sleep(1)
            print("Valor incorrecto")
            time.sleep(2)
            try:
                os.system('cls')
            except:
                try:
                    os.system('clear')
                except:
                    pass
            tiempo = None
    except:
        time.sleep(1)
        print("Valor incorrecto")
        time.sleep(2)
        tiempo = None
        try:
            os.system('cls')
        except:
            try:
                os.system('clear')
            except:
                pass

if tiempo == 1:
    semanana = "semana"
if tiempo > 1:
    semanana = "semanas"

while correctotiempo == None or correctotiempo <= 0 or correctotiempo >= 3:

    try:
        print("El tiempo introducido para alquilar el juego es:", tiempo, semanana)
        time.sleep(1)
        print("¿Quieres Cambiarlo?")
        correctotiempo = int(input("1 = si 2 = No \n"))
        corrección1234 = correctotiempooo(correctotiempo, tiempo)
        
        if correctotiempo <= 0 or correctotiempo >= 3:
            time.sleep(1)
            print("Valor incorrecto")
            time.sleep(2)
            try:
                os.system('cls')
            except:
                try:
                    os.system('clear')
                except:
                    pass
    except:
        time.sleep(1)
        print("Valor incorrecto")
        time.sleep(2)
        try:
            os.system('cls')
        except:
            try:
                os.system('clear')
            except:
                pass

tiempo = corrección1234

if tiempo == 1:
    semanana = "semana"
if tiempo > 1:
    semanana = "semanas"

usuario = [nombre, edad, Dni, juegousuario, tiempo]

try:
    os.system('cls')
except:
    try:
        os.system('clear')
    except:
        pass
print("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
print ("Nombre:", nombre, "\nDNI:", Dni, "\nEdad:", edad, "años", "\nJuego a alquilar:", juegousuario, "\nTimpo alquilado:", tiempo, semanana)
print("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
time.sleep(1)
print("Muchas gracias por alquilar juegos en AMATEUR PLAYERS")
time.sleep(1)

salir = input("El programa ha terminado, pulse cualquier tecla para salir\n")

salirseguro = admin(salir)
if salirseguro == True:
    todo = juegos_disponibles[1]
    dnisaleatorios = []
    edades = []
    tiempoalquilado = []
    for x in range(len(todo)):
        dnis1 = str(random.randint(1000, 9999))
        dnis2 = str(random.randint(1000, 9999))
        edades += [random.randint(18, 100)]
        dnisaleatorios += [dnis1 + dnis2]
        aux = random.randint(1 ,4)
        tiempoalquilado += [aux]                
            
    dnies = comprobacion_dni(2, dnisaleatorios)
    try:
        os.system('cls')
    except:
        try:
            os.system('clear')
        except:
            pass
    time.sleep(1)
    print("Has entrado en modo administrador")
    time.sleep(1)
    print("Verás las personas que han alquilado juegos, Nombre, edad, DNI, juego, tiempo alquilado")
    time.sleep(1)
    print("------------------------------------------------------------------------------")
    for x in range(len(todo)):
        time.sleep(1)
        if tiempoalquilado[x] == 1:
            t = "semana"
        else:
            t = "semanas"
        print(todo[x][0], "---------", edades[x], "---------", dnies[x], "-----------", todo[x][1], "-----------", tiempoalquilado[x], t)
    print (nombre, "---------", edad, "---------", Dni, "---------", juegousuario, "---------", tiempo, semanana)        
    time.sleep(1)
    print("------------------------------------------------------------------------------")
else:
    print("programa terminado")
