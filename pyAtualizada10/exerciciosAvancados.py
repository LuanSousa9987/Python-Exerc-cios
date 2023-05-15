# Criar uma lista com os números primos menores que 20

primos = []

for num in range(2, 20):
    for i in range(2, num):
        if num % i == 0:
            break
        else:
           
            primos.append(num)
print(primos)

# Calcular o fatorial de um número

num = 5
fatorial =1
for i in range(1, num+1):
    fatorial *= i
    print(fatorial)

# Vericar se uma String é um políndromo 

palavra = "reviver"

palindromo = True 

for i in range(len(palavra)):
    if palavra[i] != palavra[-i-1]:
        palindromo = False
        break
    if palindromo:
        print("É um palíndromo")
    else:
        print("Não é um palíndromo")


# Ordernar uma lista de números em ordem crescente

numeros = [7, 4, 2, 9, 1, 5]

for i in range(len(numeros)):

    for j in range(i+1, len(numeros)):

        if numeros [i] > numeros[j]:

            numeros[i],numeros[j] = numeros[j],numeros[i]
print(numeros)

# Calcular a raiz quadrada de um número usando o método de newton

num = 45 
raiz = num / 2 
while True:

    nova_raiz = (raiz + num / raiz) / 2

    if abs(raiz - nova_raiz) < 0.0001:
        break

    raiz = nova_raiz

print(raiz)
