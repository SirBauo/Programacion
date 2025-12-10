from utils import is_number

class DataCleaner:

    def __init__(self, data, logger):
        self.data = data
        self.logger = logger

    def menu(self):
        columnas = input("Columnas a filtrar (coma-separadas): ").split(",")
        filtrado = self.data

        for col in columnas:
            col = col.strip()
            muestra = next((row[col] for row in self.data if row[col] != ""), "")

            if is_number(muestra):
                low = float(input(f"[{col}] mínimo: "))
                high = float(input(f"[{col}] máximo: "))
                filtrado = [
                    row for row in filtrado
                    if row[col] != "" and low <= float(row[col]) <= high
                ]
            else:
                txt = input(f"[{col}] texto a buscar: ")
                filtrado = [
                    row for row in filtrado
                    if txt.lower() in row[col].lower()
                ]

        filename = "dataset_limpio.csv"
        import csv
        with open(filename, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=self.data[0].keys())
            writer.writeheader()
            writer.writerows(filtrado)

        print("Dataset limpio creado:", filename)
        self.logger.log("", "limpiar_dataset", str(columnas))
