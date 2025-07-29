# Write a python code to implement a function to flatten a nested list

def flatten(ls):
    f_ls=[]
    for i in ls:
        if isinstance(i,list):
            f_ls.extend(flatten(i))
        else:
            f_ls.append(i)
    return f_ls

l=[1,[2,[3,4],5],6]
print(f"Flatten list : {flatten(l)}")