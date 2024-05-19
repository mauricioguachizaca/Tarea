from controls.factura_controler import FacturaController
from controls.retencion_controler import RetencionController
from controls.exception.custom_exceptions import TipoRUCError

def main():
    factura_controller = FacturaController()
    retencion_controller = RetencionController()

    while True:
        print("\n1. Ingresar nueva factura")
        print("2. Mostrar historial de retenciones")
        print("3. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            numero = input("Ingrese el número de la factura: ")
            ruc = input("Ingrese el RUC: ")
            monto = float(input("Ingrese el monto: "))
            tipo_ruc = input("Ingrese el tipo de RUC (educativo/profesional): ").lower()
            try:
                factura = factura_controller.crear_factura(numero, ruc, monto, tipo_ruc)
                retencion_controller.agregar_retencion(factura)
            except TipoRUCError as e:
                print(e.message)
        elif opcion == '2':
            retencion_controller.mostrar_historial()
        elif opcion == '3':
            break
        else:
            print("Opción no válida. Intente nuevamente.")

if __name__ == "__main__":
    main()

