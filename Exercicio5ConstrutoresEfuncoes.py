import random
class Municipio:
    def __init__(self,nome:str, eleitores: list):
        self.eleitores = eleitores
        self.nome = nome
        self.votosEmBranco = eleitores[0]
        self.votosNulos = eleitores[1]
        self.votosValidos = eleitores[2]
        self.totalDeVotos = sum(eleitores)
        self.porcentagemDeVotosEmBranco = (self.votosEmBranco / sum(eleitores) * 100 ) 
        self.porcentagemDeVotosNulos = (self.votosNulos / sum(eleitores) * 100 )
        self.porcentagemDeVotosValidos = (self.votosValidos / sum(eleitores) * 100 )
        




def distribuirPopulacao(totalPopulacao, numSecoes):
    listaPopulacao = []

    for i in range(numSecoes - 1):
        populacaoAleatoria = random.randint(1, totalPopulacao)
        listaPopulacao.append(populacaoAleatoria)
        totalPopulacao -= populacaoAleatoria

    listaPopulacao.append(totalPopulacao)
    random.shuffle(listaPopulacao)

    return listaPopulacao