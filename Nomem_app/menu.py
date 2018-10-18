from pyDatalog import  pyDatalog, pyEngine
import testing
import ui
import operaciones

def main():
    estado = True
    while estado:
        opcion = ui.menu_principal()
        if opcion == '1':
            ui.ingresar_datos_usuario()
            genero = ui.ingresar_genero()
            edad = ui.ingresar_edad()
            peso = ui.ingresar_peso()
            estatura = ui.ingresar_estatura()
            sedentarismo = ui.sedentarismo()
            print("")
            total = ui.calcular_IMC(genero, peso, estatura, edad, sedentarismo)
            print("")
            t1 = total *(3/8)
            t2 = total *(3/8)
            t3 = total *(2/8)


        elif opcion == '2':
            ui.instrucciones()
        elif opcion == '0':
            ui.mensaje_salida()
            break
        else:
            print("opcion no encontrada")


if __name__ == '__main__':
    main()