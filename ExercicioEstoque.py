import random
import names 
totalDeProdutos = []
codigoAleatorio = 0
class Produto:
    def __init__(self,codigo,nome,estoque,precoDeCusto,precoDeVenda,porcentagemDeIcms,porcentagemIpi):
        self.codigo = codigo
        self.nome = nome
        self.estoque = estoque 
        self.precoDeVenda = precoDeVenda
        self.precoDeCusto = precoDeCusto
        self.porcentagemDeIcms = porcentagemDeIcms
        self.porcentagemDeIpi = porcentagemIpi 
        self.estoqueMinimo =  random.randint(0,estoque)
        self.estoqueMaximo = random.randint(self.estoqueMinimo,estoque )
        self.lucro = precoDeVenda - precoDeCusto

numeroDeProdutos = int(input("Digite quantos produtos vc gostaria de analisar "))

for i in  range (numeroDeProdutos):
    codigoAleatorio += 1 
    nomeAleatorio = names.get_first_name()
    estoqueAleatorio = random.randint(0,100000)
    precoDeCustoAleatorio = random.randint(0,10000)
    precoDeVendaAleatorio = random.randint(precoDeCustoAleatorio,100000)
    porcentagemIcmsAleatorio = random.uniform(0,100)
    porcentagemIpisAleatorio = random.uniform(0,100)
    produtoGerado = Produto(codigoAleatorio,nomeAleatorio,estoqueAleatorio,precoDeCustoAleatorio,precoDeVendaAleatorio,porcentagemIcmsAleatorio,porcentagemIpisAleatorio)
    print(f"{'-' * 60}")
    print(f"Codigo : {produtoGerado.codigo} \n")
    print(f"Produto : {produtoGerado.nome} \n")
    print(f"Estoque : {produtoGerado.estoque} \n")
    print(f"Estoque Minimo : {produtoGerado.estoqueMinimo} \n")
    print(f"Estoque Maximo : {produtoGerado.estoqueMaximo} \n")
    print(f"Porcentagem de ICMS : {produtoGerado.porcentagemDeIcms:.2f} % \n")
    print(f"Porcentagem de IPI : {produtoGerado.porcentagemDeIpi:.2f}  % \n")
    print(f" Valor para compra  : R$ {produtoGerado.precoDeCusto:.2f} \n")
    print(f" Valor para venda  : R$ {produtoGerado.precoDeVenda:.2f} \n")
    print(f" Lucro  : R$ {produtoGerado.porcentagemDeIcms:.2f} \n")
    print(f"{'-' * 60}")
    totalDeProdutos.append(produtoGerado)


produtoComMaiorPreco = max(totalDeProdutos,key=lambda x: x.precoDeVenda)
produtoComMenorPreco = min(totalDeProdutos,key=lambda x: x.precoDeVenda)
produtoComMaiorEstoque = max(totalDeProdutos,key=lambda x: x.estoque)
produtoComMenorEstoque = min(totalDeProdutos,key=lambda x: x.estoque)
produtoComMaiorICMS = max(totalDeProdutos,key=lambda x: x.porcentagemDeIcms)
produtoComMenorICMS = min(totalDeProdutos,key=lambda x: x.porcentagemDeIcms)
produtoComMaiorLucro  = max(totalDeProdutos,key=lambda x: x.lucro)
produtoComMenorLucro  = min(totalDeProdutos,key=lambda x: x.lucro)


print(f"{'-' * 60}")
print(f"O produto com maior preço  :  {produtoComMaiorPreco.nome} || Preço de Venda: R$ {produtoComMaiorPreco.precoDeVenda:.2f} \n ")
print(f"O produto com mmenor preço :  {produtoComMenorPreco.nome} || Preço de Venda: R$ {produtoComMenorPreco.precoDeVenda:.2f} \n ")
print(f"O produto com maior lucro :  {produtoComMaiorLucro.nome} || Lucro: R$ {produtoComMaiorLucro.lucro:.2f} \n ")
print(f"O produto com menor lucro :  {produtoComMenorLucro.nome} || Lucro: R$ {produtoComMenorLucro.lucro:.2f} \n ")
print(f"O produto com maior estoque :  {produtoComMaiorEstoque.nome} || Estoque: {produtoComMaiorEstoque.estoque} \n ")
print(f"O produto com menor estoque :  {produtoComMenorEstoque.nome} || Estoque: {produtoComMenorEstoque.estoque} \n ")
print(f"O produto com maior IMCS  :  {produtoComMaiorICMS.nome} || ICMS: {produtoComMaiorICMS.porcentagemDeIcms:.2f} % \n ")
print(f"O produto com menor IMCS  :  {produtoComMenorICMS.nome} || ICMS: {produtoComMenorICMS.porcentagemDeIcms:.2f} % \n  ")
print(f"{'-' * 60}")