lista = []

for n in range(5):
    n = int(input("Digite um numero: "))
    lista.append(n)
    
maior = max(lista)
menor = min(lista)

print("O maior Número é: ", maior)
print ("O Menor Número é: ", menor)
