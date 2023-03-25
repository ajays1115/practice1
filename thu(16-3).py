# find the length of integer without using len function:

# a=int(input("enter the a:"))
# b=str(a)
# r=0
# for i in b:
#     r+=1
# print(r)
#
# def cap(a,b,c):
#     win=3
#     draw=1
#     loss=0
#     i= a*win+b*draw+c*loss
#     print(i)
# cap(3,4,2)

# take a string to print if number means true or false:
# a="98"
# if a.isdecimal():
#     print("integer")
# else:
#     print("not a integer")

# Python3 code to demonstrate
# Check for float string
# using isdigit() + replace()


# b = "45.657"
# print("The original string : " + str(b))
# r= b.replace('.', '').isdigit()
# print("Is string a possible float number ? : " + str(r))

'''s="newsensw"
p=s[0:4]
o=s[4:8]
print(p,o)
z=o[:-2]
x=o[-2:]
print(z,x)
q=z[::-1]
w=x[::-1]
print(q,w)
e=q+w
print(e)
if p == e:
    print("true")
else:
    print("false")'''

# a={"a":"1","b":"2","c":"3"}
# b=a.copy()
# c=a
# print("The original dictionary:",a)
# print("The 1st copy:",b)
# print("The 2nd copy:",c)
# b["a"]=5
# c["a"]=25
# print(a,b)

'''
key_values=int(input("total key:value pairs="))
dict1={}
for i in range(key_values):
    i=input(f"key{i}=")
    dict1[i]=input(f"value{i}=")
print("dict1=",dict1)
def dict_2():
    print("case1:Changes made to one dictionary will be reflected in other dictionary")
    dict2=dict1.copy()
    dict2[input("enter the key in which to change value:" )]=input("enter value to change: ")
    print("dict2-->",dict2)
    print("dict1-->", dict1)

dict_2()
def dict_3():
    print( )
    print("case2:changes made to one dictionary will not be reflected in other")
    dict1[input("enter the key in which to change value:")] = input("enter value to change: ")
    dict3=dict1.copy()
    print("dict3-->",dict3)
    print("dict1-->", dict1)
dict_3()'''



# a=[1,2,3,4]
# b=[1,2,3,4]
# c=set(a+b)
# print(c)
# if len(a)==len(b):
#     for i in range(len(a)):
#         if a[i]!=b[i]:
#             print("false")
#             break
#     else:
#        print("true")



# a={"apple","banna","cherry","snake","cat"}
# b={"pen","rubber","cat","lion","tiger"}
# f=set(a) - set(b)
# o=set(b) - set(a)
# print(f)
# print(o)
#
# x="hello"[0]
# print(x)