'''1. Write a function to do binary search over a ordered list'''

l = list(map(int,input('enter a list :').split()))
num = int(input('enter a target number :'))
i = len(l)
for x in range(i):
    for y in range(i-1):
        if l[y]>l[y+1]:
            l[y],l[y+1]=l[y+1],l[y]
print('sorted list :',l)
mini=0
maxi=i-1
if num in l:
    for x in range(i):
        cen = (mini+maxi)//2
        if l[cen] < num : mini = cen+1
        elif l[cen] > num: maxi = cen-1
        else: tar = cen
    print('index of target :',tar)
else:
    x =l[i-1]
    for y in range(i):
        if abs(l[y]-num)<x:
            x= abs(l[y]-num)
            cl_tar=y
    print('index of nearest element is',cl_tar)














