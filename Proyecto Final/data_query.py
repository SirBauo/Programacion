import os
from utils import is_number

class DataQuery:

    def __init__(self, data, logger):
        self.data = data
        self.logger = logger

    def menu(self):
        print("\nCONSULTAR DATASET")
        print("1. Listar columnas")
        print("2. Listar columnas y tipos")
        print("3. Listar valores distintos")
        print("4. Consultar por rango o texto")
        op = input("Opción: ")

        if op == "1":
            print(list(self.data[0].keys()))
            self.logger.log("", "listar_columnas", "")

        elif op == "2":
            for col in self.data[0].keys():
                tipo = "numérico" if is_number(self.data[0][col]) else "alfanumérico"
                print(col, tipo)
            self.logger.log("", "listar_columnas_tipos", "")

        elif op == "3":
            col = input("Columna: ")
            valores = {row[col] for row in self.data}
            if len(valores) > 50:
                print("Muchos valores:", len(valores))
            else:
                print(valores)

            exp = input("Exportar a archivo? (s/n): ")
            if exp == "s":
                filename = f"output-{col}.txt"
                with open(filename, "w", encoding="utf-8") as f:
                    for v in valores:
                        f.write(str(v) + "\n")
                print("Guardado:", filename)

            self.logger.log("", "valores_distintos", col)

        elif op == "4":
            col = input("Columna: ")
            muestra = next(v[col] for v in self.data if v[col] != "")
            if is_number(muestra):
                low = float(input("Valor mínimo: "))
                high = float(input("Valor máximo: "))
                filtrados = [
                    row for row in self.data
                    if row[col] != "" and low <= float(row[col]) <= high
                ]
            else:
                txt = input("Texto a buscar: ")
                filtrados = [row for row in self.data if txt.lower() in row[col].lower()]

            print("Coincidencias:", len(filtrados))

            exp = input("Guardar resultados? (s/n): ")
            if exp == "s":
                filename = f"consulta-{col}.txt"
                with open(filename, "w", encoding="utf-8") as f:
                    for row in filtrados:
                        f.write(str(row) + "\n")
                print("Guardado:", filename)

            self.logger.log("", "consulta_columna", col)
