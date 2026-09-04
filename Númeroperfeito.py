r = 's'
while r == 's':
	
	try:
		n = int(input("Digite um número a ser testado:"))
	except:
		print("Digite apenas números!")
		continue
	
	teste = 0

	for i in range(1,n):
		if n % i == 0:
			teste=teste+i
	if teste == n:
		print(n,"é um número perfeito")
	else:
		print(n,"não é um número perfeito")

	r = input("Continuar testando? (s/n): ")
