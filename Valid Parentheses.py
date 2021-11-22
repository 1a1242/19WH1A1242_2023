class Solution:
    def isValid(self, s: str) -> bool:
        r = []
        for i in range(len(s)):
            if s[i]=='(' or s[i]=='{' or s[i]=="[":
                    r.append(s[i])
            elif len(r)>0 and r[-1]=='(' and s[i]==')':
                    r.pop()
            elif len(r)>0 and r[-1]=='{' and s[i]=='}':
                    r.pop()
            elif len(r)>0 and r[-1]=='[' and s[i]==']':
                    r.pop()
            else:
                return False
        if len(r)==0:
            return True
        return False
