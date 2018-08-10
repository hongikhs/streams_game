import random
a = list(range(1,11))
b = list(range(11,20))
c = list(range(20,31))
j = ['*']
d = a + b + b + c + j
#print(d)
random.shuffle(d)
#print(d)
for i in range(20):
    print('[', i+1, sep='', end='')
    input('번째 숫자]')
    print(d[i])
