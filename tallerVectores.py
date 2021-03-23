import numpy as np
# De los n elementos de un vector dado calcule:
# a. La sumatoria
# b. La productoria
# c. El Mayor Elemento
# d. El menor Elemento
cantidad = int(input('Ingrese la cantidad de numeros: '))
vector = []
productoria = 1
for i in range(1, cantidad + 1):
    numeros = int(input(f'Ingrese el numero {i}: '))
    vector.append(numeros)
for j in vector:
    productoria *= j

suma = sum(vector)
menor = min(vector)
mayor = max(vector)
print(f'El resultado de la sumatoria es: {suma}')
print(f'El resultado de la productoria es: {productoria}')
print(f'El numero mas pequeño ingresado fue: {menor}')
print(f'El numero mas grande ingresado fue: {mayor}')

# De los n elementos de un vector dado calcule:
# a. Cantidad de elementos pares
# b. Cantidad de elementos impares
# c. Cantidad de elementos primos
cantidad = int(input('Ingrese la cantidad de numeros: '))
vector = []
contPar = 0
contImpar = 0
contPrimo = 0
productoria = 1
for i in range(1, cantidad + 1):
    numeros = int(input(f'Ingrese el numero {i}: '))
    vector.append(numeros)
for j in vector:
    if j % 2 == 0:
        contPar += 1
    if j % 2 != 0:
        contImpar += 1

print(f'La cantidad de numeros pares son :{contPar}')
print(f'La cantidad de numeros impares son :{contImpar}')
# print(f'La cantidad de numeros primos son :{contPrimo}')

# Dado un Vector v y un Vector v1 de cómo resultado un Vector resultante de
# las siguientes operaciones:
# a. Suma
# b. Resta
cantidad = int(input('Ingrese la cantidad de numeros: '))
v = []
v1 = []
vector = []
vector1 = []
for i in range(1, cantidad + 1):
    numeros = int(input(f'Ingrese el numero {i} para el primer vector: '))
    v.append(numeros)
    numeros2 = int(input(f'Ingrese el numero {i} para el segundo vector: '))
    v1.append(numeros2)
vector = np.array(v)
vector1 = np.array(v1)
suma = vector + vector1
resta = vector - vector1
print(f'El vector resultante de la suma es: {suma}')
print(f'El vector resultante de la resta es: {resta}')

# De los n elementos de un vector dado identifique el número que mas se
# repite e indique cual es.


# Dado un Vector v de longitud par, divida en 2 partes, en la primera parte
# realice la productoria y en la segunda la sumatoria. Entregue los valores
# resultantes
cantidad = int(input('Ingrese la cantidad de numeros: '))
vector = []
productoria = 1
if cantidad % 2 == 0:
    for i in range(1, cantidad + 1):
        numeros = int(input(f'Ingrese el numero {i}: '))
        vector.append(numeros)
    p1 = vector[:int(len(vector)/2)]
    p2 = vector[int(len(vector)/2):]
    for j in p1:
        productoria *= j
    suma = sum(p2)
    print(f'La productoria de la primera parte es: {productoria}')
    print(f'La sumatoria de la segunda part es: {suma}')
else:
    print('El tamaño del vector debe ser par')
# Dado un vector v, indique si es simétrico, un vector es simétrico si siendo
# longitud par los números de la primera mitad son iguales al inverso de la
# otra mitad por ejemplo: X=[1,2,3,3,2,1], en el ejemplo x es un vector
# simétrico, en caso que la longitud del vector sea impar, se ignorará el
# elemento central y se seguirá la misma lógica anterior, por ejemplo:
# Y=[3,5,7,8,7,5,3], en este ejemplo Y es simétrico.
cantidad = int(input('Ingrese la cantidad de numeros: '))
vector = []

for i in range(1, cantidad + 1):
    numeros = int(input(f'Ingrese el numero {i}: '))
    vector.append(numeros)
p1 = vector[:int(len(vector)/2)]
if cantidad % 2 == 0:
    p2 = vector[int(len(vector)/2):]
else:
    p2 = vector[int(len(vector)/2)+1:]
p2.reverse()
if p1 == p2:
    print('El vector es simetrico')
else:
    print('El vector no es simetrico')

