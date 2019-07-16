from copy import deepcopy

class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        for i in range(len(board)):
            for j in range(len(board[0])):
                self.changeState(board, i, j)
                           
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 2:
                    board[i][j] = 1
                elif board[i][j] == 3:
                    board[i][j] = 0
    
    def changeState(self, board, i, j):
        neighbor = 0
        if i-1 >= 0 and j-1 >= 0: neighbor += board[i-1][j-1] % 2
        if i-1 >= 0: neighbor += board[i-1][j] % 2
        if i-1 >= 0 and j+1 < len(board[0]): neighbor += board[i-1][j+1] % 2 
        if j-1 >= 0: neighbor += board[i][j-1] % 2
        if j+1 < len(board[0]): neighbor += board[i][j+1] % 2                   
        if i+1 < len(board) and j-1 >= 0: neighbor += board[i+1][j-1] % 2
        if i+1 < len(board): neighbor += board[i+1][j] % 2
        if i+1 < len(board) and j+1 < len(board[0]): neighbor += board[i+1][j+1] % 2
        
        if board[i][j] == 0 and neighbor == 3:
            board[i][j] = 2                   
        elif board[i][j] == 1 and (neighbor < 2 or neighbor > 3):
            board[i][j] = 3           