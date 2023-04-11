import random, sys

class game:
    def __init__(self):
        self.board = ["-","-","-","-","-","-","-","-","-"]
        self.turn = "first"
        self.n = 0

    def print_board(self):
        temp = []
        temp.append([self.board[0],self.board[1],self.board[2]])
        temp.append([self.board[3],self.board[4],self.board[5]])
        temp.append([self.board[6],self.board[7],self.board[8]])
        print("#################")
        if self.turn == "first":
            print("先手の手番です")
        else:
            print("後手の手番です")
        for j in range(3):
            print("\t".join(temp[j]))
        print("#################")

    def is_end(self):
        for i in range(3):
            if (self.board[i] == self.board[i+3]) and (self.board[i] == self.board[i+6]) and (self.board[i] != "-"):
                return True
            if (self.board[3*i] == self.board[3*i+1]) and (self.board[3*i] == self.board[3*i+2]) and (self.board[3*i] != "-"):
                return True
        if (self.board[0] == self.board[4]) and (self.board[0] == self.board[8]) and (self.board[0] != "-"):
            return True
        if (self.board[2] == self.board[4]) and (self.board[2] == self.board[6]) and (self.board[2] != "-"):
            return True
        elif self.n == 9:
            return True
        return False

    def winner(self):
        for i in range(3):
            if (self.board[i] == self.board[i+3]) and (self.board[i] == self.board[i+6]) and (self.board[i] == "o"):
                return "先手勝ち"
            if (self.board[i] == self.board[i+3]) and (self.board[i] == self.board[i+6]) and (self.board[i] == "x"):
                return "後手勝ち"  
            if (self.board[3*i] == self.board[3*i+1]) and (self.board[3*i] == self.board[3*i+2]) and (self.board[3*i] == "o"):
                return "先手勝ち"
            if (self.board[3*i] == self.board[3*i+1]) and (self.board[3*i] == self.board[3*i+2]) and (self.board[3*i] == "x"):
                return "後手勝ち"
        if (self.board[0] == self.board[4]) and (self.board[0] == self.board[8]) and (self.board[0] == "o"):
            return "先手勝ち"
        if (self.board[0] == self.board[4]) and (self.board[0] == self.board[8]) and (self.board[0] == "x"):
            return "後手勝ち"
        if (self.board[2] == self.board[4]) and (self.board[2] == self.board[6]) and (self.board[2] == "o"):
            return "先手勝ち"
        if (self.board[2] == self.board[4]) and (self.board[2] == self.board[6]) and (self.board[2] == "x"):
            return "後手勝ち"
        elif self.n == 9:
            return "引き分け"
        return "続く"
    
    def move(self, number):
        if self.turn == "first":
            self.board[number] = "o"
            self.turn = "second"
        elif self.turn == "second":
            self.board[number] = "x"
            self.turn = "first"
        self.n += 1
        return True
        
    def randmove(self):
        number = random.randrange(0, 9)
        while self.board[number] != "-":
            number = random.randrange(0,9)
        return number

    def is_possible(self,number):
        if number < 0 or number > 8:
            return "Rangeover"
        if self.board[number] != "-":
            return False
        return True
    
    def start(self):
        b = random.randrange(0, 9)
        if b % 2 == 0:
            for i in range(9):
                if i % 2 == 0:
                    print("入力してください")
                    number = int(input())
                    while self.is_possible(number) != True:
                        print("その値は無効です。別の値を入力してください")
                        number = int(input())
                    self.move(number)
                    if self.is_end() == True:
                        self.print_board()
                        print(self.winner())
                        sys.exit()
                else:
                    self.move(self.randmove())
                    self.print_board()
                    if self.is_end() == True:
                        self.print_board()
                        print(self.winner())
                        sys.exit()

        else:
            for i in range(9):
                if i % 2 == 0:
                    self.move(self.randmove())
                    self.print_board()
                    if self.is_end() == True:
                        self.print_board()
                        print(self.winner())
                        sys.exit()
                else:
                    print("入力してください")
                    number = int(input())

                    while self.is_possible(number) != True:
                        print("その値は無効です。別の値を入力してください")
                        number = int(input())
                    self.move(number)    
                    if self.is_end() == True:
                        self.print_board()
                        print(self.winner())
                        sys.exit()
        print(self.winner())

A = game()
A.start()