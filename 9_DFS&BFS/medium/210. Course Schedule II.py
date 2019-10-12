# If the tree contains cycle, the returned dictionary dic would not be empty. Therefore the dfs function will return []
import collections
class Solution:
    
    # # BFS
    # def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
    #     dic = {i: set() for i in range(numCourses)}
    #     neigh = collections.defaultdict(set)
    #     for i, j in prerequisites:
    #         dic[i].add(j)
    #         neigh[j].add(i)
    #     # queue stores the courses which have no prerequisites
    #     queue = collections.deque([i for i in dic if not dic[i]])
    #     count, res = 0, []
    #     while queue:
    #         node = queue.popleft()
    #         res.append(node)
    #         count += 1
    #         for i in neigh[node]:
    #             dic[i].remove(node)
    #             if not dic[i]:
    #                 queue.append(i)
    #     return res if count == numCourses else []

    # DFS
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        dic = collections.defaultdict(set)
        neigh = collections.defaultdict(set)
        for i, j in prerequisites:
            dic[i].add(j)
            neigh[j].add(i)
        stack = [i for i in range(numCourses) if not dic[i]]
        count, res = 0, []
        while stack:
            node = stack.pop()
            res.append(node)
            count += 1
            for i in neigh[node]:
                dic[i].remove(node)
                if not dic[i]:
                    stack.append(i)
        return res if count == numCourses else []