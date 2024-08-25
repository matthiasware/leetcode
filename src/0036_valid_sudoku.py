"""
36. Determine if a 9 x 9 Sudoku board is valid.

Only the filled cells need to be validated according to the following rules:
- Each row must contain the digits 1-9 without repetition.
- Each column must contain the digits 1-9 without repetition.
- Each of the nine 3 x 3 sub-boxes of the grid must contain
  the digits 1-9 without repetition.

Note:
A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.


Constraints:
- board.length == 9
- board[i].length == 9
- board[i][j] is a digit 1-9 or '.'
"""

tests = [
    (
        [
            ["5", "3", ".", ".", "7", ".", ".", ".", "."],
            ["6", ".", ".", "1", "9", "5", ".", ".", "."],
            [".", "9", "8", ".", ".", ".", ".", "6", "."],
            ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
            ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
            ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
            [".", "6", ".", ".", ".", ".", "2", "8", "."],
            [".", ".", ".", "4", "1", "9", ".", ".", "5"],
            [".", ".", ".", ".", "8", ".", ".", "7", "9"],
        ],
        True,
    ),
    (
        [
            ["8", "3", ".", ".", "7", ".", ".", ".", "."],
            ["6", ".", ".", "1", "9", "5", ".", ".", "."],
            [".", "9", "8", ".", ".", ".", ".", "6", "."],
            ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
            ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
            ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
            [".", "6", ".", ".", ".", ".", "2", "8", "."],
            [".", ".", ".", "4", "1", "9", ".", ".", "5"],
            [".", ".", ".", ".", "8", ".", ".", "7", "9"],
        ],
        False,
    ),
    (
        [
            ["1", "2", ".", ".", "3", ".", ".", ".", "."],
            ["4", ".", ".", "5", ".", ".", ".", ".", "."],
            [".", "9", "1", ".", ".", ".", ".", ".", "3"],
            ["5", ".", ".", ".", "6", ".", ".", ".", "4"],
            [".", ".", ".", "8", ".", "3", ".", ".", "5"],
            ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
            [".", ".", ".", ".", ".", ".", "2", ".", "."],
            [".", ".", ".", "4", "1", "9", ".", ".", "8"],
            [".", ".", ".", ".", "8", ".", ".", "7", "9"],
        ],
        False,
    ),
]


def is_valid_sukdoku(board: list[list[str]]) -> bool:
    # check rows
    for i_row in range(9):
        elems = set()
        for i_col in range(9):
            x = board[i_row][i_col]
            if x == ".":
                continue
            if x in elems:
                return False
            elems.add(x)
    # check columns
    for i_col in range(9):
        elems = set()
        for i_row in range(9):
            x = board[i_row][i_col]
            if x == ".":
                continue
            if x in elems:
                return False
            elems.add(x)
    # check boxes
    for i_row in range(3):
        for i_col in range(3):
            elems = set()
            row_slice = slice(i_row * 3, i_row * 3 + 3)
            col_slice = slice(i_col * 3, i_col * 3 + 3)
            box = [row[col_slice] for row in board[row_slice]]
            box = [x for row in box for x in row]
            for n in box:
                if n == ".":
                    continue
                if n in elems:
                    return False
                elems.add(n)
    return True


if __name__ == "__main__":
    for board, exp in tests:
        act = is_valid_sukdoku(board)
        assert act == exp
