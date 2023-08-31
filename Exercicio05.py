#
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
    listaInputdoUsuario = []
    nomeDigitadoPeloUsuario = input("Digita o nome da cidade:") 
    
    votosEmBrancoUser = int(input("Quantos votos em branco na cidade: "))
    listaInputdoUsuario.append(votosEmBrancoUser)

    votosNulosUser = int(input("Quantos votos nulos na cidade: "))
    listaInputdoUsuario.append(votosNulosUser)
    
    votosValidosUser = int(input("Quantos votos validos na cidade: "))
    listaInputdoUsuario.append(votosValidosUser)
   

    # numeroAleatorio = random.randint(1,10000000000000)
    # populacaoAleatoria = distribuirPopulacao(numeroAleatorio,3)
    # instanciaDeCidade = Municipio(nomesCidadesReais[x],populacaoAleatoria)
    instanciaDeCidade = Municipio(nomeDigitadoPeloUsuario,listaInputdoUsuario)
   
    
    
    
    
    print(f'\n**********************************************************************')
    print(f'\n Na cidade de : {instanciaDeCidade.nome}')
    print(f'\nO numero de votos total  eh: {instanciaDeCidade.totalDeVotos}')
    print(f'\nO numero de votos em branco eh: {instanciaDeCidade.votosEmBranco}')
    print(f'\nO numero de votos  nulos eh: {instanciaDeCidade.votosNulos}')
    print(f'\nO numero de votos validos eh: {instanciaDeCidade.votosValidos}')
    print(f'\n A porcentagem de votos em Branco: {instanciaDeCidade.porcentagemDeVotosEmBranco:.2f} %')
    print(f'\n A porcentagem de votos em Nulos: {instanciaDeCidade.porcentagemDeVotosNulos:.2f} %')
    print(f'\n A porcentagem de votos em Validos: {instanciaDeCidade.porcentagemDeVotosValidos:.2f} %')
    print(f'\n**********************************************************************')
    listaDeCidades.append(instanciaDeCidade)
    x += 1

    



cidadeComMaisVotosTotais = max(listaDeCidades,key=lambda x: x.totalDeVotos)
print(f'**********************************************************************')
print(f'A cidade com mais eleitores eh : {cidadeComMaisVotosTotais.nome} \n ')
print(f'A quantidade total de votos eh  {cidadeComMaisVotosTotais.totalDeVotos} \n ')
print(f'\n**********************************************************************')


cidadeComMaisVotosValidos = max(listaDeCidades,key=lambda x: x.votosValidos)
print(f'**********************************************************************')
print(f'A cidade com mais votos validos eh : {cidadeComMaisVotosValidos.nome} \n ')
print(f'A quantidade total de votos eh : {cidadeComMaisVotosValidos.votosValidos} \n ')
print(f'Que equivale a :   {cidadeComMaisVotosValidos.porcentagemDeVotosValidos:.2f} % \n ')
print(f'\n**********************************************************************')

cidadeComMaisVotosNulos = max(listaDeCidades,key=lambda x: x.votosNulos)
print(f'**********************************************************************')
print(f'A cidade com mais votos Nulos eh : {cidadeComMaisVotosNulos.nome} \n ')
print(f'A quantidade total de votos eh : {cidadeComMaisVotosNulos.votosNulos} \n ')
print(f'Que equivale a :   {cidadeComMaisVotosValidos.porcentagemDeVotosNulos:.2f}  % \n ')
print(f'\n**********************************************************************')


cidadeComMaisVotosEmBranco = max(listaDeCidades,key=lambda x: x.votosEmBranco)
print(f'**********************************************************************')
print(f'A cidade com mais votos em Branco eh : {cidadeComMaisVotosNulos.nome} \n ')
print(f'A quantidade total de votos eh : {cidadeComMaisVotosNulos.votosEmBranco} \n ')
print(f'Que equivale a :   {cidadeComMaisVotosValidos.porcentagemDeVotosEmBranco:.2f}  % \n ')
print(f'\n**********************************************************************')


    
    
    

