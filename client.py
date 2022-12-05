from pymemcache.client import base
# https://pymemcache.readthedocs.io/_/downloads/en/stable/pdf/


def initialAction():
	print("             _           _    _          ")
	print("  __ __ _ __| |_  ___ __| |__| |__ _ _ _ ")
	print(" / _/ _` / _| ' \/ -_) _` / _` / _` | '_|")
	print(" \__\__,_\__|_||_\___\__,_\__,_\__,_|_|  ")
	print("                                         ")
	print("   por  Aitor Arana Vázquez de Prada     ")
	print("                                         ")
	print("    (introduce 0 para ver la ayuda)      ")
	print("                                         ")


'''
##################################################################
#  __  __ ___ _  _ _   _   __  __ ___ _____ _  _  ___  ___  ___  #
# |  \/  | __| \| | | | | |  \/  | __|_   _| || |/ _ \|   \/ __| #
# | |\/| | _|| .` | |_| | | |\/| | _|  | | | __ | (_) | |) \__ \ #
# |_|  |_|___|_|\_|\___/  |_|  |_|___| |_| |_||_|\___/|___/|___/ #
#                                                                #
##################################################################
'''


def getOption():
	print("Selecciona una opción")
	opt = input()
	print("")
	return opt


def doAction(client, opt):
	if opt=='-1' or opt == 'q' or opt == 'exit' or opt == 'quit':
		exit("Cacheddar se ha cerrado exitosamente")
	elif opt == '0' or opt == 'h' or opt == 'help' or opt == 'man':
		showHelp()
	elif opt == '1':
		readValue(client)
	elif opt == '2':
		writeValue(client, '')
	elif opt == '3':
		deleteValue(client)
	elif opt == '4':
		updateValue(client)
	elif opt == '5':
		listAll(client)
	elif opt == '6':
		cacheLimit(client)
	elif opt == '7':
		showVersion(client)
	else:
		print("'"+str(opt)+"' no es una opción válida, usa 0 para la lista de opciones")
	
	print("")
	print("-----------------------------------------")
	print("")
	print("")


'''
#######################################
#   ___  ___ _____ ___ ___  _  _ ___  #
#  / _ \| _ \_   _|_ _/ _ \| \| / __| #
# | (_) |  _/ | |  | | (_) | .` \__ \ #
#  \___/|_|   |_| |___\___/|_|\_|___/ #
#                                     #
#######################################
'''


'''
   __  
  /  \ 
 | () |
  \__/ 
       
'''
def showHelp():
	print("-1: Salir")
	print(" 0: Ayuda")
	print(" 1: Leer valor")
	print(" 2: Escribir valor")
	print(" 3: Eliminar valor")
	print(" 4: Actualizar valor")
	print(" 5: Mostrar todos")
	print(" 6: Cambiar límite de caché")
	print(" 7: Versión de Memcached")


'''
  _ 
 / |
 | |
 |_|
    
'''
def readValue(client):
	print("Introduce la clave del campo a leer")
	key = input()
	val = client.get(key)
	if val is None:
		print("El campo", key, "está vacío")
	else:
		print(client.get(key).decode())


'''
  ___ 
 |_  )
  / / 
 /___|
      
'''
def writeValue(client, preKey):
	key = preKey
	if key == '':
		print("Introduce la clave del campo a escribir")
		key = input()
	val = client.get(key)
	decision = 'y'
	if not val is None:
		print("Ya hay un valor en", key, "¿Quieres sobreescribirlo? [y/n]")
		decision = input()
		decision = decision.lower()
	if decision == 'y':
		print("Introduce el valor para", key)
		val = input()
		client.set(key,val)
		if val == client.get(key).decode():
			print("El valor de", key, "se ha escrito exitosamente")
		else:
			print("Ha ocurrido un error, el valor no ha podido escribirse")


'''
  ____
 |__ /
  |_ \
 |___/
      
'''
def deleteValue(client):
	print("Introduce la clave del campo a borrar")
	key = input()
	val = client.get(key)
	if val is None:
		print(key, "no tiene valor")
	else:
		client.delete(key)
		if client.get(key) is None:
			print("El valor de", key, "se ha borrado exitosamente")
		else:
			print("Ha ocurrido un error, el valor no ha podido borrarse")


'''
  _ _  
 | | | 
 |_  _|
   |_| 
       
'''
def updateValue(client):
	print("Introduce la clave del campo a actualizar")
	key = input()
	val = client.get(key)
	if not val is None:
		print("Introduce el valor para", key)
		val = input()
		success = client.set(key,val)
		if success:
			print("El campo", key, "se ha actualizado exitosamente")
		else:
			print("Ha ocurrido un error, el valor no ha podido actualizarse")
	else:
		print("El campo", key, "no existe, ¿quieres crearlo? [y/n]")
		decision = input()
		decision = decision.lower()
		if decision == 'y':
			writeValue(client, key)
		
'''
  ___ 
 | __|
 |__ \
 |___/
      
'''
def listAll(client):  # https://stackoverflow.com/questions/59859057/how-to-get-all-the-keys-from-memcache-using-python
	
	print("CLAVE:     VALOR")
	keys = {}
	for key, val in client.stats('items').items():
		_, slab, field = key.decode().split(':')
		if field != 'number' or val == 0:
			continue
		item_request = client.stats('cachedump', slab, str(val + 10))
		for key, _ in item_request.items():
			print(key.decode()+": "+client.get(key.decode()).decode())



'''
   __ 
  / / 
 / _ \
 \___/
      
'''
def cacheLimit(client):
	print("Introduce el límite de MegaBytes para el sistema")
	limit = input()
	if limit.isnumeric():
		limit = int(limit)
		try:
			success = client.cache_memlimit(limit)
			print("El límite de caché se ha actualizado exitosamente")
		except Exception as e:
			print("El límite introducido no es válido:", str(e))
	else:
		print("El valor introducido no es un límite válido")


'''
  ____ 
 |__  |
   / / 
  /_/  
       
'''
def showVersion(client):
	print("Versión actual de Memcached:", client.version().decode())


'''
##############################################################
#  __  __   _   ___ _  _   __  __ ___ _____ _  _  ___  ___   #
# |  \/  | /_\ |_ _| \| | |  \/  | __|_   _| || |/ _ \|   \  #
# | |\/| |/ _ \ | || .` | | |\/| | _|  | | | __ | (_) | |) | #
# |_|  |_/_/ \_\___|_|\_| |_|  |_|___| |_| |_||_|\___/|___/  #
#                                                            #
##############################################################
'''


if __name__ == "__main__":
	initialAction()
	client = base.Client(('127.0.0.1',11211))
	while True:
		opt = getOption()
		doAction(client, opt)


