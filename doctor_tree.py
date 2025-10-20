
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

design_memo = """
A tree is appropriate for the doctor’s structure because it shows relationships clearly. It’s organized and structured like a hospital. Using a binary tree makes it easy to set a clear chain of command, where each doctor can have two subordinates. It’s simple to add, view, and see who reports to whom. It also fits real-life systems that have leaders and multiple levels of management.

Software may use different tree traversals depending on what needs to be done. These methods let engineers process data in a specific and logical way. Preorder is useful when you want to handle the boss first and then the team. Inorder is good when engineers need a sorted order, like names. Postorder helps when dealing with the smaller parts before the main ones, like deleting or finishing lower tasks before higher ones.

Heaps help simulate real-time systems like emergency rooms because they automatically keep the most important or urgent items at the top. When a new patient comes in, the heap reorganizes itself quickly without sorting everything again, so the system always knows which patient needs attention first. This keeps things fast and efficient.
""" 
