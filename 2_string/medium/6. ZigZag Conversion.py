class Solution:
    def convert(self, s: str, numRows: int) -> str:
        li = ['' for _ in range(numRows)]
        step = 0 if numRows == 1 else -1
        idx, last = 0, numRows-1
        for d in s:
            li[idx] += d
            if idx == 0 or idx == last:
                step *= -1
            idx += step
        return ''.join(li)
        