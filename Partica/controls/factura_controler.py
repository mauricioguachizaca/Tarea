from models.factura import Factura
from controls.exception.custom_exceptions import TipoRUCError

class FacturaController:
    def __init__(self):
        self.facturas = []

    def crear_factura(self, numero, ruc, monto, tipo_ruc):
        if tipo_ruc not in ['educativo', 'profesional']:
            raise TipoRUCError(tipo_ruc)
        factura = Factura(numero, ruc, monto, tipo_ruc)
        self.facturas.append(factura)
        return factura
