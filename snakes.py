import random

class Board:
    def __init__(self):
        self.snakes = {16: 6, 47: 26, 49: 11, 56: 53, 62: 19, 64: 60, 87: 24, 93: 73, 95: 75, 98: 78}
        self.ladders = {1: 38, 4: 14, 9: 31, 21: 42, 28: 84, 36: 44, 51: 67, 71: 91, 80: 100}

    def check_snake_or_ladder(self, position):
        if position in self.snakes:
            print("Oh no! Bitten by a snake!")
            return self.snakes[position]
        elif position in self.ladders:
            print("Yay! Climbed a ladder!")
            return self.ladders[position]
        return position

class Player:
    def __init__(self, name):
        self.name = name
        self.position = 0

    def roll_dice(self):
        return random.randint(1, 6)

    def move(self, board):
        dice = self.roll_dice()
        print(self.name + " rolled a " + str(dice))
        self.position += dice
        self.position = board.check_snake_or_ladder(self.position)
        if self.position > 100:
            self.position = 100
        print(self.name + " is now on position " + str(self.position))

class Game:
    def __init__(self):
        self.board = Board()
        self.players = []

    def add_player(self, player):
        self.players.append(player)

    def play(self):
        while True:
            for player in self.players:
                input(player.name + ", press Enter to roll the dice")
                player.move(self.board)
                if player.position == 100:
                    print("Congratulations " + player.name + "! You have won the game!")
                    return


game = Game()
player1 = Player(input("Enter the name of Player 1: "))
player2 = Player(input("Enter the name of Player 2: "))
game.add_player(player1)
game.add_player(player2)

game.play()
