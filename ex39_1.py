# función para comprobar si existe un key dentro de un diccionario
def comprueba_posiciones(diccionario, posicion):
	if posicion in diccionario:
		print(f"{posicion} SI existe en {diccionario}")
	else:
		print(f"{posicion} NO existe en {diccionario}")

# posiciones de fútbol
posiciones = {
	'Portero':'POR',
	'Defensa':'DEF',
	'Centro Campista': 'MC',
	'Delantero':'DEL'
}

# ejemplo de algunos jugadores
grandes_jugadores = {
	'POR':'Oliver Khan',
	'DEF':'Roberto Carlos',
	'MC':'Zinedine Zidane',
	'DEL':'Éric Cantona'
}

print('-' * 20)
print("Ejemplo de un gran portero: ", grandes_jugadores['POR'])

print('-' * 20)
print(f"La abreviatura para defensa se dice: {posiciones['Defensa']}")

print('-' * 20)
print("Longitud del diccionario 'posiciones': ", len(posiciones))
print("Longitud del diccionario 'grandes_jugadores': ", len(grandes_jugadores))

print('-' *20)
print("Vamos a realizar unas comprobaciones...")
comprueba_posiciones(posiciones, 'Delantero')
comprueba_posiciones(grandes_jugadores, 'Cristiano Ronaldo')

print('-' *20)
print("Se actualiza el valor del delantero:\n")
grandes_jugadores['DEL'] = 'Emilio Butragueño'
print("Ahora grandes_jugadores contiene:")

for x, y in grandes_jugadores.items():
	print(x,'=>',y)
	
print('-' * 20)
print("Eliminamos el key 'Centro Campista' y añadimos el de 'Utillero'")
del posiciones['Centro Campista']
posiciones ['Utillero'] = 'Perico el utillero'
print(posiciones)

print('-' * 20)
print("Vaciamos el diccionario 'grandes_jugadores':")
grandes_jugadores.clear()
print(grandes_jugadores)

print('-' * 20)
print("Vaciamos el diccionario 'posiciones':")
del posiciones
print(posiciones)