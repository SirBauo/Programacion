from Piece import Piece

class Arfil(Piece):

    def __str__(self):
        return f"Arfil en {self._column}{self._row}"

    def listar_movimientos(self):
        moves = []
        for d in range(1, 8):
            diagonales = [
                (d, d), (d, -d), (-d, d), (-d, -d)
            ]
            for dc, dr in diagonales:
                c = chr(ord(self._column) + dc)
                r = self._row + dr
                if self._valid(c, r):
                    moves.append((c, r))
        return moves

    def es_movimiento_valido(self, col, row):
        return (col, row) in self.listar_movimientos()
