## QUESTÃO 1 ##
#
# Um site exige que os usuários insiram nome de usuário e senha para se registrarem. 
# Escreva um programa para verificar se a senha digitada pelos usuários é forte o suficiente.
# A seguir estão os critérios para verificar a senha:
#
# 1. Pelo menos uma letra entre [a-z]
# 2. Pelo menos 1 número entre [0-9]
# 3. Pelo menos uma letra entre [A-Z]
# 4. Pelo menos 1 caractere de [$ # @]
# 5. Comprimento mínimo da senha: 6
# 6. Comprimento máximo da senha: 12
#
# Seu programa deve aceitar uma sequência de senhas separadas por vírgula e as verificará 
# de acordo com os critérios acima. As senhas que correspondem aos critérios devem ser 
# impressas, separadas por uma vírgula.
# Exemplo
# Se as seguintes senhas forem fornecidas como entrada para o programa:
# ABd1234@1, umF1#, 2w3E*, 2We3345
# Então, a saída do programa deve ser:
# ABd1234@1
##

##
# A sua resposta da questão deve ser desenvolvida dentro da função main()!!! 
# Deve-se substituir o comado print existente pelo código da solução.
# Para a correta execução do programa, a estrutura atual deve ser mantida,
# substituindo apenas o comando print(questão...) existente.
##
def main():
    
    senhas = input("Digite as senhas:")
    senha = ""
    resposta = ""
    size_senhas = len(senhas)
    i = 0
    index = 0
    count = 0
    while i < size_senhas:
    
        if senhas[i] == ',' or i+1 == size_senhas:
            senha = senhas[index:i]
            size_senha = len(senha)
            if size_senha < 6 or size_senha > 18:
                index += 2
                i+=1
                continue
            j=0
            temp = 0

            while j < size_senha:
                test = ""
                test = senha[j]
                if ord(test) in range(ord("a"),ord("z")+1):
                    temp+=1
                elif ord(test) in range(ord("@"),ord("Z")+1):
                    temp+=1
                elif ord(test) in range(ord("0"),ord("9")+1):
                    temp+=1
                elif ord(test) in range(ord("#"),ord("$")+1):
                    temp+=1
                j+=1

            if temp == size_senha:
                if count == 0:
                    resposta += senha
                else:
                    resposta += ', '
                    resposta += senha
                count+=1
            else:
                index+=2
                i+=1
                continue
        
        senha = ""
        i+=1
    
    print(resposta)



        
if __name__ == '__main__':

    main()


    