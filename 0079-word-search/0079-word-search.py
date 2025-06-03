class Solution:
    def exist(self,board:[list[str]],word:str):
        ROWS,COLS = len(board),len(board[0]) #len of cols and rows dimensial
        path = set() # variable set to add all the current value to make sure we dont visit them again

        def dfs(r,c,i):#i the current char with in our target word we are looking for
            if i == len(word):
                return True

            if(r < 0 or c < 0 or # out of bounds
            r >= ROWS or c >= COLS or # greater or equal is out of bounds
            word[i]!= board[r][c] or 
            (r,c) in path):
                return False

            path.add((r,c)) # we know we found the character we are looking for we can add it to our path

            res = (dfs(r+1, c, i+1) or # dfs in all four adjacent position
       dfs(r-1, c, i+1) or # I+1 add the character if we have found it
       dfs(r, c+1, i+1) or 
       dfs(r, c-1, i+1))
#if any of them retunr true we have found our word
            path.remove((r,c))
            return res #before returning the result we remove the char we dont need

        for r in range (ROWS): #nested for loop
            for c in range (COLS):#for every single position in our grid run this in all position and run this dfs
                if dfs(r,c,0):
                    return True
        return False



        


        