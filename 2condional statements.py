a=input('enter gender: ')
# b=int(input('enter age: '))
if a=='female':
    print('ticket is free')
else:
    b=int(input('enter age: '))
    if b<=5:
        print('ticket is free')
    elif b<=12:
        print('you have child discount')
    elif b>60:
        print('you have senior citizen discount')
    else:
        print('you pay full ticket price')