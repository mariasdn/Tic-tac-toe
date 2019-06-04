from Board import Board

if __name__ == '__main__':
    print('Hi')
    b = Board()
    print(b)
    while not b.isOver():
        move = int(input('What is your move?  '))
        b.changeTile(move)
        print(b)
    print('GAME OVER! {} IS A WINNER!'.format(b.turn))
