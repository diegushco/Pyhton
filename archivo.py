#Escribir en un archivo
archivo = open("archivo_texto.txt","w")
for n in range(200,301):
	archivo.write("%d \n" %n);
archivo.close();

print "\n\n\n\n"
print "Leyendo el archivo\n\n"
archivo = open("archivo_texto.txt","r")
for linea in archivo.readlines():
	print linea.strip("\n")
archivo.close()
