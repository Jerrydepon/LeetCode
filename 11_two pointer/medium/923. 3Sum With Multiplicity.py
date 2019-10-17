# itertools.combinations_with_replacement(c, 2) for 2 elements
# 3 cases covers all possible combination

# 3 <= A.length <= 3000, so N = 3000
# But 0 <= A[i] <= 100
# So my solution is O(N + 101 * 101)

class Solution:
    def threeSumMulti(self, A: List[int], target: int) -> int:
        c = collections.Counter(A)
        res = 0
        for i, j in itertools.combinations_with_replacement(c, 2):
            k = target - i - j
            if i == j == k: 
                res += c[i] * (c[i] - 1) * (c[i] - 2) // 6
            elif i == j != k: 
                res += c[i] * (c[i] - 1) // 2 * c[k]
            elif k > i and k > j: 
                res += c[i] * c[j] * c[k]
        return res % (10**9 + 7)