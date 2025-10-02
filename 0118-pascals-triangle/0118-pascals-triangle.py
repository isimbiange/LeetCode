class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        triangle = [[1]]
        for i in range (numRows - 1): #since we already have the one row

            prev = triangle[-1] #starting from the first row

            new_row = [a+b for a , b in zip ([0] + prev, prev + [0])]# add 0-s on both sides after the first row
             
            triangle.append(new_row)# a name can't have a dot is for attributes

        return triangle
        
        