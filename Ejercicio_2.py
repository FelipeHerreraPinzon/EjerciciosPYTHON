 #  La presión, el volumen y la temperatura de una masa de aire se relacionan por la
  #        fórmula:
   #       Masa = (presión * volumen)/(0.37 * (temperatura + 460)

volumen = float(input("Ingrese volumen "))
presion = float(input("Ingrese presión "))
temperatura = float(input("Ingrese temperatura "))

masa = float((presion * volumen) / (0.37 * (temperatura + 400)))
masa = str(masa)

print('la masa es : ' + masa)


