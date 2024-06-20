# Escribir un programa que muestre por consola (con un print) los numeros de 1 a 100 (ambos incluidos y con un salto de linea entre cada impresión), sustituye los siguientes:
# - Multiplos de 3 por "Fizz"
# - Multiplos de 5 por "Buzz"
# - Multiplos de 3 y 5 por "FizzBuzz"
# - Los demás números se imprimen tal como son


# for i in range(1, 101):
#     if i % 3 == 0 and i % 5 == 0:
#         print("FizzBuzz")
#     elif i % 3 == 0:
#         print("Fizz")
#     elif i % 5 == 0:
#         print("Buzz")
#     else:
#         print(i)


def fizzbuzz():
    
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)
fizzbuzz()