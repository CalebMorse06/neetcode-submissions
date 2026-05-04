class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        word = ''
        for i in range(len(digits)):
            temp = str(digits[i])
            word = word + temp
        word = int(word)
        word = word + 1
        word = str(word)
        result = list(word)
        return result
