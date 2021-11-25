def prevSmaller(self, a):
        n = len(a)
        s = [n-1]
        o = [-1]*n
        for i in range(n-2,-1,-1):
            if a[i]<a[s[-1]]:
                o[s[-1]]=a[i]
                s.pop()
            s.append(i)
        return o
