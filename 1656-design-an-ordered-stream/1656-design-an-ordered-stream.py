class OrderedStream(object):

    def __init__(self, n):
        """
        :type n: int
        """
        self.arr = [None for _ in range(n)]  # Create a list 'arr' of size 'n' initialized with None
        self.ptr = 0  # Initialize a pointer 'ptr' to track the next index to be filled
        self.n = n  # Store the value of 'n' for future reference

    def insert(self, idKey, value):
        """
        :type idKey: int
        :type value: str
        :rtype: List[str]
        """
        self.arr[idKey - 1] = value  # Insert 'value' at index 'idKey - 1' in the 'arr' list
        if (idKey - 1 > self.ptr):  # Check if the inserted index is greater than the pointer
            return []  # If so, return an empty list as there's no contiguous chunk yet

        result = []  # Initialize an empty list to hold the resulting chunk of values
        while (self.ptr < self.n):  # While the pointer is within the bounds of the list
            if (self.arr[self.ptr] is None):  # If the value at 'ptr' is None, break the loop
                break
            result.append(self.arr[self.ptr])  # Append the value at 'ptr' to the result list
            self.ptr += 1  # Move the pointer forward for the next iteration

        return result  # Return the resulting chunk of values



# class OrderedStream(object):

#     def __init__(self, n):
#         self.stream = [None] * (n + 1)  # Initialize a list to hold the stream
#         self.ptr = 1  # Pointer to track the next index to be filled
        
        

#     def insert(self, idKey, value):
#         self.stream[idKey] = value  # Insert the value at the specified idKey
#         result = []
        
#         while self.ptr < len(self.stream) and self.stream[self.ptr] is not None:
#             result.append(self.stream[self.ptr])  # Append the value to the result
#             self.ptr += 1  # Move the pointer forward
        
#         return result
     
        


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)


