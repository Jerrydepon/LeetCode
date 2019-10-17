# find the biggest distance at the start, in the middle, and at the end
class ExamRoom:

    def __init__(self, N: int):
        self.number, self.room = N, []

    def seat(self) -> int:
        if not self.room: 
            res = 0
        else:
            d, res = self.room[0], 0
            for a, b in zip(self.room, self.room[1:]):
                if (b - a) // 2 > d:
                    d = (b - a) // 2
                    res = (b + a) // 2
            if self.number - 1 - self.room[-1] > d: 
                res = self.number - 1
        bisect.insort(self.room, res)
        return res        

    def leave(self, p: int) -> None:
        self.room.remove(p)


# Your ExamRoom object will be instantiated and called as such:
# obj = ExamRoom(N)
# param_1 = obj.seat()
# obj.leave(p)