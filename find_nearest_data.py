# There is a family with 10 members of different ages. They are sitting in the order from younger 
# to older [2, 5, 10, 13, 23, 30, 32, 40, 60, 70]. Now given a random age x = 20 between 2 and 70, 
# you need to find index of the member close to the random guess x = 20. The answer is 5th member 
# with age 23. List has to be predefined. Random integer guess x should be taken during running 
# time. 
# Tips: Implement different approaches and compare their time complexities.

input_list = [2, 5, 10, 13, 23, 30, 32, 40, 60, 70]
find = int(input('enter age between 2 and 70 : '))
low, high =0, len(input_list) - 1
while True:
    if find >= input_list[(low + high)//2] and find <= input_list[(low + high)//2 + 1]:
        pos = (low + high)//2  if abs(find - input_list[(low + high)//2]) < abs(find - input_list[(low + high)//2 + 1]) else (low + high)//2 +1
        break
    elif find > input_list[(low + high)//2]:
        low = (low + high)//2
    else:
        high = (low + high)//2
print('{}th number with age {}'.format(pos+1,input_list[pos]))