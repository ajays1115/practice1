
# pseudocode
'''setp 1: create a function and function name as to()
step 2: declare a user input to given the string value
step 3: print the string
step 4: create an empty list as d
step 5: using for loop access all letter in a string
step 6: using built-in-function convert the given string into ASCII value
step 7: print the ascii value of given string that append in in list.'''


def tooo():
    a=input("str(" ")")
    print("original string",a)
    d=[]
    for i in a:
        d.extend(ord(num)for num in i)
    print("ASCII for given string:"+str(d))
tooo()