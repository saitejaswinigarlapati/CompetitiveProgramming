def pascalsTrianle(n):
    if n==0:
        return []
    res=[[1]]
    if n==1:
        return res
    for i in range(1,n):
        prevrow=res[i-1]
        row=[1]
        for j in range(1,i):
            row.append(prevrow[j-1] + prevrow[j])
        row.append(1)
        res.append(row)
    return res


def RowinPascalsTriangle(n):
    ans=pascalsTrianle(n)
    return ans[n-1]

n=int(input("Number os pascals triangle : "))
print(pascalsTrianle(n))

s=int(input("Row of Pascals Triangle : "))
print(RowinPascalsTriangle(s))