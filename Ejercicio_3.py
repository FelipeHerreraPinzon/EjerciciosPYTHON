   #      Calcular el número de pulsaciones que una persona debe tener por cada 10 segundos
   #      de ejercicio, si la fórmula es:
   #      Número de pulsaciones = (220 - edad)/10

edad = int(input("Ingresa la edad "))
numeroPulsaciones = (220 - edad) / 10
numeroPulsaciones = str(numeroPulsaciones)

print('las pulsaciones por cada 10 segundos son ' + numeroPulsaciones)