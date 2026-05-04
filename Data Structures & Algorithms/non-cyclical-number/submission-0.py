class Solution:
         
    def numSqr(self, n):
        total = 0
        n = str(n)
        for digit in n:
            digit = int(digit)
            total = total + digit **2
        return total

    def isHappy(self, n: int) -> bool:
        seen = set() 

        while n not in seen and n != 1:
            seen.add(n)
            n = self.numSqr(n)
        if n ==1:
            return True
        else:
            return False 


   

    

    