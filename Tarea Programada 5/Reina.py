from Piece import Piece

class Reina(Piece):

    def __str__(self):
        return f"Reina en {self._column}{self._row}"

    def listar_movimientos(self):
        moves = []
        for d in range(1, 8):
            direcciones = [
                (d, 0), (-d, 0), (0, d), (0, -d),      
                (d, d), (d, -d), (-d, d), (-d, -d)     
            ]
            for dc, dr in direcciones:
                c = chr(ord(self._column) + dc)
                r = self._row + dr
                if self._valid(c, r):
                    moves.append((c, r))
        return moves

    def es_movimiento_valido(self, col, row):
        return (col, row) in self.listar_movimientos()
