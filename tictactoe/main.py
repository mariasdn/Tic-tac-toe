class Board:
    def __init__(self):
        self.data = ['N' for _ in range(9)]
        self.moves = 0
        self.turn = 'X'

    def changeTile(self, tile):
        if self.moves % 2 == 1:
            self.turn = 'O'
        else:
            self.turn = 'X'
        self.data[tile] = self.turn
        self.moves += 1
    
    def isOver(self):
        # Check if 
        combo = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
        for x in combo:
            if self.data[x[0]] is not 'N' and self.data[x[0]]==self.data[x[1]]==self.data[x[2]]:
                return True
        if self.moves >= 9:
            return True
        return False
        
