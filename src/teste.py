from enum import Enum
from enum import auto
from colorama import init, Fore, Back, Style


class Color(Enum):
    WHITE = 0
    BLACK = 1


class Piece(Enum):
    EMPTY = auto()
    PAWN = auto()
    ROOK = auto()
    KNIGHT = auto()
    BISHOP = auto()
    KING = auto()
    QUEEN = auto()


ELEMENTS = {
    (Color.WHITE, Piece.EMPTY): Back.LIGHTBLACK_EX,
    (Color.WHITE, Piece.KING): f'{Fore.LIGHTWHITE_EX}\u265A',
    (Color.WHITE, Piece.QUEEN): f'{Fore.LIGHTWHITE_EX}\u265B',
    (Color.WHITE, Piece.ROOK): f'{Fore.LIGHTWHITE_EX}\u265C',
    (Color.WHITE, Piece.BISHOP): f'{Fore.LIGHTWHITE_EX}\u265D',
    (Color.WHITE, Piece.KNIGHT): f'{Fore.LIGHTWHITE_EX}\u265E',
    (Color.WHITE, Piece.PAWN): f'{Fore.LIGHTWHITE_EX}\u265F',
    (Color.BLACK, Piece.EMPTY): Back.LIGHTCYAN_EX,
    (Color.BLACK, Piece.KING): f'{Fore.BLACK}\u265A',
    (Color.BLACK, Piece.QUEEN): f'{Fore.BLACK}\u265B',
    (Color.BLACK, Piece.ROOK): f'{Fore.BLACK}\u265C',
    (Color.BLACK, Piece.BISHOP): f'{Fore.BLACK}\u265D',
    (Color.BLACK, Piece.KNIGHT): f'{Fore.BLACK}\u265E',
    (Color.BLACK, Piece.PAWN): f'{Fore.BLACK}\u265F'
}


def init_tiles():
    row = [ELEMENTS[(Color(i % 2), Piece.EMPTY)] for i in range(8)]
    return [row if i % 2 == 0 else row[::-1] for i in range(8)]


def init_board():

    def get_army(color):
        return [
            (color, Piece.ROOK),
            (color, Piece.KNIGHT),
            (color, Piece.BISHOP),
            (color, Piece.QUEEN),
            (color, Piece.KING),
            (color, Piece.BISHOP),
            (color, Piece.KNIGHT),
            (color, Piece.ROOK)
        ]

    return (
        [
            get_army(Color.BLACK),
            [(Color.BLACK, Piece.PAWN) for _ in range(8)],
            *[[None] * 8 for _ in range(4)],
            [(Color.WHITE, Piece.PAWN) for _ in range(8)],
            get_army(Color.WHITE)
        ]
    )


def print_board(board, flip=False):

    def flip_board(board):
        return [row[::-1] for row in reversed(board)]

    for i, row in enumerate(board if not flip else flip_board(board)):
        for j, piece in enumerate(row):
            piece = ELEMENTS.get(piece)
            print(f"{tiles[i][j]}{piece if piece else ' '}",
                  Style.RESET_ALL, end='', flush=True)
        print()


if __name__ == '__main__':
    init()
    tiles = init_tiles()
    board = init_board()
    print_board(board)