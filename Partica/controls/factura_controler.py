from models.factura import Factura
from controls.exception.custom_exceptions import TipoRUCError

class FacturaController:
    def __init__(self):
        self.facturas = []

    def crear_factura(self, numero, ruc, monto, tipo_ruc):
        if tipo_ruc not in ['educativo', 'profesional']:
            raise TipoRUCError(tipo_ruc)
        
        # Crear una instancia de Factura
        factura = Factura(numero=numero, ruc=ruc, monto=monto, tipo_ruc=tipo_ruc)
        
        # Agregar la factura a la lista de facturas
        self.facturas.append(factura)
        
        # Devolver la factura creada
        return factura
