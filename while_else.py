#  Executing else block after while loop

i = 0 
while i<2:
    print(i)
    i +=1
    # break
    # if break is executed else block is not executed
else:
    print(i)
    print('Success')