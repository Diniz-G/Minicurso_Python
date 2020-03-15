print("Insira dois números e o operador: ")
a = int(input())
b = int(input())
sinal = input()

if sinal == "+":
    print(a+b)
elif sinal == "-":
    print(a-b)
elif sinal == "*":
    print(a*b)
elif sinal == "/":
    print(a/b)
else:
    print("Sinal não reconhecido.")