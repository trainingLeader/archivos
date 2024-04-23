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

def SearchData():
    criterio = input('Ingrese el Nro Identificacion del estudiante: ')
    data=gf.campusAcademic.get('data').get(criterio)
    return data
    

def ModifyData():
    dataStudent = SearchData()
    identificacion,codStudent,nombreStudent,notas = dataStudent.values()
    for key in dataStudent.keys():
        if (key != 'identificacion' and key != 'notas'):
            if(bool(input(f'Desea modificar el {key} s(si) o Enter No'))):
                dataStudent[key] = input(f'Ingrese el nuevo valor para {key} :')
    gf.campusAcademic.get('data').update({identificacion:dataStudent})
    cf.UpdateFile(gf.campusAcademic)
    uisSt.MenuStudent(0)
