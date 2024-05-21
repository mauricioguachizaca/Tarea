from flask import Blueprint, render_template, redirect, request, jsonify, make_response
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

@router.route('/facturas/<int:id>', methods=['GET'])
def obtener_factura(id):
    factura = factura_controller.obtener_factura(id)
    if factura:
        return jsonify(factura.to_dict())
    return make_response(f"Factura con ID {id} no encontrada", 404)

@router.route('/facturas/eliminar/<int:id>', methods=['POST'])
def eliminar_factura(id):
    if factura_controller.eliminar_factura(id):
        return '', 204
    else:
        return make_response(f"Factura con ID {id} no encontrada", 404)

@router.route('/facturas/editar/<int:id>', methods=['POST'])
def editar_factura(id):
    data = request.form
    try:
        factura = factura_controller.editar_factura(id, data['numero'], data['ruc'], float(data['monto']), data['tipo_ruc'])
        if factura:
            retencion_controller.actualizar_retencion(factura)
            return '', 204
        else:
            return make_response(f"Factura con ID {id} no encontrada", 404)
    except TipoRUCError as e:
        return make_response(str(e), 400)
    except KeyError as e:
        return make_response(f"Falta el campo {str(e)}", 400)
