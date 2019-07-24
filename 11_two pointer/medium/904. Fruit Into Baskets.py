import collections
class Solution:
    def totalFruit(self, tree: List[int]) -> int:
        basket = collections.Counter()
        res, first = 0, 0
        for last in range(len(tree)):
            basket[tree[last]] += 1
            while len(basket) == 3:
                basket[tree[first]] -= 1
                if basket[tree[first]] == 0:
                    basket.pop(tree[first])
                first += 1
            res = max(res, last-first+1)
        return res
                