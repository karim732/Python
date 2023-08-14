def func(key, value, d=None):
    d[key]=value
    print(d)


d={}
func(1,'one',d)
func(2,'two',d)


