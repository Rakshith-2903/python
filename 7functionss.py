def greet():
    print('hello')
greet()

def marriage(boy,girl):
    print(f'boy is {boy}')
    print(f'girl is {girl}')
    print(f' {boy} married {girl}')
marriage('rak', 'gan')

def tables(num):
    for i in range(1,11):
        print(f'{num}*{i}={num*i}')
tables(5)

def fun(num):
    return int(str(num)*5)
a=1000000
b=fun(1)
print(a+b)

def add(*num):
    return sum(num)
print(add(1, 2, 3, 4, 5))

def student_info(**details):
    print(details)
    for key , values in details.items():
        print(f'{key} : {values}')
student_info(name='rakshith', age=20, roll_no=123, branch='cse')

def factorial(n):
    if n==1:
        return 1
    return n*factorial(n-1)
print(factorial(5))

def calculate(a,b):
    def add():
        return a+b
    def sub():
        return a-b
    def mul():
        return a*b
    def div():
        return a/b
    print(f'addition is {add()}')
    print(f'subtraction is {sub()}')
    print(f'multiplication is {mul()}')
    print(f'division is {div()}')
calculate(10,5)