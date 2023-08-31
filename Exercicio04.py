import random

nomes = [
    "Helena", "Alice", "Laura", "Maria Alice", "Sophia", "Manuela", "Maitê", "Liz", "Cecília", "Isabella", 
    "Luísa", "Eloá", "Heloísa", "Júlia", "Ayla", "Maria Luísa", "Isis", "Elisa", "Antonella", "Valentina", 
    "Maya", "Maria Júlia", "Aurora", "Lara", "Maria Clara", "Lívia", "Esther", "Giovanna", "Sarah", 
    "Maria Cecília", "Lorena", "Beatriz", "Rebecca", "Luna", "Olívia", "Maria Helena", "Mariana", "Isadora", 
    "Melissa", "Maria", "Catarina", "Lavínia", "Alícia", "Maria Eduarda", "Agatha", "Ana Liz", "Yasmin", 
    "Emanuelly", "Ana Clara", "Clara", "Ana Júlia", "Marina", "Stella", "Jade", "Maria Liz", "Ana Laura", 
    "Maria Isis", "Ana Luísa", "Gabriela", "Alana", "Rafaela", "Vitória", "Isabelly", "Bella", "Milena", 
    "Clarice", "Mirella", "Ana", "Emilly", "Betina", "Mariah", "Zoe", "Maria Vitória", "Nicole", "Laís", 
    "Melina", "Bianca", "Louise", "Ana Beatriz", "Heloíse", "Malu", "Melinda", "Letícia", "Maria Valentina", 
    "Chloe", "Maria Elisa", "Maria Heloísa", "Maria Laura", "Maria Fernanda", "Ana Cecília", "Hadassa", 
    "Ana Vitória", "Diana", "Ayla Sophia", "Eduarda", "Ana Lívia", "Isabel", "Elis", "Pérola", "Joana",
    # Masculine names
    "Lucas", "Miguel", "Arthur", "Davi", "Gabriel", "Pedro", "Bernardo", "Matheus", "Heitor", "Cauã", 
    "Enzo", "Lorenzo", "Gustavo", "Felipe", "Samuel", "Benjamin", "Rafael", "João", "Daniel", "Vitor", 
    "Eduardo", "Noah", "Leonardo", "Henrique", "Theo", "Isaac", "Murilo", "Caio", "Lucca", "Vinícius", 
    "Pedro Henrique", "João Pedro", "Bryan", "Davi Lucca", "Pietro", "Francisco", "Caleb", "Antônio", 
    "Enzo Gabriel", "Davi Lucas", "Bruno", "Yuri", "Emanuel", "Ian", "Tomás", "Nathan", "Ryan", "Luiz Felipe", 
    "Igor", "Ruan", "Otávio", "Luan", "Kaique", "Breno", "Davi Luiz", "Augusto", "Nicolas", "Guilherme", 
    "Daniel", "Carlos", "Calebe", "Vicente", "Fernando", "Marcelo", "Thiago", "João Lucas", "Raul", 
    "Felipe", "Fábio", "André", "Erick", "Paulo", "Giovanni", "Roberto", "Renan", "José", "Arthur Gabriel"
]


def diasVividos (nome: str,anos:int,meses:int,dias:int):
    anosEmDias = anos * 365 
    mesesEmDias = meses * 365 
    diasTotaisVividos = anosEmDias + mesesEmDias + dias
    print(anos,meses,dias)
    print(f'Ola {nome},gostaria de informar que v seu total de dias vividos eh {diasTotaisVividos}')



diasVividos( nomes[random.randint(0,len(nomes))],random.randint(1,120),random.randint(1,12),random.randint(0,365)  )

