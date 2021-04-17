class TicTacToe:

    def __init__(self):
        self.player1 = " "
        self.player2 = " "
        self.board = {x: str(x) for x in range(1, 10)}
        self.count = 0

    def start_game(self):
        print("Enter your name, Player1: ")
        user1 = input()
        print("Enter your name, Player2: ")
        user2 = input()
        print(f"{user1.upper()} is X")
        print(f"{user2.upper()} is O")
        self.player1 = user1
        self.player2 = user2

    def display_board(self):
        print(f" {self.board[7]} | {self.board[8]} | {self.board[9]}")
        print(f" - + - + - ")
        print(f" {self.board[4]} | {self.board[5]} | {self.board[6]}")
        print(f" - + - + - ")
        print(f" {self.board[1]} | {self.board[2]} | {self.board[3]}")

    def check(self):
        if self.count > 3:
            if self.board[1] == self.board[2] == self.board[3]:
                return True
            elif self.board[4] == self.board[5] == self.board[6]:
                return True
            elif self.board[7] == self.board[8] == self.board[9]:
                return True
            elif self.board[1] == self.board[4] == self.board[7]:
                return True
            elif self.board[2] == self.board[5] == self.board[8]:
                return True
            elif self.board[3] == self.board[6] == self.board[9]:
                return True
            elif self.board[1] == self.board[5] == self.board[9]:
                return True
            elif self.board[3] == self.board[5] == self.board[7]:
                return True
            return False

    def game(self):
        possible_positions_index = list(range(1, 10))
        used_index = []
        while True:
            for char in ["X", "Y"]:
                if len(possible_positions_index) == 0:
                    return "Draw"
                print(f"It is {char} turn to play, where do you want to play")
                position = int(input())
                if position not in possible_positions_index and position not in used_index:
                    raise ValueError(f"Position should be between 1 - 9")
                elif position in used_index:
                    while position in used_index:
                        print(f"The positon {position} has been used already")
                        print("Please enter another position")
                        position = int(input())
                    possible_positions_index.remove(position)
                    used_index.append(position)
                    self.board[position] = char
                    self.display_board()
                    self.count += 1
                else:
                    possible_positions_index.remove(position)
                    used_index.append(position)
                    self.board[position] = char
                    self.display_board()
                    self.count += 1
                    if self.check():
                        if char == "X":
                            return "X"
                        else:
                            return "Y"


d = TicTacToe()
d.start_game()
d.display_board()
result = d.game()
if result == "X":
    print(f"{d.player1.upper()} WINS!!!!")
    print(f"{d.player2.upper()} LOSES!!!")
elif result == "Y":
    print(f"{d.player2.upper()} WINS!!!!")
    print(F"{d.player1.upper()} LOSES")
else:
    print("IT IS A DRAW!!!!" + u"\U0001F91D")

# print(u"\U0001F91D")