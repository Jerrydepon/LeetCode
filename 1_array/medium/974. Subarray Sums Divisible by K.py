# initialize 1 for modulus 0
# add 1 to number of combination
class Solution:
    def subarraysDivByK(self, A: List[int], K: int) -> int:
        li = [1] + (K-1) * [0]
        res, sum_ = 0, 0
        for a in A:
            sum_ += a
            idx = sum_ % K
            res += li[idx]
            li[idx] += 1
        return res