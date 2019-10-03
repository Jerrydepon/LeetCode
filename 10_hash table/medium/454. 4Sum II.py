# similar to 2sum, but divide 4 lists into two pairs
class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        hashtable, count = {}, 0
        for a in A:
            for b in B :
                if a + b in hashtable :
                    hashtable[a+b] += 1
                else :
                    hashtable[a+b] = 1        
        for c in C :
            for d in D :
                if -c - d in hashtable :
                    count += hashtable[-c-d]
        return count        