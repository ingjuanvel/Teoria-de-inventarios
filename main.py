import math  #importamos la libreria math para usar algunas funciones matemáticas que necesitemos

D = int(input("Ingrese el valor de la demanda diaria de productos: ")
        )  #definimos el valor de la demanda diaria
K = int(input("Ingrese el valor del costo del pedido: ")
        )  #definimos el valor de costo de pedido
h = int(
  input("Ingrese el valor del costo diario de almacenamiento por unidad: ")
)  #costo de almacenamiento por unidad por dia
L = int(input("Ingrese el tiempo de espera de llegada de un pedido en dias: ")
        )  #tiempo de espera de llegada de un pedido

y = math.sqrt(
  (2 * D * K) / (h)
)  #cálculo de la cantidad óptima de pedido utilizando la fórmula para minimizar los costos totales de inventario
Le = L * D  #Calculamos la cantidad de unidades que deben haber para volver a hacer un pedido
print(
  "La cantidad optima de pedido es: {:.2f} unidades cuando el inventario se reduzca a {:.2f}"
  .format(y, Le))
