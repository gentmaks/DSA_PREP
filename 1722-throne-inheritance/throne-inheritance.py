from enum import Enum, auto

class Status(Enum):
    alive = auto()
    dead = auto()

class InheritanceNode:
    def __init__(self, name: str, status: Status):
        self.name = name
        self.status = status
        self.children = []

class ThroneInheritance:

    def __init__(self, kingName: str):
        self.king_name = kingName
        self.mapping = {}
        self.mapping[self.king_name] = InheritanceNode(self.king_name, Status.alive)

    def birth(self, parentName: str, childName: str) -> None:
        parent_node = self.mapping[parentName]
        child_node = InheritanceNode(childName, Status.alive)
        parent_node.children.append(child_node)
        self.mapping[childName] = child_node

    def death(self, name: str) -> None:
        self.mapping[name].status = Status.dead

    def getInheritanceOrder(self) -> List[str]:
        king = self.mapping[self.king_name]
        res = []
        def dfs(node):
            if not node:
                return
            if node.status == Status.alive:
                res.append(node.name)
            for child in node.children:
                dfs(child)
        dfs(king)
        return res

# Your ThroneInheritance object will be instantiated and called as such:
# obj = ThroneInheritance(kingName)
# obj.birth(parentName,childName)
# obj.death(name)
# param_3 = obj.getInheritanceOrder()