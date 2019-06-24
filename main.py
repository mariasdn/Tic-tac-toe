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

    option1 = input(
        "Would you like to challenge someone (1) be challenged by someone (2) or play alone/local (3): ")
    if option1 is 1:
        ipaddr = input(
            "Please provide the ip address for the person you want to challenge: ")
