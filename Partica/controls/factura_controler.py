from models.factura import Factura
from controls.exception.custom_exceptions import TipoRUCError

class FacturaController:
    def __init__(self):
        self.facturas = []
        self.current_id = 1

    def crear_factura(self, numero, ruc, monto, tipo_ruc):
        if tipo_ruc not in ['educativo', 'profesional']:
            raise TipoRUCError(tipo_ruc)

        # Crear una instancia de Factura
        factura = Factura(id=self.current_id, numero=numero, ruc=ruc, monto=monto, tipo_ruc=tipo_ruc)
        self.current_id += 1
        
        # Agregar la factura a la lista de facturas
        self.facturas.append(factura)
        
        # Devolver la factura creada
        return factura

    def obtener_factura(self, id):
        for factura in self.facturas:
            if factura.id == id:
                return factura
        return None

    def eliminar_factura(self, id):
        factura = self.obtener_factura(id)
        if factura:
            self.facturas.remove(factura)
            return True
        return False


