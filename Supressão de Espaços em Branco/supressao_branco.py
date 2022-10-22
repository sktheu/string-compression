################################################################
#                            ARQUIVOS                          #
################################################################

# Pegue o arquivo .txt (em modo escrita) que irá armezenar o resultado da compressão
arquivo2 = open("arquivo_compressão.txt", "w")

# Pegue o arquivo .txt (em modo escrita) que irá armezenar o resultado da descompressão
arquivo3 = open("arquivo_descompressão.txt", "w")


################################################################
#                           TEXTOS                             #
################################################################


# Pegue o arquivo .txt (em modo leitura) com o texto original e converta para string
arquivo1_txt = open("arquivo_original.txt", "r").read()

arquivo2_txt = ""

arquivo3_txt = ""


################################################################
#                          CONTROLE                            #
################################################################

# FLAG que será usada para marcação durante o algortimo
FLAG = "#"



################################################################
#                          FUNÇÕES                             #
################################################################

# Função para compressão aonde precisamos dizer qual será o texto que vai ser comprimido

def compressao(texto, flag):

    # Armazene dentro de uma lista todos os caracteres do meu texto original
    caracteres = list(texto)

    # Contador da repetição
    contador = 0

    # Resultado
    resultado = ""

    # Percorra a lista de caracteres do texto original verificando os espaços em branco
    for i in range(0, len(caracteres)):

        # Se o meu caractere atual for igual a um espaço em branco
        if caracteres[i] == " ":

            # Se for a primeira repetição desse espaço em branco, coloque a flag
            if contador == 0:
                resultado += flag

            # Acrescente mais um ao meu contador de espaços atual
            contador = contador + 1


        # Caso não for um espaço
        else:

            # Coloco o contador
            if contador != 0:
                resultado += str(contador)

            # Apenas coloque o caractere atual
            resultado += caracteres[i]

            # Reinicie minha contagem de espaços
            contador = 0

    # Retorne a minha string final
    return resultado


# Função para descompressão aonde precisamos dizer qual será o texto que vai ser descomprimido
def descompressao(texto, flag):

    # Armazene dentro de uma lista todos os caracteres do meu texto comprimido
    caracteres = list(texto)

    # String que irá o meu resultado da descompressão
    resultado = ""

    # Percorra a lista de caracteres do meu texto comprimido verificando as flags
    for i in range(0, len(caracteres)):

        # Caso o caractere atual for uma flag
        if caracteres[i] == flag:

            # Pegue o caractere seguinte, ou seja, a quantidade de repetições de espaços
            contador = int(str(caracteres[i+1]))
            caracteres[i+1] = ""

            # Adicione os espaços em brancos com base no meu contador atual
            for i in range(0, contador):
                resultado += " "

        else:

            # Apenas coloque o caractere atual
            resultado += caracteres[i]


    # Retorne a minha string final
    return resultado


################################################################
#                          EXECUÇÃO                            #
################################################################


# Aplique a compressão e então armazene na string relacionada ao arquivo 2
arquivo2_txt = compressao(arquivo1_txt, FLAG)


# Aplique a descompressão e então armazene na string relacionada ao arquivo 3
arquivo3_txt = descompressao(arquivo2_txt, FLAG)


# Escreva a string no arquivo relacionado a compressão
arquivo2.write(arquivo2_txt)

# Escreva a string no arquivo relaciona a descompressão
arquivo3.write(arquivo3_txt)


print("Saiu do Forno!")
