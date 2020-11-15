class TreeNode:
    def __init__(self,data):
        self.data = data
        self.children = []
        self.parent = None

    def add_child(self,child):
        child.parent = self
        self.children.append(child)

def build_product_tree():
    root=TreeNode("Electronics")

    laptop=TreeNode("Laptop")
    laptop.add_child(TreeNode("MSI"))
    laptop.add_child(TreeNode("Alienware"))
    laptop.add_child(TreeNode("ROG"))
    
    tv=TreeNode("TV")
    tv.add_child(TreeNode("LG"))
    tv.add_child(TreeNode("Bravia"))
    tv.add_child(TreeNode("Samsung"))

    cellphone=TreeNode("Cellphone")
    cellphone.add_child(TreeNode("ROG Phone"))
    cellphone.add_child(TreeNode("1+"))
    cellphone.add_child(TreeNode("Samsung Z"))

    root.add_child(laptop)
    root.add_child(tv)
    root.add_child(cellphone)
    
    return root


if __name__ == "__main__":
    root=build_product_tree()
    pass