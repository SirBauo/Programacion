class OperationLogger:

    def __init__(self, filename):
        self.filename = filename

    def log(self, dataset, operacion, parametros):
        with open(self.filename, "a", encoding="utf-8") as f:
            f.write(f"{dataset} | {operacion} | {parametros}\n")

    def show_all(self):
        try:
            with open(self.filename, "r", encoding="utf-8") as f:
                print(f.read())
        except FileNotFoundError:
            print("No hay registros.")
