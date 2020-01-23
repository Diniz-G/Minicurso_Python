print("olá mundo")

dia = 25
mes = 7
ano = 2019

print(dia, mes, ano, sep = "/")

dia = input("Digite o dia: ")
mes = input("Digite o mes: ")
ano = input("Digite o ano: ")

dia=int(dia)
mes=int(mes)
ano=int(ano)

print(dia,"/",mes,"/",ano)
print(dia, mes, ano, sep = "/")
print('{}/{}/{}' .format(dia, mes, ano))
print('{:.2f}/{:.2f}/{:.2f}' .format(dia, mes, ano))
print('{:2.0f}/{:2.0f}/{:2.0f}' .format(dia, mes, ano))