from Piece import Piece

class Torre(Piece):

    def __str__(self):
        return f"Torre en {self._column}{self._row}"

    def possible_moves(self):
        moves = []
        for d in range(1, 8):
            for c, r in [
                (self._column, self._row + d),
                (self._column, self._row - d),
                (chr(ord(self._column) + d), self._row),
                (chr(ord(self._column) - d), self._row),
            ]:
                if self._valid(c, r):
                    moves.append((c, r))
        return moves
