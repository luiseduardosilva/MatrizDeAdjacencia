"""
	ESTRUTURAS DE DADOS II
	By: LuisSilva - 10.06.2018
"""

linha = "+"+("-" *75)+"+"
matriz 		= []
listaOD 	= []
listaP 		= []

# CRIA MATRIZ
def criaMatriz(tamanho, matriz):
	linha = []
	for i in range(0 ,tamanho+1):
		linha = []
		for x in range(0, tamanho+1):
			linha.append(" ")
		matriz.append(linha)

# MUDAR VALORES DA MATRIZ
def mudaValor(listaOD, listaP, matriz):
	matriz[0][0] = "X"
	contador = 0
	for letra in listaOD:
		matriz[0][contador+1] = letra[0]
		matriz[contador+1][0] = letra[1]
		matriz[contador+1][contador+1] = listaP[contador]
		print("+"+("-"*33 +" ") +letra[0] + " -> "+letra[1]+ " "+("-"*34)+"+")
		mostraMatriz(matriz)
		contador = contador +1

# EXIBE MATRIZ
def mostraMatriz(matriz):
	for linha in (matriz):
		print(linha)

# MENU
def menu():
	print(linha+"""\n
	[+] Representação de Grafos – Matriz de Adjacência
	[+] By: LuisSilva
	[+] GitHub: github.com/luiseduardosilva
	[+] Python 3.x+
	[+] Exit "."
	\n"""+linha)

# START 
def start():
	verO 	= ""
	verD 	= ""
	while (verO != "." and verD != "."):
		verO = input("	ORIGEM: \n 		->")
		verD = input("	DESTINO: \n 		->")
		verP = input("	PESO: \n 		->")
		print("+"+("-" *75)+"+")
		if verO == "." or verD == ".":
			pass
		elif verO == "" or verD == "" or len(verO) >= 2 or len(verD) >= 2:
			print("VALOR NAO VALIDO![1]")
		else:
			if len(listaOD) >= 1:
				if verO.upper()+verD.upper() in listaOD or verD.upper()+verO.upper() in listaOD:
					print("VALOR NAO VALIDO[2]")
				else:
					listaOD.append(verO.upper() + verD.upper())
					listaP.append(verP.upper())	
			else:
				listaOD.append(verO.upper()+verD.upper())
				listaP.append(verP.upper())

menu()
start()
criaMatriz(len(listaOD), matriz)
mudaValor(listaOD, listaP, matriz)
print(linha)
