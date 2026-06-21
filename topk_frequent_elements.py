from collections import Counter
class Solutiion:
    def topKFrequent(sleg, nums:list[int], k:int)->list[int]:
        count_nums = Counter(nums)
        top_elements = [nums for nums , frequency in count_nums.most_common(k)]
        return top_elements


# testing    
# f= Solutiion()
# nums = [1,1,1,2,2,3,4,5,5,5]
# k=2
# elements = f.topKFrequent(nums,k)
# print(elements)
        