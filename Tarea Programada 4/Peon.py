from Piece import Piece

class Peon(Piece):

    def __str__(self):
        return f"Peón en {self._column}{self._row}"

    def possible_moves(self):
        moves = []

        if self._valid(self._column, self._row + 1):
            moves.append((self._column, self._row + 1))

        return moves
