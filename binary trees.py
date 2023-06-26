class BTNode:
    def __init__(self, data) -> None:
        self.left = None
        self.data = data
        self.right = None

class BTree:
    def __init__(self) -> None:
        self.inorder_arr = []
        self.preorder_arr = []
        self.postorder_arr = []
        self.levelorder_arr = []
        self.levelorder_q = []
 
    def create_node(self, data):
        node = BTNode(data)
        return node

    def insert_node(self, node, data):
        if node is None:
            return self.create_node(data)
        elif data < node.data:
            node.left = self.insert_node(node.left, data)
        else:
            node.right = self.insert_node(node.right, data)

        return node
    
    def inorder(self, node):
        if node is None:
            return
        
        self.inorder(node.left)
        self.inorder_arr.append(node.data)
        self.inorder(node.right)

        return self.inorder_arr
    
    def preorder(self, node):
        if node is None:
            return
        
        self.preorder_arr.append(node.data)
        self.preorder(node.left)
        self.preorder(node.right)

        return self.preorder_arr
        
    def postorder(self, node):
        if node is None:
            return
        
        self.postorder(node.left)
        self.postorder(node.right)
        self.postorder_arr.append(node.data)

        return self.postorder_arr
    
    def levelorder(self, node):
        self.levelorder_q.append(node)

        while len(self.levelorder_q) != 0:
            root = self.levelorder_q.pop(0)
            self.levelorder_arr.append(root.data)
            
            if root.left:
                self.levelorder_q.append(root.left)
            if root.right:
                self.levelorder_q.append(root.right)

        return self.levelorder_arr

    def isBST(self, node):
        validate = self.inorder(node)

        if all(validate[i] <= validate[i+1] for i in range(len(validate) - 1)):
            return True
        return False


    def height(self, node):
        if node is None:
            return -1
        
        return max(self.height(node.left), self.height(node.right)) + 1

    
nodes = [2, 10, 7, 15, 16, 12, 20, 30, 6, 8]
tree = BTree()
root = tree.create_node(5)
for i in nodes:
    tree.insert_node(root, i)
