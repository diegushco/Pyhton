import configparser
configuracion = configparser.ConfigParser()



config_file = 'archivo_conf'

configuracion.read(config_file);

nombre = configuracion.get("Humano","nombre")
apellido = configuracion.get("Humano","apellido")
edad = configuracion.get("Humano","edad")

print nombre
print apellido
print edad

#averiguar de beautifilsoap
#tambien de urllib2

#para base de datos con mysql, toca instalar MYSQLdb
#pentesting y fuzzers?
#paht.basename
#path.abspath