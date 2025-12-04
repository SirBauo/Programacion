from abc import ABC, abstractmethod

class Piece(ABC):

    def __init__(self, column, row):
        self._column = column
        self._row = row

    @property
    def column(self):
        return self._column

    @column.setter
    def column(self, new_col):
        self._column = new_col

    @property
    def row(self):
        return self._row

    @row.setter
    def row(self, new_row):
        self._row = new_row

    def _valid(self, c, r):
        return "a" <= c <= "h" and 1 <= r <= 8

    @abstractmethod
    def listar_movimientos(self):
        """Debe retornar una lista de tuplas (col, row)."""
        pass

    @abstractmethod
    def es_movimiento_valido(self, col, row):
        """Debe retornar True/False."""
        pass

    def __str__(self):
        return f"Pieza en {self._column}{self._row}"
