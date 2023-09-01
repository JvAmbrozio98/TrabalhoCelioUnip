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


def  entradaPeloUsuario():
    listaInputdoUsuario = []
    nomeDigitadoPeloUsuario = input("Digita o nome da cidade:")     
        
    votosEmBrancoUser = int(input("Quantos votos em branco na cidade: "))    
    listaInputdoUsuario.append(votosEmBrancoUser)    

    votosNulosUser = int(input("Quantos votos nulos na cidade: "))    
    listaInputdoUsuario.append(votosNulosUser)    
        
    votosValidosUser = int(input("Quantos votos validos na cidade: "))    
    listaInputdoUsuario.append(votosValidosUser)    
    instanciaDeCidade = Municipio(nomeDigitadoPeloUsuario,listaInputdoUsuario)    
    return instanciaDeCidade        

def testeAutomatizado(x):
    nomesCidadesReais = [
    "São Paulo", "Rio de Janeiro", "Belo Horizonte", "Salvador", "Brasília", 
    "Curitiba", "Fortaleza", "Recife", "Porto Alegre", "Manaus","Botucatu","Bauru"]
    numeroAleatorio = random.randint(1,1000)
    populacaoAleatoria = distribuirPopulacao(numeroAleatorio,3)
    instanciaDeCidade = Municipio(nomesCidadesReais[x],populacaoAleatoria)
    return instanciaDeCidade



