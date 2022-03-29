# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


from collections import deque


class Codec:
    def serialize(self, root: TreeNode) -> str:
        """Encodes a tree to a single string."""
        if not root:
            return ""
        q = deque([(root)])
        data = []
        while q:
            node = q.popleft()
            if node:
                data.append(str(node.val))
                q.append(node.left)
                q.append(node.right)
            else:
                data.append("#")

        return ",".join(data)

    def deserialize(self, data: str) -> TreeNode:
        """Decodes your encoded data to tree."""
        if not data:
            return None
        data = data.split(",")
        q = deque(data)
        root = TreeNode(int(q.popleft()))
        p = deque([root])  # memory non-empty nodes
        while q:
            node = p.popleft()
            left = q.popleft()
            right = q.popleft()
            if left != "#":
                node.left = TreeNode(int(left))
                p.append(node.left)  # add non-empty node
            if right != "#":
                node.right = TreeNode(int(right))
                p.append(node.right)  # add non-empty node

        return root


# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans
