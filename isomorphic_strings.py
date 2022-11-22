'''
205. Isomorphic Strings
Easy
5.4K
1K
Companies
Given two strings s and t, determine if they are isomorphic.

Two strings s and t are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.

 

Example 1:

Input: s = "egg", t = "add"
Output: true
Example 2:

Input: s = "foo", t = "bar"
Output: false
Example 3:

Input: s = "paper", t = "title"
Output: true
 

Constraints:

1 <= s.length <= 5 * 104
t.length == s.length
s and t consist of any valid ascii character.
'''

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        dict_s={}
        dict_t={}
        check_t=[]
        check_s=[]
        counter=0
        for i in range(len(s)):
            if s[i] not in dict_s:
                counter+=1
                dict_s[s[i]]=counter
            check_s.append(dict_s[s[i]])

        counter=0
        for i in range(len(t)):
            if t[i] not in dict_t:
                counter+=1
                dict_t[t[i]]=counter
            check_t.append(dict_t[t[i]])

        if len(check_s)==len(check_t):
            for i in range(len(check_t)):
                if check_t[i]!=check_s[i]:
                    return False
            return True
        else:
            return False

def test_cases(sol):
    s,t="egg","add"
    assert(sol.isIsomorphic(s,t))==True , "invalid value"
    s,t="foo","bar"
    assert(sol.isIsomorphic(s,t))==False , "invalid value"
    s,t="paper","title"
    assert(sol.isIsomorphic(s,t))==True , "invalid value"
    

if __name__=="__main__":
    sol=Solution()
    test_cases(sol)
    print("Test cases pass")     