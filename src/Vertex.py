class Vertex:
    def __init__(self, id: str, label: str, type: str, width: int):
        self.id = id
        self.label = label
        self.type = type
        self.unique_id = self.label +"_"+ self.id
        self.weight = None
        
        cell: int = int(self.label)
        y:int = (int((cell - 1) / width + 1))
        x:int = int(cell - (y - 1) * width)
        y = -y

        # X: float = (width - y) * 1 + 
        self.pos = (x,y)

    def __lt__(self, other):
        return (int(self.label) < int(other.label))