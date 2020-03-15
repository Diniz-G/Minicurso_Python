lista1 = [1,2,3,4,5]
lista2 = ["abacaxi", "bola", "cachorro", "dentista", "elefante"]
lista3 = ["2,00", "1,50", "300,00", "-", "-"]

for numero, nome, valor in zip(lista1, lista2, lista3):
    print(numero, nome, valor)