import modules.corefiles as cf
import funciones.globales as fg
import ui.uiStudent as uiSt
def mainMenu(op):
    fg.borrar_pantalla()
    title = """
    *********************************************
    * SISTEMA GESTION DE NOTAS - CAMPUSACADEMIC *
    *********************************************
    """
    mainMenuOp = "1. Gestion estudiantes\n2. Gestion de notas\n3. Salir"
    if (op != 3):
        print(title)
        print(mainMenuOp)
        try:
            opcion = int(input(':) '))
        except ValueError:
            print('Error en la opcion ingresada')
            fg.pausar_pantalla()
            mainMenu(0)
        else:
            match (opcion):
                case 1:
                    uiSt.MenuStudent(0)
                case 2:
                    pass
                case 3:
                    print("Regrese pronto ....")
                    fg.pausar_pantalla()
                case _:
                    print('Opcion ingresada no pertenece al menu de opciones')
                    fg.pausar_pantalla()
                    mainMenu(0)
if __name__ == '__main__':
    cf.MY_DATABASE = 'data/alumnos.json'
    cf.checkFile(fg.campusAcademic)
    mainMenu(0)
