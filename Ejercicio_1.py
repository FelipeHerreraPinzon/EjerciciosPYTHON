
  #      Dada una cantidad en pesos, obtener la equivalencia en dólares,
  #      asumiendo que la
  #      unidad cambiaría es un dato desconocido.

cantidad = float(input("Ingrese cantidad en pesos: "))
precioDolar = float(input("¿ A cómo esta el dolar hoy ?"))

equivalenciaDolares = float(cantidad / precioDolar)
equivalenciaDolares = str(equivalenciaDolares)

print('tu dinero en dolares es ' + equivalenciaDolares)


