from timeit import timeit

def normal_imp():
    return [i for i in (0, 1, 2, 3, 4,5)]

def optimised_imp():
    return [ 0,1,2,3,4,5]

normal_time = timeit(stmt=normal_imp)
optimised_time = timeit(stmt=optimised_imp)

print(f'normal_imp: {round(normal_time, 4)}s')
print(f'optimised_imp: {round(optimised_time,4)}s')