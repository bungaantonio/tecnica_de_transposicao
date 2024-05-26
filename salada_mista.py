def cifrar(texto_claro, chave):
    num_colunas = len(chave)
    num_linha = -(-len(texto_claro) // num_colunas)  # Divisão Inteira

    # Preenchendo o texto com espaços em branco se necessário
    texto_claro += ' ' * (num_colunas * num_linha - len(texto_claro))

    # Criando as colunas
    colunas = [''] * num_colunas
    for i, char in enumerate(texto_claro):
        colunas[i % num_colunas] += char

    # Função para realizar as rotações
    def rotacionar(coluna, graus):
        if graus == 90:
            return coluna[-1] + coluna[:-1]
        elif graus == 180:
            return coluna[::-1]
        elif graus == 270:
            return coluna[1:] + coluna[0]
        return coluna

    # Primeira rotação baseada no primeiro dígito da chave
    primeiro_digito = int(chave[0])
    if 0 <= primeiro_digito <= 2:
        graus_rotacao = 90
    elif 3 <= primeiro_digito <= 6:
        graus_rotacao = 180
    elif 7 <= primeiro_digito <= 9:
        graus_rotacao = 270
    colunas = [rotacionar(col, graus_rotacao) for col in colunas]

    # Segunda rotação baseada no segundo dígito da chave
    segundo_digito = int(chave[1])
    if 0 <= segundo_digito <= 2:
        graus_rotacao = 90
    elif 3 <= segundo_digito <= 6:
        graus_rotacao = 180
    elif 7 <= segundo_digito <= 9:
        graus_rotacao = 270
    colunas = [rotacionar(col, graus_rotacao) for col in colunas]

    # Reordenando as colunas de acordo com a chave
    ordenar_colunas = [None] * num_colunas
    for i, k in enumerate(chave):
        ordenar_colunas[int(k) - 1] = colunas[i]

    # Concatenando as colunas criptografadas
    cifrar_texto = ''.join(ordenar_colunas)

    return cifrar_texto

def decifrar(texto_cifrado, chave):
    num_colunas = len(chave)
    num_linha = -(-len(texto_cifrado) // num_colunas)  # Divisão Inteira

    # Dividindo o texto cifrado em colunas
    colunas = [''] * num_colunas
    pos = 0
    for i in range(num_colunas):
        colunas[i] = texto_cifrado[pos:pos + num_linha]
        pos += num_linha

    # Revertendo a reordenação das colunas de acordo com a chave
    ordenar_colunas = [None] * num_colunas
    for i, k in enumerate(chave):
        ordenar_colunas[i] = colunas[int(k) - 1]

    colunas = ordenar_colunas

    # Função para reverter as rotações
    def rotacionar_inverso(coluna, graus):
        if graus == 90:
            return coluna[1:] + coluna[0]
        elif graus == 180:
            return coluna[::-1]
        elif graus == 270:
            return coluna[-1] + coluna[:-1]
        return coluna

    # Revertendo a segunda rotação baseada no segundo dígito da chave
    segundo_digito = int(chave[1])
    if 0 <= segundo_digito <= 2:
        graus_rotacao = 90
    elif 3 <= segundo_digito <= 6:
        graus_rotacao = 180
    elif 7 <= segundo_digito <= 9:
        graus_rotacao = 270
    colunas = [rotacionar_inverso(col, graus_rotacao) for col in colunas]

    # Revertendo a primeira rotação baseada no primeiro dígito da chave
    primeiro_digito = int(chave[0])
    if 0 <= primeiro_digito <= 2:
        graus_rotacao = 90
    elif 3 <= primeiro_digito <= 6:
        graus_rotacao = 180
    elif 7 <= primeiro_digito <= 9:
        graus_rotacao = 270
    colunas = [rotacionar_inverso(col, graus_rotacao) for col in colunas]

    # Reconstruindo o texto claro a partir das colunas
    texto_claro = ''
    for i in range(num_linha):
        for col in colunas:
            if i < len(col):
                texto_claro += col[i]

    return texto_claro.strip()

# Exemplo de uso
texto_claro = input("Texto claro: ")
chave = input("Chave: ")

cifrado = cifrar(texto_claro, chave)
print(f"Texto criptografado: {cifrado}")

#
chave = input("Confirme a chave para decifrar o texto: ")
decifrado = decifrar(cifrado, chave)
print(f"Texto descriptografado: {decifrado}")