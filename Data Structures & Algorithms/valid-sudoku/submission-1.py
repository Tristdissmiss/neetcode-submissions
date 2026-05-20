class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool: 
        #representation of rows
        for i in range(9):#row 
            s = set()
            for j in range(9):#col
                #initate board
                item = board[i][j]
                if item in s: 
                    return False 
                elif item != '.':
                    s.add(item)
        
        #representation of cols 
        for i in range(1,9):#row 
            s = set()
            for j in range(1,9):#col
                #initate board
                item = board[j][i]
                if item in s: 
                    return False 
                elif item != '.':
                    s.add(item) 
        
        #tracking the boxes 
        for row in range(0,9,3):
            for col in range(0,9,3):
                s = set()
                for i in range(3):
                    for j in range(3): 
                        if board[row+i][col+j] in s:
                            return False 
                        elif board[row+i][col+j] != ".":
                            s.add(board[row+i][col+j])
        return True