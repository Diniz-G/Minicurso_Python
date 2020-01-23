from datetime import datetime

def hora_exata():
    print('Processando...')
    print(datetime.now())
    print()

for x in range(0,11):
    print(x)
    print(hora_exata)

now = datetime.now()

print(now.hour)