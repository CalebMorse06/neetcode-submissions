class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = []
        for word in strs:
            length = len(word)
            encoded.append(str(length) + "#" + word)
        return "".join(encoded)




    def decode(self, s: str) -> List[str]:

        result = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j +=1
            
            word_len = int(s[i:j])
            word_start = j+1
            word_end = word_start + word_len
            word = s[word_start:word_end]
            result.append(word)
            i = word_end
        return result 
