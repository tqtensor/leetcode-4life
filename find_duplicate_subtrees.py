from typing import Optional, List
from collections import defaultdict


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
    # preorder traversal serialisation map to node + count

    serialisationCount = defaultdict(int)
    serialisationNode = {}

    def preorder(node):
        if node is None:
            return "#"
        L = preorder(node.left)
        R = preorder(node.right)
        this = ",".join((str(node.val), L, R))
        serialisationCount[this] += 1
        serialisationNode[this] = node
        return this

    preorder(root)
    return [
        serialisationNode[serialisation]
        for serialisation in serialisationCount
        if serialisationCount[serialisation] >= 2
    ]
