a = "Gabriel"
b = "Diniz"

concat = a + " " + b + "\n"
print(concat)
print(concat.lower())
print(concat.upper())
print(concat.strip()) #remove o "\n"

#######################################
my_string = "O rato roeu a roupa..."
my_list = my_string.split() #separa em strings a cada " "
#ou passa-se como argumento em qual caractere deve quebrar a string
print(my_list)

busca = my_string.find("roeu")
print(busca)
print(my_string[busca:])

calça = my_string.replace("roupa", "calça")
print(calça)