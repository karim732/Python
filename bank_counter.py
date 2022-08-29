# There is a counter in a bank after lunch time where people with following tokens are standing in a queue [20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]. Suddenly 3 more new counters are opened and the current one is closed. So, people at the back of original counter got out easily and start rushing towards other counters. Now they form three new lines in the order: new counter 1 [30, 27, 24, 21], new counter 2 [29, 26, 23, 20], new counter 3 [28, 25, 22]. The number of new counters may vary. If number of new counters is 2, two counters will have tokens then in the order: new counter 1 [30, 28, 26, 24, 22, 20], new counter 2 [29, 27, 25, 23, 21]. So, you need to get the number of new counters during execution time.

# Tips: You need to find the suitable data structure for this problem. That data structure can be implemented from scratch or using built-in functions. Try implementing both version and compare their memory and running time.


input_queue = [20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
no_counters = int(input('Number of new counters : '))
result_lines = [[] for _ in range(no_counters)]
for i in range(len(input_queue)-1, -1, -no_counters):
    for j in range(no_counters):
        if i-j >= 0: # To avoid circulating list
            result_lines[j].append(input_queue[i-j])
        else:
            break
print(result_lines)