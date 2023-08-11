import pandas as pd

inp = pd.read_excel('brics.xlsx')

# creates a new column with rounding values of expectancy column
inp['new_msg'] = inp['expectancy'].apply(lambda x: round(x))

print(inp)


#         country    capital    gdp  literacy  expectancy  population  new_msg
# 0        Brazil   Brasilia   2750     0.944        76.8      210.87       77
# 1        Russia     Moscow   1658     0.997        72.7      143.96       73
# 2         India  New Delhi   3202     0.721        68.8     1367.09       69
# 3         China    Beijing  15270     0.964        76.4     1415.05       76
# 4  South Africa   Pretoria    370     0.943        63.6       57.40       64