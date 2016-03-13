#Saber si alguien es mayor de edad
edad = int(raw_input("Ingresa tu edad"))
if edad >=18 and edad <=54:
	print "Eres mayor de edad, adelante"
elif edad >= 55:
	print "Eres muy mayor de edad, deja de tomar"
else:
	print "Oye!! eres menor, no puedes tomar!! vete!!!"
