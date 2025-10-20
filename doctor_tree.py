
class DoctorNode:
    def __init__(self, name):
        self.name = name
        self.left = None
        self.right = None


class DoctorTree:
    def __init__(self):
        self.root = None

    def insert(self, parent_name, employee_name, side):

        if self.root is None:
            self.root = DoctorNode(employee_name)
            return True

        def find(node):
            if node is None:
                return False
            if node.name == parent_name:
                if side == "left" and node.left is None:
                    node.left = DoctorNode(employee_name)
                    return True
                elif side == "right" and node.right is None:
                    node.right = DoctorNode(employee_name)
                    return True
                else:
                    return False
            # search both sides
            return find(node.left) or find(node.right)

        return find(self.root)

   
    def preorder(self, node):
        if node is None:
            return []
        result = [node.name]
        result += self.preorder(node.left)
        result += self.preorder(node.right)
        return result



tree = DoctorTree()
tree.root = DoctorNode("Dr. Rubio")
tree.insert("Dr. Rubio", "Dr. Morales", "right")
tree.insert("Dr. Rubio", "Dr. Reno", "left")
tree.insert("Dr. Reno", "Dr. Carson", "right")
tree.insert("Dr. Reno", "Dr. Chase", "left")

print(tree.preorder(tree.root))
