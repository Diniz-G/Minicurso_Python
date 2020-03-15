def dobro(x):
    return x*2

valor = [1,2,3,4,5]

# map(função, lista)
valor_dobrado = map(dobro, valor)

#for i in valor_dobrado:
#    print(i)

valor_dobrado = list(valor_dobrado)
print(valor_dobrado)