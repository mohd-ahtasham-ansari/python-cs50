#ask user name
#name= input("what is your name?  ")

#remove whitespace from str
#name = name.strip()
#capitalize user name initials
#name=name.title()
# OR we can chain them togethr

#name= name.strip().title()
"""
or we can do both
1.take input 
2.and perform fuxn on string in one line 
"""

name=input("What's your name?  ").strip().title()

#say hello to user
"""
this is a multi line comment
"""


print("hello,", name)

#we can do this in another way by usin f and{} 

print(f"Hello ,{name}")