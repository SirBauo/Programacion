from Piece import Piece

class Peon(Piece):

    def __str__(self):
        return f"Peón en {self._column}{self._row}"

    def listar_movimientos(self):
        moves = []
        if self._valid(self._column, self._row + 1):
            moves.append((self._column, self._row + 1))
        return moves

    def es_movimiento_valido(self, col, row):
        return (col, row) in self.listar_movimientos()
