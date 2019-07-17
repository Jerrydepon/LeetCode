"""
# Definition for a Node.
class Node:
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors
"""
import collections

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None
        
        copyNode = Node(node.val, [])
        dic = {node:copyNode}
        queue = collections.deque([node])
        while queue:
            n = queue.popleft()
            for neighbor in n.neighbors:
                if neighbor not in dic:
                    copyNeighbor = Node(neighbor.val, [])
                    dic[neighbor] = copyNeighbor
                    dic[n].neighbors.append(copyNeighbor)
                    queue.append(neighbor)
                else:
                    dic[n].neighbors.append(dic[neighbor])
        return copyNode
                