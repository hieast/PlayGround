class Node:
    def __init__(self, board, score0, score1 ,player, path):
        self.board = board
        self.player = player
        self.score1 = score1
        self.score0 = score0
        self.path = path
        if len(board) != 0:
            if player:
                self.leftChild = Node(board[1:], score0, score1 + board[0], not player, path + "l")
                self.rightChild = Node(board[:-1], score0, score1 + board[-1], not player, path + "r")
            else:
                self.leftChild = Node(board[1:], score0 + board[0], score1, not player, path + "l")
                self.rightChild = Node(board[:-1], score0 + board[-1], score1, not player, path + "r")


    def __str__(self):
        res = ""
        res += "(" + str(self.score0) + ", " + str(self.score1) + ")\n"
        res += self.path
        if len(self.board) != 0:
            res += "--" * len(self.path) + str(self.leftChild) + "\n" + "--" * len(self.path)  + str(self.rightChild)
        return res

    def minimax(self):
        if len(self.board) == 0:
            return (self.score0, self.score1, self.path)
        left = self.leftChild.minimax()
        right = self.rightChild.minimax()

        if self.player:
            return left if left[0] < right[0] else right
        else:
            return right if left[0] < right[0] else left



#def pick_a_number(board):





#pick_a_number([1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3])

tree = Node([12, 9, 7, 3, 4, 7, 4, 7, 3, 16, 4, 8, 12, 1, 2, 7, 11, 6, 3, 9, 7, 1], 0, 0 ,False, "")
#print tree
print tree.minimax()