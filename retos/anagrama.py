# escriba una funcion que reciba dos palabras (String) y retorne verdadero o falso (bool) según sean o no anagramas.
# Un anagrama es una palabra o frase que se forma reordenando las letras de otra palabra inicial.
# No hace falta comprobar que ambas palabras existan.
# Dos palabras exactamente iguales no son anagrama

def son_anagramas(palabra1, palabra2):
    palabra1 = palabra1.lower().replace("", "")
    palabra2 = palabra2.lower().replace("", "")
    # Verificacion de la longitud
    if len(palabra1) != len(palabra2):
        return False

    # Ordenar las letras de ambas palabras y comparar
    return sorted(palabra1) == sorted(palabra2)

# salidas
print(son_anagramas("listen", "silent")) #True
print(son_anagramas("tomate", "temato")) #True
print(son_anagramas("roma", "amor")) #True
print(son_anagramas("arroba", "aroma")) #False