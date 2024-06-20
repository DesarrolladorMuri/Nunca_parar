# Escriba un programa que se encargue de comprobar si un numero es o no primo
# Hecho esto, imprima los números primos entres 1 y 100
import math

# def es_primo(n):
#     if n <= 1:
#         return False
#     elif n == 2:
#         return True
#     elif n % 2 == 0:
#         return False
    
#     sqrt_n = int(math.sqrt(n)) + 1
#     for i in range(3, sqrt_n, 2):
#         if n % i == 0:
#             return False
#     return True

# # Salida de numeros
# print(es_primo(2))
# print(es_primo(5))
# print(es_primo(8))
# print(es_primo(10))

# # imoprimir todos los numeros
# print("Números primpos entre el 1 y el 100:")

# for num in range(1, 101):
#     if es_primo(num):
#         print(num, end=" ")

# # Especificar un salto de linea para los números    
# print()

# VERSION MAS COMPRIMIDA

def es_primo(n):
    return n > 1 and all(n % i != 0 for i in range(2, int(n**0.5) + 1))

print("Búmeros primos entre 1 y 100:")
print(*(num for num in range(1, 101) if es_primo(num)))