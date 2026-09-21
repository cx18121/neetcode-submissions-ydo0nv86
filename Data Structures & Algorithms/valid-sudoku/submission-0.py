class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in board:
            s = set()
            for box in row:
                if (box != '.'):
                    if box in s:
                        return False
                    s.add(box)
        
        for j in range(9):
            s = set()
            for i in range(9):
                box = board[i][j]
                if box != '.':
                    if box in s:
                        return False
                    s.add(box)
        
        for i in range(0, 7, 3):
            for j in range(0, 7, 3):
                s = set()
                for r in range(3):
                    for c in range(3):
                        box = board[i+r][j+c]
                        if box != '.':
                            if box in s:
                                return False
                            s.add(box)
        return True
                       
            
        