class Solution:
    def merge(self, l: List[List[int]]) -> List[List[int]]:
        l.sort()
        s = [l[0][0], l[0][1]]
        for i in range(1,len(l)):
            if s[-2]<=l[i][0]<=s[-1] and l[i][1]>=s[-1]:
                s.pop()
                s.append(l[i][1])
            elif s[-2]<=l[i][0]<=s[-1] and s[-2]<=l[i][0]<=s[-1]:
                continue
            else:
                s.append(l[i][0])
                s.append(l[i][1])
        ol = []
        while(len(s)!=0):
            r = s.pop()
            le = s.pop()
            ol.append([le,r])
        return sorted(ol)
