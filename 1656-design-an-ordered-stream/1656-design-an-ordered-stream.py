class OrderedStream(object):

    def __init__(self, n):
        self.stream = [None] * (n + 1)  # Initialize a list to hold the stream
        self.ptr = 1  # Pointer to track the next index to be filled
        
        

    def insert(self, idKey, value):
        self.stream[idKey] = value  # Insert the value at the specified idKey
        result = []
        
        while self.ptr < len(self.stream) and self.stream[self.ptr] is not None:
            result.append(self.stream[self.ptr])  # Append the value to the result
            self.ptr += 1  # Move the pointer forward
        
        return result
     
        


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)


