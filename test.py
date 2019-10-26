class Solution(object):
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        if not matrix or not matrix[0]: return 0
        m = len(matrix)
        n = len(matrix[0])
        res = [[0] * n for _ in range(m)]
        visited = [[0] * n for _ in range(m)]
        for x in range(m):
            for y in range(n):
                res[x][y] = self.helper(matrix, x, y, visited)
        print(res)
        return max(res[x][y] for x in range(m) for y in range(n))


    def helper(self, matrix, x, y, visited):
        step = 0
        if not visited[x][y]:
            visited[x][y] = 1
            for i in range(-1, 2):
                for j in range(-1, 2):
                    dx = i + x
                    dy = j + y
                    if (0 <= dx < len(matrix)
                            and 0 <= dy < len(matrix)
                            and not visited[dx][dy]
                            and abs(matrix[x][y] - matrix[dx][dy]) > 3):
                        s = self.helper(matrix, dx, dy, visited)
                        if s > step:
                            step = s
            visited[x][y] = 0
        return step + 1

# a = [[8,2,4],[0,6,1],[3,7,9]]
a = [[7,1,5,7],[2,8,3,9],[3,6,1,4],[5,1,7,3]]
print(Solution().longestIncreasingPath(a))