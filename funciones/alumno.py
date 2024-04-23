import os
import json
import funciones.globales as gf
import modules.corefiles as cf
import ui.uiStudent as uisSt
def NewStudent():
    title = """
    ***************************
    * REGISTRO DE ESTUDIANTES *
    ***************************
    """
    gf.borrar_pantalla()
    print(title)
    identificacion = input("Ingres el Nro de Identificacion : ")
    codStudent = input("Ingrese Codigo del estudiante :")
    nombreStudent = input("Ingrese Nombre Estudiante : ")
    estudiante = {
        'identificacion': identificacion,
        'codStudent': codStudent,
        'nombreStudent': nombreStudent,
        'notas' : {
            'parciales' : {},
            'quices' : {},
            'trabajos' : {}
        }
    }
    cf.AddData('data',identificacion,estudiante)
    gf.campusAcademic.get('data').update({identificacion:estudiante})
    if(bool(input('Desea registrar otro estudiante S(Si) o Enter(No)'))):
        NewStudent()
    else:
       uisSt.MenuStudent(0)



