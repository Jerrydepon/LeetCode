# mark visit[i] = 1 for valid course
# mark visit[i] = -1 for under checking
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for _ in range(numCourses)]
        visit = [0] * numCourses
        for adv, pre in prerequisites:
            graph[adv].append(pre)
        for i in range(len(graph)):
            if not self.findPrereq(i, graph, visit):
                return False
        return True
            
    def findPrereq(self, i, graph, visit):
        if visit[i] == -1:
            return False
        elif visit[i] == 1:
            return True
        visit[i] = -1
        for j in graph[i]:
            if not self.findPrereq(j, graph, visit):
                return False
        visit[i] = 1
        return True