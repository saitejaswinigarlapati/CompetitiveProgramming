'''


*args: The special syntax *args in function definitions is used to pass a variable number of arguments to a function. Python program to illustrate *args for a variable number of arguments:

'''
print("*args ")
def fun(*argv):
    for arg in argv:
        print(arg)

fun('Hello', 'Welcome', 'to', 'GeeksforGeeks')


'''
**kwargs: The special syntax **kwargs in function definitions is used to pass a variable length argument list. We use the name kwargs with the double star **.

'''
print('\n **kwargs' )
def fun(**kwargs):
    for k, val in kwargs.items():
        print("%s == %s" % (k, val))


# Driver code
fun(s1='Geeks', s2='for', s3='Geeks')