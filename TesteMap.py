def quadrado(termo):
	return termo**2
	
elementos = [1,3,4,5,6]

map(quadrado,elementos)

resultado = list(map(quadrado,elementos))

print(resultado)
