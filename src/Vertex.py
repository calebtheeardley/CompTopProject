class Vertex:
    def __init__(self, id: str, label: str, type: str):
        self.id = id
        self.label = label
        self.type = type

        width: int = 6938
        cell: int = int(self.label)
        y:int = (int((cell - 1) / width + 1))
        x:int = int(cell - (y - 1) * width)
        y = -y

        # X: float = (width - y) * 1 + 
        self.pos = (x,y)