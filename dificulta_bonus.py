def gerar_opcoes(apostas,pesos):
    opcoes = []
    for i in range(len(apostas)):
        for peso in range(pesos[i]):
            opcoes.append(apostas[i])
    return opcoes
