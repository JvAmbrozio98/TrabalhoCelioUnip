def vendas():
    x= 0
    while x < 10:


        produto = str (input("Informe o nome do produto: "))
        qnt_adquirida = int (input ("Informe a quantidade comprada: "))
        preco = float (input ("Informe o valor pago pelo produto: "))
        total = float (qnt_adquirida*preco)

        if qnt_adquirida<=5:
            desconto=preco*0.02

        elif qnt_adquirida > 5 and qnt_adquirida <= 10:
            desconto=preco*0.03
        else:
                desconto=preco*0.05
        total=total-desconto
        print ("Produto", produto)
        print ("Quantidade Adquirida", qnt_adquirida)
        print ("Preço", preco)
        print ("Desconto", desconto)
        print ("Total", total)
        x=x+1

