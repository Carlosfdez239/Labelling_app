'''
Importa archivo Excel y recorre las filas de una pestaña creando
un diccionario por fila, usando la primera fila como clave

C. Fdez
16/11/2024
Rev 0


    ARCHIVO_EXCEL = "archivo.xlsx"
    PESTANA = "nombre_de_la_hoja"

TO DO

    [] Cargar y configurar el archivo fuente
    [] Crear los diccionarios
    [] Exportar los datos según parámetro de llamada del método

'''

import openpyxl

def Procesar_Excel(EXCEL, PESTANA):
    '''
    EXCEL --> ruta completa y nombre del archivo Excel.xlsx;
    PESTANA --> Nombre de la hoja;
    '''
    ArchivoExcel = EXCEL
    Pestana = PESTANA
    # Carga del archivo Excel
    wb = openpyxl.load_workbook(ArchivoExcel)
    
    # Selecciona la pestaña fuente de los datos
    hoja = wb[Pestana]

    # Crear la lista para almacenar los diccionarios
    datos = []

    # Se recorren las filas de la hoja asumiendo que las claves están en la primera fila
    encabezados = [celda.value for celda in hoja[1]]

    # Se leen las filas restantes y almacenarlas como diccionarios
    for fila in hoja.iter_rows(min_row=2, values_only=True):
        fila_diccionario = {encabezados[i]: fila[i] for i in range(len(encabezados))}
        datos.append(fila_diccionario)
    
    # Imprimir los datos
    for registro in datos:
        print(registro)

    # Cerramos el archivo
    wb.close()
    return datos


if __name__ == "__main__":
    Procesar_Excel("/home/casa/Documentos/Worldsensing/Pruebas/Packing_List_EN24-00445.xlsx","Contenido")