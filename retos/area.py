# Crea una única función (importante que solo sea una) que sea capaz de calcular y retornar el área de un polígono.
# La función recibirá por parámetro sólo Un polígono a la vez.
# Los polígonos soportados serán Triángulo, Cuadrado y Rectángulo.
# Imprima el área de un polígono de cada tipo

# def calcular_area_poligono(tipo, *args):
#     tipo = tipo.lower()

#     if tipo == "triangulo":
#         base, altura = args
#         area = (base * altura) / 2
#         print(f"El area del triangulo con base {base} y altura {altura} es: {area}")
#         return area
#     elif tipo == "cuadrado":
#         lado = args[0]
#         area = lado * lado
#         print(f"El area del cuadrado con lado {lado} es: {area}")
#         return area
#     elif tipo == "rectangulo":
#         base, altura = args
#         area = base * altura
#         print(f"El area del rectangulo con base {base} y altura {altura} es: {area}")
#         return area
#     else:
#         print(f"No se reconoce el tipo de poligono '{tipo}'.")
#         return None
    
# # salida
# calcular_area_poligono("triangulo", 54, 14)
# calcular_area_poligono("cuadrado", 40)
# calcular_area_poligono("rectangulo", 10, 25)

# VERSION MAS CORTA

def cal_area_poli(tipo, *args):
    areas = {
        "triangulo": lambda base, altura: (base * altura) / 2,
        "cuadrado": lambda lado: lado * lado,
        "rectangulo": lambda base, altura: base * altura
    }
    
    tipo = tipo.lower()
    if tipo in areas:
        area = areas[tipo](*args)
        print(f"El área del {tipo} es: {area}")
        return area
    else:
        print(f"No se reconoce el tipo de poligono '{tipo}'.")

# salida
cal_area_poli("triangulo", 54, 14)
cal_area_poli("cuadrado", 40)
cal_area_poli("rectangulo", 10, 25)