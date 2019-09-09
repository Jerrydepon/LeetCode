# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# serialize: use deque to append result 
# mind the use of ([root])

# deserialize: 
# split first to convert number to string    
# use deque to traverse through tree
# use idx to point to element in the list
import collections
class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return ''
        queue = collections.deque([root])
        res = []
        while queue:
            node = queue.popleft()
            if node:
                queue.append(node.left)
                queue.append(node.right)
                res.append(str(node.val))
            else:
                res.append("#")
        return ','.join(res)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None
        data = data.split(',')
        root = TreeNode(int(data[0]))
        queue = collections.deque([root])
        idx = 1
        while queue:
            node = queue.popleft()
            if data[idx] != '#':
                node.left = TreeNode(int(data[idx]))
                queue.append(node.left)
            idx += 1
            if data[idx] != '#':
                node.right = TreeNode(int(data[idx]))
                queue.append(node.right)
            idx += 1    
        return root
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))