#patron para evitar un monton de ifs si usted tiene que llamar funciones 
#que implementan distintas versiones de un algoritmo y reciben los mismos 
#parametro

def sumar(a,b):
    return a+b

def restar(a,b):
    return a - b

def multiplicar(a,b):
    return a * b

def dividir(a,b):
    return a/b

operaciones = {
    "suma": sumar,
    "resta": restar,
    "multi": multiplicar,
    "div": dividir
}    

def ejecutar_operacion(operacion, valor_1, valor_2):
    if operacion not in operaciones:
        print("esa operacion es invalida")
    else:
        mi_funcion = operaciones[operacion]
        print(f"la operacion {operacion} tiene por resultado {mi_funcion(valor_1,valor_2)}")

ejecutar_operacion("suma",2,3)
ejecutar_operacion("resta",2,3)
ejecutar_operacion("multi",2,3)
ejecutar_operacion("multiplicacion",2,3)