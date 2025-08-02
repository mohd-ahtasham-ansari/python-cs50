"""
name = input("whats your name?  ")
print("hello ,MR")
print(name)

the output of both print fxn is in diffrent line so

OR 
to get the output in same line we use END argument of the print function ,
which is by default is \n , we do it end=""
"""

name = input("whats your name?  ")
print("hello, ", end="")
print(name)

"""
there is another argument of print fxn that is sep=" ", 
we can override it too
"""
print("Hello,",name ,sep="......")