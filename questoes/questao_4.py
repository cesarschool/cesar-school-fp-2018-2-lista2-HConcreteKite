## QUESTÃO 4 ##
#
# Escreva um programa que leia uma data do usuário e calcule seu sucessor imediato.
# Por exemplo, se o usuário inserir valores que representem 2013-11-18, seu programa 
# deve exibir uma mensagem indicando que o dia imediatamente após 2013-11-18 é 
# 2013-11-19. Se o usuário inserir valores que representem 2013-11-30, o programa deve 
# indicar que o dia seguinte é 2013-12-01. Se o usuário inserir valores que representem 
# 2013-12-31 então o programa deve indicar que o dia seguinte é 2014-01-01. A data 
# será inserida em formato numérico com três instruções de entrada separadas; 
# uma para o ano, uma para o mês e uma para o dia. Certifique-se de que o seu programa 
# funciona corretamente para anos bissextos.
##


##
# A sua resposta da questão deve ser desenvolvida dentro da função main()!!! 
# Deve-se substituir o comado print existente pelo código da solução.
# Para a correta execução do programa, a estrutura atual deve ser mantida,
# substituindo apenas o comando print(questão...) existente.
##
def main():
    data = input()
    lista_mes = "312831303130313130313031"
    resposta = ""

    bissexto = 0
    temdiaextra = True

    index = data.find("-")
    ano = int(data[0:index])
    mes = int(data[index+1:index+3])
    dia = int(data[index+4:])
    dia+=1

    if ((ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0)):
    	bissexto = 1
    dia_mes = int(lista_mes[((mes-1)*2):((mes-1)*2)+2])

    if mes == 2:
    	dia_mes += bissexto

    if dia > dia_mes:
    	dia = 1
    	mes+=1
    	if(mes > 12):
    		mes = 1
    		ano+=1

    ano = str(ano)
    mes = str(mes)
    dia = str(dia)


    print("{}-{}-{}".format(ano,mes,dia))

if __name__ == '__main__':
    main()