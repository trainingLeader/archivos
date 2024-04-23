import modules.corefiles as cf
import funciones.globales as gf
import funciones.alumno as st
import main

def MenuStudent(op : int):
    title = """
    *******************************************
    * MODULO ADMIN ESTUDIANTES CAMPUSACADEMIC *
    *******************************************
    """
    menuStudentOp = '1. Agregar\n2. Editar\n3. Eliminar\n4. Salir'
    gf.borrar_pantalla()
    if (op != 4):
        print(title)
        print(menuStudentOp)
        try:
            op = int(input(":) "))
        except ValueError:
            print("Opcion no tiene formato adecuado")
            gf.pausar_pantalla()
            MenuStudent(0)
        else:
            match (op):
                case 1:
                    st.NewStudent()
                case 2:
                    pass
                case 3:
                    pass
                case 4:
                    main.mainMenu(0)
                case _:
                    print("La opcion ingresada no esta disponible en las opciones")
                    gf.pausar_pantalla()