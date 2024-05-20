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

    def obtener_factura(self, numero):
        for factura in self.facturas:
            if factura.numero == numero:
                return factura
        return None

    def eliminar_factura(self, numero):
        factura = self.obtener_factura(numero)
        if factura:
            self.facturas.remove(factura)
            return True
        return False

    def editar_factura(self, numero, nuevo_numero, nuevo_ruc, nuevo_monto, nuevo_tipo_ruc):
        factura = self.obtener_factura(numero)
        if factura:
            factura.numero = nuevo_numero
            factura.ruc = nuevo_ruc
            factura.monto = nuevo_monto
            factura.tipo_ruc = nuevo_tipo_ruc
            return factura
        return None
