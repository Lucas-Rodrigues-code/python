#examples os dictionaries


# Criando um dicionário
carro = {
    "marca": "Toyota",
    "modelo": "Corolla",
    "ano": 2020
}

# Acessando dados do dicionário
print(carro["marca"])  # Saída: Toyota
print(carro["modelo"])  # Saída: Corolla
print(carro["ano"])  # Saída: 2020

# Criando um dicionário aninhado
alunos = {
    "aluno1": {
        "nome": "Lucas",
        "idade": 22,
        "curso": "Engenharia"
    },
    "aluno2": {
        "nome": "Maria",
        "idade": 20,
        "curso": "Medicina"
    }
}

# Acessando dados do dicionário aninhado
print(alunos["aluno1"]["nome"])  # Saída: Lucas
print(alunos["aluno2"]["curso"])  # Saída: Medicina

# Criando um dicionário
frutas = {
    "maçã": 3,
    "banana": 5,
    "laranja": 2
}

# Iterando sobre as chaves do dicionário
for fruta in frutas:
    print(fruta, frutas[fruta])
# Saída:
# maçã 3
# banana 5
# laranja 2

# Criando um dicionário
pessoa = {
    "nome": "João",
    "idade": 30,
    "cidade": "São Paulo"
}

# Usando o método get() para acessar valores
idade = pessoa.get("idade")
print(idade)  # Saída: 30

# Usando o método keys() para obter todas as chaves
chaves = pessoa.keys()
print(chaves)  # Saída: dict_keys(['nome', 'idade', 'cidade'])

# Usando o método values() para obter todos os valores
valores = pessoa.values()
print(valores)  # Saída: dict_values(['João', 30, 'São Paulo'])

# Usando o método items() para obter todos os pares chave-valor
itens = pessoa.items()
print(itens)  # Saída: dict_items([('nome', 'João'), ('idade', 30), ('cidade', 'São Paulo')])

# Dicionário de pontuações dos alunos
student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
}

# Dicionário para armazenar as notas dos alunos
student_grades = {}

# Convertendo as pontuações em notas
for student, score in student_scores.items():
    if score >= 91:
        student_grades[student] = "Outstanding"
    elif score >= 81:
        student_grades[student] = "Exceeds Expectations"
    elif score >= 71:
        student_grades[student] = "Acceptable"
    else:
        student_grades[student] = "Fail"

# Exibindo o dicionário de notas dos alunos
print(student_grades)




print("Welcome to the secret auction program.")

bids = {}
bidding_finished = False

def find_highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    # bidding_record = {"Angela": 123, "James": 321}
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid: 
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")

while not bidding_finished:
    name = input("What is your name?: ")
    price = int(input("What is your bid?: $"))
    bids[name] = price
    should_continue = input("Are there any other bidders? Type 'yes' or 'no'.\n")
    if should_continue == "no":
        bidding_finished = True
        find_highest_bidder(bids)
    elif should_continue == "yes":
        print('\n' * 20)