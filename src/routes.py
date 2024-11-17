from flask import Blueprint, render_template, request
from lib.Procesador import Procesar_Excel

bp = Blueprint("main", __name__)

@bp.route('/')
def index():
    #return render_template('index.html')
    return render_template('parametros.html')

@bp.route('/')
def principal():
    #return render_template('index.html')
    return render_template('index.html')

@bp.route('/procesar', methods=["POST"])
def procesar():
    ruta_excel = request.form["ruta_excel"]
    hoja_excel = request.form["hoja_excel"]

    try:
        datos = Procesar_Excel(ruta_excel, hoja_excel)
        return f"Datos procesados con exito: {datos}"
    except Exception as e:
        return f"Error al procesar el archivo: {e}"