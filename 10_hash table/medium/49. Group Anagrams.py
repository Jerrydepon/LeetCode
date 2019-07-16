class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # # redundant
        # if strs == []:
        #     return []
        # dic, output = {}, []
        # for i, s in enumerate(strs):
        #     sorted_s = "".join(sorted(s))
        #     dic[sorted_s] = dic.get(sorted_s, []) + [i]
        # for k, v in dic.items():
        #     group = []
        #     for index in v:
        #         group.append(strs[index])
        #     output.append(group)
        # return output
        
        d = {}
        for w in strs:
            key = tuple(sorted(w))
            d[key] = d.get(key, []) + [w]
        return list(d.values())
            