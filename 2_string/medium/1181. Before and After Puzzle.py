# brute force
# use tuple to avoid error of unhashable type: 'list'
class Solution:
    def beforeAndAfterPuzzles(self, phrases: List[str]) -> List[str]:
        phrases = [st.split(" ") for st in phrases]
        tmp = set()
        for i in range(len(phrases)):
            for j in range(len(phrases)):
                if i != j:
                    if phrases[i][-1] == phrases[j][0]:
                        tmp.add(tuple(phrases[i]+phrases[j][1:]))

        res = [" ".join(lst) for lst in tmp]
        return sorted(res)        