# use defaultdict(list) to make value a list
# find path lexically
# if cannot find a path, restore the route and dictionary for next path
# stop searching if find a path
import collections

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        dic = collections.defaultdict(list)
        for ticket in tickets:
            dic[ticket[0]].append(ticket[1])
        self.res, self.route, self.len_route = None, ['JFK'], len(tickets)+1
        self.findRoute(dic, 'JFK')
        return self.res
    
    def findRoute(self, dic, start):
        if len(self.route) == self.len_route:
            self.res = self.route
            return
        des_li = sorted(dic[start])
        for des in des_li:
            self.route.append(des)
            dic[start].remove(des)
            self.findRoute(dic, des)
            if self.res:
                return
            self.route.pop()
            dic[start].append(des)
            