from models.factura import Factura

class Retencion:
    def __init__(self, factura: Factura):
        self.factura = factura
        self.retencion = self.calcular_retencion()

    def calcular_retencion(self):
        if self.factura.tipo_ruc == 'educativo':
            return self.factura.monto * 0.08
        elif self.factura.tipo_ruc == 'profesional':
            return self.factura.monto * 0.10
        else:
            return 0

    def __repr__(self):
        return f"Factura Nro: {self.factura.numero}, RUC: {self.factura.ruc}, Monto: {self.factura.monto}, Retención: {self.retencion}"
