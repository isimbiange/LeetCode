class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])  # assume the size of the board is not 0

        def capture(r,c):
            
            if(
                r < 0 or c < 0 or 
                r == ROWS or c == COLS or 
                board[r][c]!= "O"
                ): #if rows and columms all less than 0 or have gone above the size of the rows amd colums of the board
           
                return
            board[r][c] = "T"
            capture(r+1,c)
            capture(r-1,c)
            capture(r,c+1)
            capture(r,c-1)

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O" and (r in [0,ROWS -1]or c in [0, COLS -1]):
                    capture(r,c)  #call the capture method and turn thr "O" int 'T"

        for r in range(ROWS):
            for c in range(COLS):
                if (board[r][c] =="O"):# checks if r or c is O 
                    board[r][c] = "X" #then it assigns it to being x

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "T":
                    board[r][c] = "O"

       
        