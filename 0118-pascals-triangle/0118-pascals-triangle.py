class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res=[[1]] #the first row we already have

        for i in range(numRows-1): # iterating starting from our one row
            temp = [0]+res[-1]+[0] #adding 0 on both sides of the row
            row =[] #our new empty row
            for j in range (len(res[-1])+1): #adding the next pointer to the second pointer
                row.append(temp[j]+temp[j+1]) # findind the additional result
            res.append(row)#appending the new result in our empty row
        return res #retun the number of rows we had to go through to much our input
        