## QUESTÃO 2 ##
#
# Um robô se move em um plano a partir do ponto original (0,0). O robô pode se 
# mover nas direções CIMA, BAIXO, ESQUERDA e DIREITA de acordo com um 
# passo fornecido. O traço do movimento do robô é mostrado da seguinte forma:
#
# CIMA 5
# BAIXO 3
# ESQUERDA 3
# DIREITA 2
#
# Os números após a direção são passos. 
# Escreva um programa para calcular a distância entre a posição atual e o 
# ponto original após uma seqüência de movimentos. Se a distância for um 
# float, basta imprimir o inteiro mais próximo.
# Exemplo:
# Se as seguintes tuplas são dadas como entrada para o programa:
# 
# CIMA 5
# BAIXO 3
# ESQUERDA 3
# DIREITA 2
#
# Então, a saída do programa deve ser:
# 2
# 
# Dicas:
# As entradas devem ser lidas do console até que um valor vazio seja digitado. 
# A saída deve ser um inteiro que representa a distancia para o ponto original. 
# Entradas inválidas devem ser descartadas da contagem.
##


##
# A sua resposta da questão deve ser desenvolvida dentro da função main()!!! 
# Deve-se substituir o comado print existente pelo código da solução.
# Para a correta execução do programa, a estrutura atual deve ser mantida,
# substituindo apenas o comando print(questão...) existente.
##
def main():
    x = 0.0
    y = 0.0
    distancia = 0.0
    print("Digite as Entradas: \n")
    while True:
    	comando = input()
    	if comando == "":
    		break

    	size = len(comando)
    	index = comando.find(" ")

    	if index == -1:
    		print("Comando Inválido")
    		continue
    		
    	direcao = comando[0:index]
    	modulo = comando[index+1:]

    	if direcao == "CIMA":
    		x+= float(modulo)
    	elif direcao == "BAIXO":
    		x+= float(modulo) * -1
    	elif direcao == "DIREITA":
    		y+= float(modulo)
    	elif direcao == "ESQUERDA":
    		y+= float(modulo) * -1
    	else:
    		print("Comando Inválido")
    		continue

    	temp = pow(x,2) + pow(y,2)
    	distancia = pow(temp,0.5)
    	distancia = int(distancia)

    print(distancia)








    
if __name__ == '__main__':
    main()