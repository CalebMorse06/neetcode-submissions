class Solution:
    def isValid(self, s: str) -> bool:
        par_map ={')':'(', '}':'{',']':'['}
        stack_pop = []

        for i in s:
            
            if i in par_map:
                if not stack_pop:
                    return False 
                temp = stack_pop.pop()
                if par_map[i]  == temp:
                    continue
                else:
                    return False
            else:
                stack_pop.append(i)
        if not stack_pop:
            return True
        else:
            return False 