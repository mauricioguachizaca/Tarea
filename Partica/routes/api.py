from flask import Blueprint, jsonify, make_response, request
from controls.factura_controler import FacturaController
from controls.retencion_controler import RetencionController
from controls.exception.custom_exceptions import TipoRUCError
from flask_cors import CORS

api = Blueprint('api', __name__)
CORS(api)

factura_controller = FacturaController()
retencion_controller = RetencionController()

@api.route('/')
def home():
    return make_response(
        jsonify({"msg": "OK", "code": 200}),
        200
    )

@api.route('/api/facturas', methods=['POST'])
def guardar_factura():
    data = request.json
    try:
        factura = factura_controller.crear_factura(data['numero'], data['ruc'], data['monto'], data['tipo_ruc'])
        retencion = retencion_controller.agregar_retencion(factura)
        return make_response(
            jsonify({"msg": "Factura y retención guardadas correctamente", "code": 200, "data": retencion.to_dict()}),
            200
        )
    except TipoRUCError as e:
        return make_response(
            jsonify({"msg": str(e), "code": 400}),
            400
        )
    except KeyError as e:
        return make_response(
            jsonify({"msg": f"Falta el campo {str(e)}", "code": 400}),
            400
        )


@api.route('/api/retenciones', methods=['GET'])
def lista_retenciones():
    historial = retencion_controller.mostrar_historial()
    return make_response(
        jsonify({"msg": "OK", "code": 200, "data": [ret.to_dict() for ret in historial]}),
        200
    )
