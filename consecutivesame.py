# Python program to find
# length of the longest
# consecutive 1s in
# binary representation of
# a number.

B_input = [1, 1, 0, 1, 1, 1, 0]
flag, sum = 0, 0
for i in B_input:
    if i == 0:
        if sum >= flag:
            flag = sum
        sum = 0
    else:
        sum = sum + 1
print(flag if flag > sum else sum)

def maxConsecutiveOnes(x):
    count = 0
    while (x != 0):
        x = (x & (x << 1))
        count = count + 1
        print(x)
    return count

print(maxConsecutiveOnes(14))