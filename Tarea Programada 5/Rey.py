from Piece import Piece

class Rey(Piece):

    def __str__(self):
        return f"Rey en {self._column}{self._row}"

    def listar_movimientos(self):
        moves = []
        for dc in [-1, 0, 1]:
            for dr in [-1, 0, 1]:
                if dc == 0 and dr == 0:
                    continue
                c = chr(ord(self._column) + dc)
                r = self._row + dr
                if self._valid(c, r):
                    moves.append((c, r))
        return moves

    def es_movimiento_valido(self, col, row):
        return (col, row) in self.listar_movimientos()
