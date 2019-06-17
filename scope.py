def func1(a):
    return a+x

def func2(a):
    x=2
    return a+x

def func3(a):
    global g
    g= 3
    return a+g

x = 1

# (L)GB
print(func1(10))

# L(G)B
print(func2(10))
print(func3(10))
print(g)


# LG(B)
print(dir('__builtins__'))
