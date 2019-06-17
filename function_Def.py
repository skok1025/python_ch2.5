
def dummy():
    pass

def my_function():
    print('Hello World')

def times(a,b):
    return a*b

dummy()
my_function()
times(10,20)

# 함수도 객체다
print(dummy,type(dummy))
f = my_function()

print(f,my_function)

# 여러 return 값
def func():
    return 10,'hello',[1,2,3];

n, s, l = func()
print(n,s,l)




