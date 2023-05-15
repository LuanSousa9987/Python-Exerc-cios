# Dicionário com as distâncias médias do sol para a lua em UA.
# Para calcular a distância da Terra em relação a outros planetas do Sistema Solar.
#Podemos utilizar os dados de distância média do Sol para cada planeta  e converter esses valores em quilômetros (km).
# UA (Unidade Astronômica).

distancias = {'Mercurio':0.39, 'Venus': 0.72, 'Terra ':1.0, 'Marte':1.52, 
'Jupiter': 5.20, 'Saturno':9.58, 'Urano': 19.18, "Netuno":30.7}

# Valor da unidade astronômica (UA) em km.

UA = 149597870.7

# Loop para calcular a distância da Terra para cada planeta em km.

for planeta, distancia_ua in distancias.items():
    distancia_km = distancia_ua * UA
    if planeta == 'Terra':
        continue
    print(f"A distância média entre a terra e {planeta} é de {distancia_km} km. ")


# Esse é um exemplo de um programa que utiliza a biblioteca Matplotlib.
# Para plotar a curvatura do espaço-tempo ao redor de um objeto massivo.



import numpy as np
import matplotlib.pyplot as plt 

# Definindo as constantes 



G = 6.6743e-11   # Constante gravitacional 
C = 299792458    # Velocidade da luz
M = 10           # Massa do objeto em unidades solares  

# Definindo as coordenas

x = np.linspace(-10, 10, 100)
y = np.linspace(-10, 10, 100)
xx, yy = np.meshgrid(x, y)
r = np.sqrt(xx**2 + yy**2)

# Calcula a curvatura do espaço-tempo

phi = -G * M / r
g00 = -1 -2 * phi / C**2
g11 = 1 + 2 * phi / C**2

# Plota a curvatura

plt.imshow(g00, cmap='collwarm')
plt.colorbar()
plt.title("Curvaura do espaço-tempo ao redor de um objeto massivo")
plt.xlabel("Cordenada X")
plt.xlabel("Cordenada y")
plt.show()

