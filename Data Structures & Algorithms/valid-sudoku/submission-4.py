class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        for col in range(len(board)):
            dec_row = set()
            for row in range(len(board[col])):
                if board[col][row] in dec_row:
                    return False
                if board[col][row] != ".":
                    dec_row.add(board[col][row])
        
          
        for row in range(len(board[0])):
            dec_col = set()
            for col in range(len(board)):
                if board[col][row] in dec_col:
                    return False
                if board[col][row] != ".":
                    dec_col.add(board[col][row]) 
        
        for i_col in range(0, len(board), 3):
            for i_row in range(0, len(board[i_col]), 3):
                dec_min = set()
                for row in range(3):
                    for col in range(3):
                        if board[i_col + col][i_row + row] in dec_min:
                            return False
                        if board[i_col + col][i_row + row] != ".":
                            dec_min.add(board[i_col + col][i_row + row]) 

        return True





