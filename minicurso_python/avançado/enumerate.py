lista = ["abacate", "bola", "cachorro"]

# forma não recomendada
# range() cria um vetor do tamanho de lista
for i in range(len(lista)):
    print(i, ":", lista[i])

print("\nUsando enumerate: ")
# usando enumerate
for i, nome in enumerate(lista):
    print(i, ":", nome)