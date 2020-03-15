# Equação de segundo grau
print("Resolva aqui sua equação de 2° grau")
a = float(input("Insira 'a': "))
b = float(input("Insira 'b': "))
c = float(input("Insira 'c': "))
d = (b**2)-(4*a*c)
sol1 = (b + (d**(1/2)))/(2*a)
sol2 = (b - (d**(1/2)))/(2*a)

# print("Sua equação é: ")
# print(a+"x^2+"+b+"x+"+c+"=0")

print("Soluções: ")
print(sol1)
print(sol2)