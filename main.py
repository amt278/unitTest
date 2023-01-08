import math

def fun(x):
    return 1 / x


def mWloop(x, y):
    return sum(y for _ in range(x))

#mWloop(10, 17)


def length(x):
    print(int(math.floor(math.log10(x)) + 1))
    if math.log10(x) == 0:
        print('1')
    else:
        print(int(math.ceil(math.log10(x))))
    print('--------------------------------------------------')
    
    return int(math.floor(math.log10(x)) + 1)
'''
length(12345)
length(1)
length(12)
length(123)
length(123456789)
'''
