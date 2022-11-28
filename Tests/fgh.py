def f(n):
    parts=[]

    def rec(n,maxi=n,t=[]):
        nonlocal parts
        if n==0:
            parts+=[t]
            return

        for i in range(1,min(n,maxi)+1):
            rec(n-i,i,t+[i])

    rec(n)
    print(parts)

f(4)