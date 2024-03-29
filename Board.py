import json


class Board:
    def __init__(self, str=''):
        if str is '':
            self.data = ['N' for _ in range(9)]
            self.moves = 0
            self.turn = 'X'
        else:
            d = json.loads(str)
            self.data = d['data']
            self.moves = d['moves']
            self.turn = d['turn']

    def __str__(self):
        stringRepr = ' {} | {} | {} \n' \
                     '-----------\n' \
                     ' {} | {} | {} \n' \
                     '-----------\n' \
                     ' {} | {} | {} \n'

        spaces = []
        for i in range(9):
            if self.data[i] is not 'N':
                spaces.append(self.data[i])
            else:
                spaces.append(str(i))

        return stringRepr.format(spaces[0], spaces[1], spaces[2], spaces[3],
                                 spaces[4], spaces[5], spaces[6], spaces[7],
                                 spaces[8])

    def toJSON(self):
        return json.dumps(self.__dict__)

    def changeTile(self, tile):
        """
        Changes the tile given as a parameter.
        Raise exception if the tile that is passed in already has been played on
        Raise expection if the tile is not between 0-8 inclusive
        """
        if not (0 <= tile <= 8):
            raise Exception("Tile passed in is not between 0-8 inclusive")
        if self.moves % 2 == 1:
            self.turn = 'O'
        else:
            self.turn = 'X'
        if self.data[tile] is not 'N':
            raise Exception("Changing tile would cause overwrite of past turn")
        self.data[tile] = self.turn
        self.moves += 1

    def isOver(self):
        """
        isOver checks if the game is over.
        the game can be over in 2 situations:
            first one of the players has made 3 in a row
            second all the tiles are filed and the playres cannot go anywhere
        """
        combo = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6],
                 [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
        for x in combo:
            if self.data[x[0]] is not 'N' and self.data[x[0]] == self.data[x[1]] == self.data[x[2]]:
                return True
        if self.moves >= 9:
            return True
        return False
