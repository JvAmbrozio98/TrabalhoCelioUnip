#

from Exercicio5ConstrutoresEfuncoes import Municipio,distribuirPopulacao,testeAutomatizado,entradaPeloUsuario,escolhaDeModo
listaDeCidades = []
x = 0
# instanciaDeCidade = escolhaDeModo()

escolhaRapida = int(input("Digite 0 para usar os testes automaticos e qualquer outro numero para realizar as entradas   "))

while(x < 10):
    
    if(escolhaRapida == 0):
        instanciaDeCidade = testeAutomatizado(x)
    else:
        instanciaDeCidade = entradaPeloUsuario()

    
    #1instanciaDeCidade = entradaPeloUsuario ()
    print(f'\n**********************************************************************')    
    print(f'\n Na cidade de : {instanciaDeCidade.nome}')    
    print(f'\nO numero de votos total  eh: {instanciaDeCidade.totalDeVotos}')    
    print(f'\nO numero de votos em branco eh: {instanciaDeCidade.votosEmBranco}')
    print(f'\nO numero de votos  nulos eh: {instanciaDeCidade.votosNulos}')
    print(f'\nO numero de votos validos eh: {instanciaDeCidade.votosValidos}')
    print(f'\n A porcentagem de votos brancos: {instanciaDeCidade.porcentagemDeVotosEmBranco:.2f} %')
    print(f'\n A porcentagem de votos  nulos: {instanciaDeCidade.porcentagemDeVotosNulos:.2f} %')
    print(f'\n A porcentagem de votos validos: {instanciaDeCidade.porcentagemDeVotosValidos:.2f} %')
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
print(f'A quantidade total de votos nulos eh : {cidadeComMaisVotosNulos.votosNulos} \n ')
print(f'Que equivale a :   {cidadeComMaisVotosNulos.porcentagemDeVotosNulos:.2f}  % \n ')
print(f'\n**********************************************************************')


cidadeComMaisVotosEmBranco = max(listaDeCidades,key=lambda x: x.votosEmBranco)
print(f'**********************************************************************')
print(f'A cidade com mais votos em Branco eh : {cidadeComMaisVotosEmBranco.nome} \n ')
print(f'A quantidade total de votos eh : {cidadeComMaisVotosEmBranco.votosEmBranco} \n ')
print(f'Que equivale a :   {cidadeComMaisVotosEmBranco.porcentagemDeVotosEmBranco:.2f}  % \n ')
print(f'\n**********************************************************************')


    
    
    

