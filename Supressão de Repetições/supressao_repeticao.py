################################################################
#                            ARQUIVOS                          #  
################################################################

# Pegue o arquivo .txt (em modo escrita) que irá armezenar o resultado da compressão
from unittest import result


arquivo2 = open("d:/Supressão de Repetições/arquivo_compressão.txt", "w")

# Pegue o arquivo .txt (em modo escrita) que irá armezenar o resultado da descompressão
arquivo3 = open("d:/Supressão de Repetições/arquivo_descompressão.txt", "w")


################################################################
#                           TEXTOS                             #  
################################################################


# Pegue o arquivo .txt (em modo leitura) com o texto original e converta para string 
arquivo1_txt = open("d:/Supressão de Repetições/arquivo_original.txt", "r").read()

arquivo2_txt = ""

arquivo3_txt = ""


################################################################
#                          CONTROLE                            #  
################################################################

# FLAG que será usada para marcação durante o algortimo
FLAG = "#"

# Quantidade mínima de repetições
REPETICAO_MINIMA = 4


################################################################
#                          FUNÇÕES                             #  
################################################################

# Função para compressão aonde precisamos dizer qual será o texto que vai ser comprimido, a flag e a quantidade mínima de repetições
def compressao(texto, flag, repeticao):

    # Converta o texto original para uma lista de caracteres
    caracteres = list(texto)
    
    # Lista que irá armazenar os caracteres da compressão
    lista = []

    # Contador de repetições do caractere atual
    contador = 1

    # Caractere que estamos observando atualmente
    car = caracteres[0]

    # Percorra a lista de caracteres do texto original
    for i in range(1, len(caracteres)):

        # Se o caractere atual for igual ao caractere que estamos observando atualmente
        if caracteres[i] == car:

            # Acrescente mais um a repetição
            contador = contador + 1

        # Caso não for o mesmo caractere
        else:

            # Se a quantidade de repetições for maior ou igual a quantidade mínima
            if contador >= repeticao:
                # Adicione a flag
                lista.append(flag)

                # Adicione o contador
                lista.append(str(contador)) 
            
            # Adicione o caractere
            lista.append(car)

            # Troque o caractere que estamos observando
            car = caracteres[i]

            # Reinicie a contagem
            contador = 1
    
    # Última tentativa do algoritmo
    if contador >= repeticao:
        lista.append(flag)
        lista.append(str(contador)) 

    lista.append(car)

    # String que irá juntar os caracteres da lista comprimida
    resultado = ""

    # Percorra a lista dos caracteres comprimidos
    for i in range(0, len(lista)):
        # Adicione o caractere atual na string do resultado final
        resultado += lista[i]

    # Retorne o resultado final
    return resultado

# Função para descompressão aonde precisamos dizer qual será o texto que vai ser descomprimido e a flag que foi usada no algoritmo de compressão
def descompressao(texto, flag):

    # Converta o texto comprimido para uma lista de caracteres
    caracteres = list(texto)

    # Armazena o caractere que iremos repetir
    car = ''

    # Lista que irá armazenar os caracteres da descompressão
    lista = []

    # Percorra a lista de caracteres do texto comprimido
    for i in range(0, len(caracteres)):

        # Caso o caractere atual for a flag
        if caracteres[i] == flag:
            
            # Logo o próximo é a quantidade que foi repetida
            repeticao = int(caracteres[i+1])

            # E o em seguida é o caractere que foi repetido
            car = caracteres[i+2]

            # Remova ambos os caracteres de referência, pois não queremos escrevê-los
            caracteres[i+1] = ""
            caracteres[i+2] = ""

            # Adicione o caractere da repetição, conforme o valor retirado
            for j in range(0, repeticao):
                lista.append(car)
                i = i + 1

        # Caso não for uma flag
        else:
            # Apenas coloque o caractere atual
            lista.append(caracteres[i])

    # String que irá juntar os caracteres da lista descomprimida
    resultado = ""

    # Percorra a lista de caracteres descomprimidos
    for i in range(0, len(lista)):

        # Adicione o caractere atual na string do resultado final
        resultado += lista[i]
    
    # Retorne o resultado final
    return resultado

################################################################
#                          EXECUÇÃO                            #  
################################################################


# Aplique a compressão e então armazene na string relacionada ao arquivo 2
arquivo2_txt = compressao(arquivo1_txt, FLAG, REPETICAO_MINIMA)


# Aplique a descompressão e então armazene na string relacionada ao arquivo 3
arquivo3_txt = descompressao(arquivo2_txt, FLAG)


# Escreva a string no arquivo relacionado a compressão
arquivo2.write(arquivo2_txt)

# Escreva a string no arquivo relaciona a descompressão
arquivo3.write(arquivo3_txt)

print("Saiu do Forno!")