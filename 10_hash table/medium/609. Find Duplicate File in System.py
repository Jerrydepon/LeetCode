# use of 'partition()'
# use of 'defaultdict(list)'
import collections

class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        dic = collections.defaultdict(list)
        for path in paths:
            path = path.split()
            root = path[0]
            for file in path[1:]:
                index, _, name = file.partition('(')
                dic[name[:-1]].append(root + '/' + index)
                
        return [groups for groups in dic.values() if len(groups) > 1]