from Board import Board

if __name__ == '__main__':
    # 1. Ask user for input (ipaddr) to connect too or 2. if they are expecting a game or 3. play alone
    # 1.
    # attempt to connect to that server
    # if failure inform user and crash
    # else play the game
    # 2.
    # display ipaddr
    # wait until a conntection is requested
    # play game
    # 3. Play game

    b = Board()
    print(b)
    while not b.isOver():
        move = int(input('What is your move?  '))
        b.changeTile(move)
        print(b)
    print('GAME OVER! {} IS A WINNER!'.format(b.turn))
