import random
from Exercicio5ConstrutoresEfuncoes import Municipio
from Exercicio5ConstrutoresEfuncoes import distribuirPopulacao


listaDeCidades = []
nomesCidadesReais = [
    "São Paulo", "Rio de Janeiro", "Belo Horizonte", "Salvador", "Brasília", 
    "Curitiba", "Fortaleza", "Recife", "Porto Alegre", "Manaus"
]
x = 0


while(x < 10):
    numeroAleatorio = random.randint(1,10000000000000)
    populacaoAleatoria = distribuirPopulacao(numeroAleatorio,3)
    instanciaDeCidade = Municipio(nomesCidadesReais[x],populacaoAleatoria)
   
    
    
    
    
    print(f'\n**********************************************************************')
    print(f'\n Na cidade de : {instanciaDeCidade.nome}')
    print(f'\nO numero de votos total  eh: {instanciaDeCidade.totalDeVotos}')
    print(f'\nO numero de votos em branco eh: {instanciaDeCidade.votosEmBranco}')
    print(f'\nO numero de votos em nulos eh: {instanciaDeCidade.votosNulos}')
    print(f'\nO numero de votos em valido eh: {instanciaDeCidade.votosValidos}')
    print(f'\n A porcentagem de votos em Branco: {instanciaDeCidade.porcentagemDeVotosEmBranco:.2f} %')
    print(f'\n A porcentagem de votos em Nulos: {instanciaDeCidade.porcentagemDeVotosNulos:.2f} %')
    print(f'\n A porcentagem de votos em Validos: {instanciaDeCidade.porcentagemDeVotosValidos:.2f} %')
    print(f'\n**********************************************************************')
    listaDeCidades.append(instanciaDeCidade)
    x += 1

    



cidadeComMaisVotosValidos = max(listaDeCidades,key=lambda x: x.porcentagemDeVotosValidos)
print(cidadeComMaisVotosValidos.porcentagemDeVotosValidos)
print(cidadeComMaisVotosValidos.nome)

    
    
    
    

