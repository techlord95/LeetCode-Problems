class Solution:
    def totalFruit(self, fruits: list[int]) -> int:
        left_pointer = 0 
        maximum_fruits = 0
        basket = {}
        
        # create enumerate objects which contains iterative count in tuple
        # fruit here is the type of fruit at each tree
        for right_pointer , fruit in enumerate(fruits):
            basket[fruit] = basket.get(fruit,0) +1 # adding current fruit to the basket or increment the count if it is already present 


            # Shrink the window if there are more than 2 types of fruit
            while len(basket) > 2:
                basket[fruits[left_pointer]] -=1 
                if basket[fruits[left_pointer]] ==0:
                    del basket[fruits[left_pointer]]
                left_pointer +=1

            maximum_fruits = max(maximum_fruits , right_pointer -left_pointer + 1 ) # if shrinking is done update with len of current window

        return maximum_fruits



# left t0 right arrangement of trees [i] 
# collect fruits such that:
# only 2 baskets are there , each can hold single type of fruit , no limits on amount of fruit each basket can hold
# exctly 1 fruit from 1 tree can be picked 
# return max num of fruits you can pick   

# Time and Space O(n)