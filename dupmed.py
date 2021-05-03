# Recebendo os valores da multiplicação

x = int(input("Insira um valor: "))

y = int(input("Insira o segundo valor: "))

# Organizando para que x > y

if y > x:
    n = y
    y = x
    x = n
    
s = y

# Calcula e armazena as potencias de dois que terao de multiplicar o valor maior

pots = []

count = 0

while s >= 1:
    if s%2 == 1:
        pots.append(2 ** count)
        s -= 1
    s = s/2
    count += 1

# Calcula e armazena os produtos das potencias de dois pelo numero maior, que somadas sao os resultados da multiplicacao

mults = []

m = 0

for m in range(len(pots)):
    mults.append(pots[m] * x)
    m += 1
    
# Com tudo ja calculado exibe os numeros a serem somados, as potencias e a soma para o usuario

print("As potencias de dois que resultaram valores impares foram: ", pots)
print("Os valores a serem somados são: ", mults)
print("O resultado da soma, e consequentemente da multiplicacao de ",x," por",y," é:", sum(mults))





# Escrito por: Lucca Lacerda