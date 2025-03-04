class ArrayListADT:
    def __init__(self):
        self.data = []
        self.size = 0
                
    def add(self, num):
        # for i in self.data:
            self.data.append(num)
            self.size = self.size_()
            # self.size+=1
            return True
        
    def add_at(self, index, c):  
        index = int(index)  
        self.data.append(c)  
        self.size = self.size_()
        for i in range(len(self.data) - 2, index - 1, -1):
            self.data[i + 1] = self.data[i]
        
        self.data[index] = c
        self.size = self.size_()
        return True
    
    def add_all_at(self,index,col):
        for i in range(len(col)):
            self.add_at(index + i, col[i])
        return True
    
    def add_all(self,c):
        for i in c:
            self.data.append(i)
        self.size = self.size_()
        return self.data

    def contains(self,o):
        for i in self.data:
            if i == o:
                return True
        return False 

    def index_of(self,o):
        for i in range(len(self.data)):
            if self.data[i] == o:
                return i
        return -1

    def get(self,index):
        # print(self.data)
        l = []
        for i in self.data:
            if i != None:
                l.append(i)
        # print(l,index)
        self.size = len(l)
        self.data = l
        return l[index]
    
    def last_index_of(self,o):
        # print(63636,self.size- 1)
        l = []
        for i in range(len(self.data)):
            if self.data[i] == o:
                l.append(i)
        return l[-1]
    
    def is_empty(self):
        return len(self.data) == 0
    
    def size_(self):
        return len(self.data)
    
    def remove_at(self, index):
        l = []
        a = self.data[index]
        for i in range(len(self.data)):
            if i != index:
                l.append(self.data[i])
        self.data = l
        self.size = self.size_()
        return a            
    
    def remove(self,o):
        a = self.data.index(o)
        self.remove_at(a)
        self.size = self.size_()
        return True

            
    def set(self,index,e):
        a = self.data[index]
        self.data[index] = e
        return a
                
    def trim_to_size(self):
        return self.data


    def clear(self):
        self.data = []
        self.size = 0
    
    def ensure_capacity(self, cap):
        self.add_all_at(len(self.data),[None]*cap)


    def __str__(self):
        return f"{self.data}"

class LuckyBingoBoard:
    def __init__(self,size,board):
        self.size = size
        self.board = board
        self.marks = []
        for i in range(self.size):
            r = []
            for j in range(self.size):
                r.append(False)
            self.marks.append(r)

    def mark_number(self,num):
        for i in range(self.size):
            for j in range(self.size):
                # print(num)
                # print(self.board[i][j],num)
                # print(self.marks[i][j])
                if self.board[i][j] == num:
                    self.marks[i][j] = True
                # print(self.marks[i][j])
        # self.print_board()


    def is_row_complete(self,row):
        for i in range(self.size):
            # print(row,i)
            # print(self.marks[row][i])
            if self.marks[row][i] == False:
                return False
        return True
    
    def is_column_complete(self,col):
        for i in range(self.size):
            # print(col,i)
            if self.marks[i][col] == False:
                return False
        return True
    
    def is_main_diagonal_complete(self):
        for i in range(self.size):
            if self.marks[i][i] == False:
                return False
        return True
    
    def is_anti_diagonal_complete(self):
        for i in range(self.size):
            if self.marks[i][self.size - 1 - i] == False:
                return False
        return True
    
    def is_cross_complete(self):
        for i in range(self.size):
            if self.marks[i][self.size//2] == False and self.marks[self.size//2][i] == False:
                return False
        return True
    
    def check_win(self):
        for i in range(self.size):
            # print(self.is_column_complete(i))
            if self.is_row_complete(i) or self.is_column_complete(i):
                return True
        if self.is_main_diagonal_complete() or self.is_anti_diagonal_complete() or self.is_cross_complete():
            return True
        return False

    def print_board(self):
        print("Board State:")
        for i in range(self.size):
            print(" ".join("X" if self.marks[i][j] else str(self.board[i][j]) for j in range(self.size)))


class Player:
    # l = ["B", "I", "N", "G", "O"]

    def __init__(self,name,board):
        self.name = name
        self.board = board
        self.letters =[]

    def mark_number(self,number):
        # print(number)
        self.board.mark_number(number)



    def has_won(self):
        if self.board.check_win():
            # print("hi")
            # print(self.board.check_win())
            # print(f"{self.name} has won!")
            # self.display_board()
            return True
        return False
        # self.print_result()


    def display_board(self):
        print(f"{self.name}'s Board:")
        self.board.print_board()


class LuckyBingoGame:
    def __init__(self,players,p):
        self.players = players
        self.predefined_numbers = p
        self.current_index = 0

    def play(self):
        for number in self.predefined_numbers:
            # print(number)
            for player in self.players:
                # print(self.predefined_numbers[self.current_index])
                print(f"{player.name} calls number: {self.predefined_numbers[self.current_index]}")
                for player in self.players:
                    # print(f"{player.name} calls number: {number}")
                    # print(player.name)
                    player.board.mark_number(self.predefined_numbers[self.current_index])
                    player.display_board() 
                self.current_index+=1

                for player in self.players:
                    if player.has_won():                
                        print(f"{player.name} Wins!")
                        return
                    
