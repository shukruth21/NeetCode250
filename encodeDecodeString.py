class Solution:

    def encode(self, strs: List[str]) -> str:
        s=""
        for st in strs:
            s= s+st+'/'
        return s
        

    def decode(self, s: str) -> List[str]:
        de=[]
        a=""
        for c in s:
            if(c!='/'):
                a+=c
            elif(c=='/'):
                de.append(a)
                a=""
        return de
            
