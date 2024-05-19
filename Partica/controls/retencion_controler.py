from models.retencion import Retencion
from controls.dao.historial_dao import HistorialDAO
from controls.tda.linked_list import LinkedList
import os

class RetencionController:
    def __init__(self):
        self.historial = LinkedList()
        self.dao = HistorialDAO()
        self.cargar_historial()

    def agregar_retencion(self, factura):
        retencion = Retencion(factura)
        self.historial.append(retencion)
        self.dao.guardar_historial(self.historial)

        folder_path = 'partica/Taller/data'

        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
        return retencion

    def cargar_historial(self):
        self.historial = self.dao.cargar_historial()

    def mostrar_historial(self):
        for retencion in self.historial:
            print(retencion)
