# ex36.py
# Aventura en Python
from sys import argv, exit

usuario = argv[1]

# función para la segunda decisión del usuario
def decision_2():
	asignaturas = []
	print("Bien, ahora, introduce 3 asignaturas que quieras cursar:")
	
	for x in range(0,3):
		asignaturas.append(input(f"{x+1}> "))
	
	print("\nTus asignaturas son:\n", asignaturas)
	print(f"\nY la mejor de todas, desde luego, es {asignaturas[1]}")
	fin_de_partida("Pero... lo siento, la imparten a la vez Ana, Francesc y Miguel el murciano")


# función para la primera decisión del usuario
def decision_1():
	print(f"Vas a matricularte en Ilerna Online, decide tu itinerario, {usuario}:")
	print("\t- DAM")
	print("\t- DAW")
	
	eleccion = input("> ")
	if eleccion == "DAM":
		print("Elección correcta. Los verdaderos programadores son de DAM.")
		decision_2()
	elif eleccion == "DAW":
		fin_de_partida("Al elegir DAW, viene JavaScript y te convierte en idiota.")
	else:
		fin_de_partida("No sabes seguir una indicación básica.")
	


# función para finalizar la partida
def fin_de_partida(texto):
	print(texto, "\nFIN DE LA PARTIDA.")
	exit(0)

# función para comenzar la aventura
def comenzar_aventura():
	print(f"Hola {usuario}. ¿Preparado para la aventura? (s/n).")
	
	eleccion = input("> ")
	if eleccion == "s":
		print("Excelente...\n")
		decision_1()
	elif eleccion == "n":
		fin_de_partida("Pues date media vuelta, ¡cobarde!.")
	else:
		fin_de_partida("No sabes seguir una indicación básica.")
	

# arranca el programa
comenzar_aventura()