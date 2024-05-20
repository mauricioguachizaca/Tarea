from flask import Blueprint, render_template, redirect, request, make_response
from controls.factura_controler import FacturaController
from controls.retencion_controler import RetencionController
from controls.exception.custom_exceptions import TipoRUCError

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

@router.route('/facturas/editar/<int:numero>', methods=['GET', 'POST'])
def editar_factura(numero):
    if request.method == 'GET':
        factura = factura_controller.obtener_factura(numero)
        if factura:
            return render_template('facturas/editar.html', factura=factura)
        else:
            return make_response("Factura no encontrada", 404)
    elif request.method == 'POST':
        data = request.form
        try:
            nueva_factura = factura_controller.editar_factura(numero, data['nuevo_numero'], data['nuevo_ruc'], float(data['nuevo_monto']), data['nuevo_tipo_ruc'])
            if nueva_factura:
                return redirect('/facturas', code=302)
            else:
                return make_response("Factura no encontrada", 404)
        except KeyError as e:
            return make_response(f"Falta el campo {str(e)}", 400)

@router.route('/facturas/eliminar/<int:numero>', methods=['POST'])
def eliminar_factura(numero):
    if request.method == 'POST':
        if factura_controller.eliminar_factura(numero):
            return redirect('/facturas', code=302)
        else:
            return make_response("Factura no encontrada", 404)

