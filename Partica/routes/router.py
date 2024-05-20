from flask import Blueprint, render_template, redirect, request, abort
from controls.factura_controler import FacturaController
from controls.retencion_controler import RetencionController
from controls.exception.custom_exceptions import TipoRUCError
from flask import make_response

router = Blueprint('router', __name__)

factura_controller = FacturaController()
retencion_controller = RetencionController()

@router.route('/')
def home():
    return render_template('home.html')

@router.route('/facturas')
def ver_facturas():
    historial = retencion_controller.mostrar_historial()
    return render_template('facturas/lista.html', lista=historial)

@router.route('/facturas/formulario')
def ver_guardar():
    return render_template('facturas/guardar.html')

@router.route('/facturas/guardar', methods=['POST'])
def guardar_factura():
    data = request.form
    try:
        factura = factura_controller.crear_factura(data['numero'], data['ruc'], float(data['monto']), data['tipo_ruc'])
        retencion_controller.agregar_retencion(factura)
        return redirect('/facturas', code=302)
    except TipoRUCError as e:
        return make_response(str(e), 400)
    except KeyError as e:
        return make_response(f"Falta el campo {str(e)}", 400)
    
@router.route('/facturas/modificar', methods=['POST'])
def modificar_factura():
    data = request.form
    pos = int(data['id']) - 1
    historial = retencion_controller.mostrar_historial()
    try:
        factura = historial[pos].factura
        factura_controller.modificar_factura(factura, data)
        retencion_controller.actualizar_retencion(pos, factura)
        return redirect('/facturas', code=302)
    except IndexError:
        return make_response("Índice fuera de rango", 400)
    except KeyError as e:
        return make_response(f"Falta el campo {str(e)}", 400)
