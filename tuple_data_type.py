''' single variable containing multiple values is tuple
            tuple is sequence type and tuple is immutable '''



x = 1,
print(x,type(x))       # (1,) tupleclass


y = 3.6
print(y,type(y))     # 3.6 floatclass


t = (3,6,'code',True, 3.69)
print(t.count(0))          # 0
print(t.index(0))      # ValueError: tuple.index(x): x not in tuple