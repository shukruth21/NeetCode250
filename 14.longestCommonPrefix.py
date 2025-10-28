
#BRUTEFORCE SOLUTION: start from first word compare each letter and update answer
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans=strs[0]
        for i in range (1,len(strs)):
            temp=""
            it=strs[i]
            l=min(len(it),len(ans))
            for j in range(l):
                if(it[j]==ans[j]):
                    temp+=ans[j]
                else:
                    break
            ans=temp
        return ans

  #for better solution i need to learn trie
