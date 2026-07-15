class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
  
        address = {}

        for word in strs:
            sig = "".join(sorted(word))
            if sig in address:
                address[sig].append(word)
            else:
                address[sig] = [word]
        return list(address.values())