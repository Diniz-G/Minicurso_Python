var1 = "Gabriel"
var2 = "Diniz"

concat = var1 + " " + var2

print('Olá ' + concat + '!')

##############################
tamanho = len(concat)
print(tamanho)

##############################
letra = concat[12]
print(letra)

##############################
for i in range(tamanho):
    print(concat[i])

##############################
print(concat[0:5]) #se deixar vazio dps do ':' vai até o final