from Board import Board
from Server import TicTacToeHTTPServer

import requests
import socketserver


def playGame(b):
    print(b)
    while not b.isOver():
        move = int(input('What is your move?  '))
        b.changeTile(move)
        print(b)
    print('GAME OVER! {} IS A WINNER!'.format(b.turn))


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
    print('\n========================\n'
          'WELCOME TO TIC_TAC_TOE!\n \nWhat kind of game would you like to play?\n')
    while (True):
        option = input('[A] Single player\n'
                       '[B] Ask a friend to play with you\n'
                       '[C] Be added to your friend\'s game\n\n')
        if option == 'A':
            b = Board()
            playGame(b)
            break
        if option == 'B':
            ipaddr = input("Please enter your friend's IP address. ")
            b = Board()
            while not b.isOver():
                print(b)
                move = int(input('What is your move?  '))
                try:
                    b.changeTile(move)
                except Exception as e:
                    print(e)
                    continue
                # send request
                response = requests.post(
                    "http://" + ipaddr + ":5500", data=b.toJSON(), timeout=10)
                b = Board(str=response.text)

            break
        if option == 'C':
            # TODO: we are going to ignore this part! For now!
            httpd = socketserver.TCPServer(("", 5500), TicTacToeHTTPServer)
            httpd.serve_forever()
            break
        else:
            print(
                '\nPlease chose one of the following options. (TIP: use capital letters)')
