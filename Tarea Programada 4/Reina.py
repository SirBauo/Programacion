from Piece import Piece

class Reina(Piece):

    def __str__(self):
        return f"Reina en {self._column}{self._row}"

    def possible_moves(self):
        moves = []
        for d in range(1, 8):
            dirs = [
                (d, d), (d, -d), (-d, d), (-d, -d),
                (d, 0), (-d, 0), (0, d), (0, -d)
            ]
            for dc, dr in dirs:
                c = chr(ord(self._column) + dc)
                r = self._row + dr
                if self._valid(c, r):
                    moves.append((c, r))
        return moves
