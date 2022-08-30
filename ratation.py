inp = [9, 11, 14, 19, 25, 29, 3, 5, 6, 7]
inp = [3,3, 4,4, 5, 6, 6, 9, 9, 9, 0, 0, 2, 3, 3]
num=0
'''def check(arr):
    e=-1
    for i in arr:
        if e<=i:
            e=i
        else:
            return False
    return True


while True:
    if check(inp) == True:
        print("number of roatation",num)
        break
    else:
        num=num+1
        inp.append(inp[0])
        inp.pop(0)
        check(inp)'''
e=-1
for i in inp:
    if i>=e:
        e=i
        num=num+1
    else:
        break
if num <= len(inp)//2:
    print(num)
else:
    print(len(inp)-num)



