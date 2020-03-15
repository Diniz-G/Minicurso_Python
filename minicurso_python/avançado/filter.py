def pares(i):
    if i%2 == 0:
        return i

lista = [1,2,3,4,5,6,7,8,9]

#filter(função de teste/condição, lista)
lista_pares = filter(pares, lista)

# list() converte o objeto do tipo filter em uma lista
print(list(lista_pares))