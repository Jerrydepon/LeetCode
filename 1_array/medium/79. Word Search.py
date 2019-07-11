class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    if self.findWord(i, j, board, word, 0):
                        return True
        return False
    
    def findWord(self, i, j, board, word, index):
        if i < 0 or j < 0 or i >= len(board) or j >= len(board[0]) or board[i][j] == "#":
            return False
        if board[i][j] == word[index]:
            if index == len(word)-1:
                return True
            tmp = board[i][j]
            board[i][j] = "#"
            res = self.findWord(i-1, j, board, word, index+1) \
                    or self.findWord(i+1, j, board, word, index+1) \
                    or self.findWord(i, j-1, board, word, index+1) \
                    or self.findWord(i, j+1, board, word, index+1)
            board[i][j] = tmp
            return res
        else:
            return False
        