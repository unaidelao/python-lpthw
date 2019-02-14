# Una breve historia con diferentes elecciones.

print("""Te despiertas en una barca, en mitad de un lago,
¿qué haces?:
1. Mirar a tu alrededor.
2. Volver a dormirte.""")

eleccion1 = input("> ")

if eleccion1 == "1":
	print("Ves a tu izquierda, lejos, tierra firme. Y a tu derecha,")
	print("ves una isla de mediano tamaño. ¿Qué haces?:")
	print("1. Decides ir a tierra firme.")
	print("2. Mejor vas a la isla.")
	
	eleccion2 = input("> ")
	
	if eleccion2 == "1":
		print("No tienes remos, así que intentas dar empuje con la")
		print("mano, pero sólo consigues dar vueltas como una peonza.")
		print("FIN.")
	elif eleccion2 == "2":
		print("Antes de llegar te ataca un calamar gigante.")
		print("Mala suerte. FIN.")
	else:
		print("Tu originalidad en la respuesta ha sido premiada")
		print("con una muerte instantánea de tu personaje.")
		print("Mala suerte. FIN.")
	
elif eleccion1 == "2":
	print("Al volver a dormirte te despiertas, esta vez de verdad.")
	print("¡Qué sueño más tonto!. FIN.")
else:
	print("¿No te sirven las dos opciones que te he dado? Vaya...")
	print("Pues por inconformista, tu personaje resulta que se le")
	print("ocurre mirar a ver qué hay debajo del agua, y se cae, y")
	print("¡fíjate por donde! No sabe nadar. FIN.")