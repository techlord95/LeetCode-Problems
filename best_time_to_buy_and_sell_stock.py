class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        #stock basics cant sell before buying 
        left_ptr, right_ptr = 0 , 1 
        maximum_profit = 0

        while right_ptr < len(prices):
            if prices[right_ptr] > prices[left_ptr]:
                profit = prices[right_ptr] - prices[left_ptr]
                maximum_profit = max(maximum_profit , profit)
            else:
                left_ptr = right_ptr

            right_ptr +=1
            #right_ptr is indented with while as this has to be sold and the movement has to be captured for the next day so it keeps moving with while loop
        return maximum_profit



# what is sliding window approach  