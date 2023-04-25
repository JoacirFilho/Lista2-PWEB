lista = []

n1 = int(input("Digite um numero: "))

for n in range(5):
    lista.append(n)
    media = sum(lista) / (n1)

print(lista)

print("A media da lista {}, é {};".format(lista, media))
