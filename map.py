import pandas as pd

inp = pd.read_excel('brics.xlsx')
# Dictionary to find if condition
messages ={'Brazil':'B', 'Russia':'R', 'India':'I', 'South Africa':'S', 'China':'C'}
# if condition true then value of respective key(column_row) is added to new(msg) column 
inp['msg'] = inp['country'].map(messages)

print(inp)