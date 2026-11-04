class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for word in strs:
            for i in word:
                res+=i
            res+="λ"

        return res

    def decode(self, s: str) -> List[str]:
        decoded = []
        word = ""
        for i in s:
            if i=='λ':
                decoded.append(word)
                word = ""
            else:
                word+=i

        return decoded


        