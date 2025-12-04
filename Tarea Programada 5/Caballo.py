from Piece import Piece

class Caballo(Piece):

    def __str__(self):
        return f"Caballo en {self._column}{self._row}"

    def listar_movimientos(self):
        moves = []
        saltos = [
            (1, 2), (2, 1), (-1, 2), (-2, 1),
            (1, -2), (2, -1), (-1, -2), (-2, -1)
        ]
        for dc, dr in saltos:
            c = chr(ord(self._column) + dc)
            r = self._row + dr
            if self._valid(c, r):
                moves.append((c, r))
        return moves

    def es_movimiento_valido(self, col, row):
        return (col, row) in self.listar_movimientos()
