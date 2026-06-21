class TimeMap:
    
    # the initializer dunder method storing in a dictionary 
    def __init__(self) :
        self.keyStore = {} 
        
    def set(self , key:str , value:str , timestamp :int)-> None:
        if key not in self.keyStore:
            self.keyStore[key] = []  #creating empty list if key does not exist 
        self.keyStore[key].append([value , timestamp]) # values stored in increasing timestamp order as timestamps are 
                                                       # guaranateed to be increasing
        
    def get(self , key:str , timestamp:int) -> str:
        # if no valid timestamp exist we store result in empty string
        result , value = "" , self.keyStore.get(key,[]) # in value here we get the list for the key if the key does not exist return empty list
        
        #binary search 
        left , right = 0 , len(value) - 1 
        
        # the latest timestamp <= given timestamp -> arr would already be sorted acc to  the timestamp no need to sort here 
        while left <=right:
            mid_val = (left+right) // 2 
            
            #current timestamp <= target timestamp
            if value[mid_val][1] <= timestamp:
                result = value[mid_val][0]
                
                left = mid_val + 1 
            else :
                right = mid_val - 1 
        return result 
    
# Time complexity 

# set()
# Append operation → O(1)

# get()
# Binary search → O(log n)

# Space Complexity
# O(n) overall storage