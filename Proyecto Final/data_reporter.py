import json
from utils import is_number

class DataReporter:

    def __init__(self, data, logger):
        self.data = data
        self.logger = logger

    def create_report(self):
        cols = self.data[0].keys()

        reporte = {
            "columnas": [],
            "rows_totales": len(self.data),
            "columnas_con_vacios": []
        }

        for col in cols:
            muestra = next((row[col] for row in self.data if row[col] != ""), "")
            tipo = "numérico" if is_number(muestra) else "alfanumérico"
            reporte["columnas"].append({"nombre": col, "tipo": tipo})

            if any(row[col] == "" for row in self.data):
                reporte["columnas_con_vacios"].append(col)

        with open("reporte.json", "w", encoding="utf-8") as f:
            json.dump(reporte, f, indent=4)

        print("Reporte generado: reporte.json")
        self.logger.log("", "generar_reporte", "")
