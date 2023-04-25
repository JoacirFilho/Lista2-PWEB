anterior = 0 
proximo = 1
soma = 1

fim = int (input("Digite um numero:"))

for i in range (0 , fim):
    soma = anterior + proximo
    print(soma)
    anterior = proximo
    proximo = soma