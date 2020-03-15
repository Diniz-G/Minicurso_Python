minha_lista = ["sabão", "shampoo", "escova"]

minha_lista.append("chinelo")
print(minha_lista)

if "escova" in minha_lista:
    print("Escova está na lista")
else:
    print("Escova não está na lista")

del minha_lista[2:]
# para deletar a lista inteira
# -> del minha_lista[:]
print(minha_lista)

minha_lista.append("abacaxi")
print(minha_lista)
minha_lista.sort()
# lista.reverse() inverte a ordem da lista
# lista.sort(reverse = True) ordena de forma decrescente
# lista2 = sorted(lista) ordena a lista e a atribui a outra variavel
print(minha_lista)