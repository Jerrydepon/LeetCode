# the method is similar to Q.84, but check the height by layer
class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0
        
        res = 0
        height = [0] * (len(matrix[0]) + 1)
        for row in matrix:
            for i in range(len(matrix[0])):
                height[i] = height[i] + 1 if row[i] == '1' else 0
            # print(height)
            position = [-1]
            for j in range(len(height)):
                while height[j] < height[position[-1]]:
                    h = height[position.pop()]
                    w = j - position[-1] - 1
                    res = max(res, h*w)
                position.append(j)                
        return res
                       