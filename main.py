'''
Labelling App

C. Fdez
rev 0
16/11/2024

Aplicación para la reimpresión de etiquetas de packaging para nodos

La aplicación trabaja con credenciales de usuario limitando el acceso a funcionalidades de parametrización
general
En primer plano la interface debe presentar las opciones de etiqueta a reimprimir
Un cuadro de texto será el encargado de gestionar el filtro de búsqueda
Una vez localizados los datos de la etiqueta buscada, se rellenarán 3 o las necesarias etiquetas
de manera que el usuario pueda reconocer y validar la etiqueta.
En un cuadro de imagen se mostrará la etiqueta definitiva y se activará la opción de imprimir

Los datos de origen se cargarán desde un archivo Excel, el cual se recorrerá generando un diccionario
por cada una de las filas de la pestaña que contiene los datos.

Usaremos label_generator.py para la creación de la etiqueta


En el menú de setup, bloqueado por las credenciales del usuario logeado, se definirán:
    - La impresora
    - El archivo fuente  (su ruta completa)
    - las dimensiones de la etiqueta

TO DO

    [] main.py
        [] la interface en formato html
        [] las url para las pantallas de trabajo y de setup
        [] El archivo de usuarios con sus contraseñas
        []  

'''
from flask import Flask
from src.routes import bp
#from src import create_app

app = Flask(__name__)
#app = create_app()

app.register_blueprint (bp)



if __name__ == "__main__":
    app.run(debug=True)