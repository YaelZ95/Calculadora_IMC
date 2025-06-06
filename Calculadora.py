nombre = ""
apellido_p = ""
apellido_m = ""
edad = 0
peso = 0
estatura = 0
IMC = 0

import time
#Proceso de impresion de datos IMC con animacion de carga
def imprimir_datos_y_IMC(duracion_animacion=5):
    #Esto se usa para la animacion de carga
    animacion = "|/-\\"
    tiempo_final = time.time() + duracion_animacion
    i = 0
    #Muestra el mensaje de inicio del proceso
    print("\nCalculando e imprimiendo datos")
    #Aqui calcula el IMC
    IMC = float(peso)/(float(estatura)*float(estatura))
    #Animacion de carga
    while time.time() < tiempo_final:
        print(f'\rEspere un momento... {animacion[i % len(animacion)]}', end='')
        time.sleep(0.1)
        i += 1
    #Imprime el finalizado del proceso junto con los datos proporcionados y el IMC calculado
    print("\rProceso completado con exito\n")
    print("Tu nombre completo es: "+str(nombre)+" "+str(apellido_p)+" "+str(apellido_m))
    print("Tienes "+str(edad)+" años\nPesas "+str(peso)+" kilogramos\nTu estatura es de "+str(estatura)+" metros\ny tu Indice de Masa Corporal (IMC) es de "+str(round(IMC, 2))+" kg/m")

print("Calculadora de I.M.C hecho por Yael Zuñiga Garcia\nPara conocer tu I.M.C es necesario que llenes el siguiente formulario\n")
nombre = input("Introduce tu nombre (sin apellidos)\n")

apellido_p = input("Introduce tu apellido paterno\n")

apellido_m = input("Introduce tu apellido materno\n")

edad = input("Introduce tu edad actual\n")
while True:
    try: 
        int(edad)
        break
    except ValueError:
        edad = input("Error en el valor, Ingresa tu edad en numeros enteros\n")

peso = input("Introduce tu peso en kilogramos\n")
while True:
    try:
        float(peso)
        break
    except ValueError:
        peso = input("Error en el valor, Ingresa tu peso en numeros enteros o con decimales\n")

estatura = input("Introduce tu estatura en metros\n")
while True:
    try:
        float(estatura)
        break
    except ValueError:
        estatura = input("Error en el valor, Ingresa tu estatura en numeros enteros con decimales\n")

imprimir_datos_y_IMC()
