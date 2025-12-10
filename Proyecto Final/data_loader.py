import csv
import os

class DataLoader:

    def load(self, filename):
        path = os.path.join("data", filename)
        with open(path, newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            data = list(reader)
        return data
