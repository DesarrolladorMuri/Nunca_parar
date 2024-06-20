# Escribe un programa que imprima los primeros 50 números de la secuencia de fibonacci empezando en 0.
# La secuencia de fibonacci es una serie de números en la que cada número es la suma de los anteriors.
# 0, 1, 1, 2, 3, 5, 8, 13...

# def fibonacci_secuencia(n):
#     fib_secuencia = [0, 1]
#     for i in range(2, n):
#         fib_secuencia.append(fib_secuencia[-1] + fib_secuencia[-2])
        
#     return fib_secuencia

# resultado = fibonacci_secuencia(50)
# print(resultado)

# SEGUNDA FORMA DE REALIZARLO

def fibonacci_secuencia(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fib_secuencia = fibonacci_secuencia(n - 1)
        fib_secuencia.append(fib_secuencia[-1] + fib_secuencia[-2])
        return fib_secuencia

# imprimir los primeros 50 números de Fibonacci
resultado = fibonacci_secuencia(50)
print(resultado)