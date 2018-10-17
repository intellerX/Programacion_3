import os


def limpiar_pantalla():
    os.system('clear')


def mensaje_salida():
    limpiar_pantalla()
    print(""" 
			----------------------------------------------------------------------------
									Usted ha salido de la aplicacion
			----------------------------------------------------------------------------
	""")


def menu_principal():
    print("""
			NOMEM - Aplicacion para la creacion de dietas para los colombianos
			----------------------------------------------------------------------------
											Menu Principal
			----------------------------------------------------------------------------
			----------------------------------------------------------------------------
			1. Ingresar datos de usuario
			2. Instrucciones de uso
			0. Salir del programa
	""")
    opcion = raw_input('Digite su opcion: ')
    return opcion


def ingresar_datos_usuario():
    print("""
		   Ingrese su genero: 
		   1. masculino
		   2. femenino
		   ----------------------------------------------------------------------------
	""")

    genero = float(input("  Digite su opcion: "))

    edad = float(input("    Ingrese su edad: "))

    peso = float(input("    Ingrese su peso en kilogramos: "))

    estatura = float(input("    Ingrese su estatura en centimetros: "))

    print(""" 
		   Ingrese su nivel de sedentarismo:
		   1. una persona que no hace ejercicio.
		   2. deporte de 1-3 veces por semana.
		   3. deporte de 3-5 veces por semana.
		   4. deporte de 6-7 veces por semana.
		   5. deporte mas de una vez por dia.
		   ----------------------------------------------------------------------------
	""")

    sedentarismo = float(input("    Digite su opcion: "))


    if genero == 1:
        if sedentarismo == 1:
            Total = float((66.473 + (13.751 * peso) + (5.0033 * estatura) - (6.7550 * edad)) * 1.2)
        elif sedentarismo == 2:
            Total = float((66.473 + (13.751 * peso) + (5.0033 * estatura) - (6.7550 * edad)) * 1.375)
        elif sedentarismo == 3:
            Total = float((66.473 + (13.751 * peso) + (5.0033 * estatura) - (6.7550 * edad)) * 1.375)
        elif sedentarismo == 4:
            Total = float((66.473 + (13.751 * peso) + (5.0033 * estatura) - (6.7550 * edad)) * 1.725)
        elif sedentarismo == 5:
            Total = float((66.473 + (13.751 * peso) + (5.0033 * estatura) - (6.7550 * edad)) * 1.9)

    else:
        if sedentarismo == 2:
            Total = float((655.1 + (9.463 * peso) + (1.8 * estatura) - (4.6756 * edad)) * 1.2)
        elif sedentarismo == 2:
            Total = float((655.1 + (9.463 * peso) + (1.8 * estatura) - (4.6756 * edad)) * 1.375)
        elif sedentarismo == 3:
            Total = float((655.1 + (9.463 * peso) + (1.8 * estatura) - (4.6756 * edad)) * 1.55)
        elif sedentarismo == 4:
            Total = float((655.1 + (9.463 * peso) + (1.8 * estatura) - (4.6756 * edad)) * 1.725)
        elif sedentarismo == 5:
            Total = float((655.1 + (9.463 * peso) + (1.8 * estatura) - (4.6756 * edad)) * 1.9)

    print(" La cantidad de calorias para su consumo son: "+str(int(Total)))
    pass
    return 0


ingresar_datos_usuario()