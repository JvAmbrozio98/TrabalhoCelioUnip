import random
def maiorNumeroDecimal (n1,n2,n3):
    if ((n1<n2) and (n2 < n3)):
        print(f'O menor  numero eh {n1} ')
    else:
        if(n2 < n3) :
            print(f'O menor numero eh {n2} ')
        else:
            print(f'O menor numero eh {n3} ')
    print(n1,n2,n3)

maiorNumeroDecimal(random.randint(0,10000),random.randint(0,10000),random.randint(0,10000))