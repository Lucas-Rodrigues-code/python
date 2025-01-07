print("Bem vindo ao calculador de gorjeta!")
bill = float(input("Qual foi o valor da conta? $"))
tip = int(input("Qual a porcentagem de gorjeta você gosta de dar? 10, 12 ou 15? "))
people = int(input("Quantas pessoas vão dividir a conta? "))
total = (bill + bill * tip / 100) / people
total = round(total, 2)

print(f"Cada pessoa deve pagar: ${total}")