class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        k_dict = {} ## element, frequency
        for i in range(len(nums)):
            if nums[i] in k_dict:
                k_dict[nums[i]] += 1 # if it is in dict increment
            else:
                k_dict[nums[i]] = 1
            ## built our dictonary 
            ## want to return
            ordered = sorted(k_dict.items(), key = lambda pair: pair[1], reverse = True)
            k_top = ordered[:k]
            result = []
            for pair in k_top:
                result.append(pair[0])
        return result
            