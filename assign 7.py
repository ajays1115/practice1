#ques.1
#pseudo code
"""
->assign a list 'x' and create empty list 'xx','yy' and an empty dictinary 'y'
->using for loop we traverse through the index values of the list
->if the index are even they gonno append in the list 'xx' and odd index are append in list 'yy'
->using keyword update we can add lsit'xx' as keys and 'yy' as values into dictinary 'y' in a for loop
->print the new dictionary 'y'
"""
#code
"""x=[1,'a',2,'b',3,'c']
xx=[]
yy=[]
y={}
for i in range(len(x)):
    if(i%2==0):
        xx.append(x[i])
    else:
        yy.append(x[i])
print(xx)
print(yy)
for i in range(len(xx)):
    y.update({xx[i]:yy[i]})
print(y)
"""


#ques.2
#pseudo code
"""
->create an empty dictionary
->using for loop we can get numbers upto a range
->inside the for loop we can multiply the number with '5'
->now we can update both the key (i) and value (x) into 'y'
->now print the dictionary 'y'
"""
#code
"""
y={}
for i in range(1,11):
    x=i*5
    y.update({i:x})
print(y)
"""



#ques.3
#pseudo code
"""
->get the input for how many numbers need to worked in this problem and initialize max=0
->using for loop get the input and check whether it is greater than 'max' or not
->if it is greater then store the value in max and continue the loop
->at the end of the loop we can get the largest number and print it
"""
#code
"""
print("no. of elements to get:")
n=int(input())
max=0
for i in range(n):
    x=int(input())
    if (x>max):
        max=x
print("the largest number is:",max)

"""


#ques.4
"""
#pseudo code
->get the number which we want to find the factorial from the user and initialize fact=1
->using for loop we can multiply the numbers present before the given number
->print the result
"""
#code

"""print("number to get the factorial is :")
n=int(input())
fact=1
for i in range(1,n+1):
    fact=fact*i
print(fact)"""