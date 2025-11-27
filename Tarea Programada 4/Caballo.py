from Piece import Piece

class Caballo(Piece):

    def __str__(self):
        return f"Caballo en {self._column}{self._row}"

    def possible_moves(self):
        moves = []
        jumps = [
            (1, 2), (2, 1), (-1, 2), (-2, 1),
            (1, -2), (2, -1), (-1, -2), (-2, -1)
        ]
        for dc, dr in jumps:
            c = chr(ord(self._column) + dc)
            r = self._row + dr
            if self._valid(c, r):
                moves.append((c, r))
        return moves
