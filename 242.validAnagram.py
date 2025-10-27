class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if(len(s)!=len(t)):return False
        countS, countT={},{}
        for i in range(len(s)):
            countS[s[i]]=1+countS.get(s[i],0)
            countT[t[i]]=1+countT.get(t[i],0)
        return countS==countT



In Python, the .get() method is used to safely retrieve a value from a dictionary.
.get(key,default)
key → the key you want to look up
default → the value to return if the key doesn’t exist in the dictionary
