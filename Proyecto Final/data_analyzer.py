from utils import is_number
import math

class DataAnalyzer:

    def __init__(self, data, logger):
        self.data = data
        self.logger = logger

    def menu(self):
        print("\nANALIZAR DATOS")
        col = input("Columna numérica: ")

        valores = [float(row[col]) for row in self.data if is_number(row[col])]
        if not valores:
            print("No es numérica.")
            return

        print("Máximo:", max(valores))
        print("Mínimo:", min(valores))
        print("Promedio:", sum(valores)/len(valores))

        var = sum((x - sum(valores)/len(valores))**2 for x in valores) / len(valores)
        print("Varianza:", var)
        print("Desviación estándar:", math.sqrt(var))

        self.logger.log("", "analizar_columna", col)
