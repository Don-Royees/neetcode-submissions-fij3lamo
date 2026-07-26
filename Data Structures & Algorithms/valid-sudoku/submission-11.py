class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        for row in range(9):
            check_set = set()
            for y in range(9):
                if board[row][y] != ".":
                    if board[row][y] in check_set:
                        return False
                    check_set.add(board[row][y])

        for column in range(9):
            check_set= set()
            for x in range(9):
                if board[x][column] != ".":
                    if board[x][column] in check_set:
                        return False
                    check_set.add(board[x][column])


        for sq_row in range(0,9,3):
            for sq_column in range(0,9,3):
                check_set = set()
                for x in range(3):
                    for y in range(3):
                        item = board[sq_row + x][sq_column + y]
                        if item in check_set and item != ".":
                            return False 
                        check_set.add(item)
        return True                        
