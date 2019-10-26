# use row & col to iterate through 2D vector
class Vector2D:

    def __init__(self, v: List[List[int]]):
        self.row, self.col, self.v = 0, 0, v      

    def next(self) -> int:
        while self.row < len(self.v):
            while self.col < len(self.v[self.row]):
                result = self.v[self.row][self.col]
                self.col += 1
                return result
            self.col = 0
            self.row += 1      

    def hasNext(self) -> bool:
        while self.row < len(self.v):
            if self.col < len(self.v[self.row]):
                return True
            self.col = 0
            self.row += 1
        return False      


# Your Vector2D object will be instantiated and called as such:
# obj = Vector2D(v)
# param_1 = obj.next()
# param_2 = obj.hasNext()