is_failed=True
i=1
while is_failed and i<=100:
    print(i)
    i+=1
print('loop ended')

is_failed=True
i=1
while is_failed:
    print(f'try{i}')
    i+=1
    if i>100:
        break

is_failed=True
i=1
while is_failed:
    if i%2!=0:
        i+=1
        continue
    print(i)
    i+=1
    if i>100:
        break

i=0
while i<=10:
    print(i)
    i+=1

i=0
while i<=10:
    x=0
    while x<i:
        print('rakshith' , end='-')
        x+=1
    print('')
    i+=1

pin='123'
trial=1
while trial<=3:
    input_pin=input(f'trial-{trial}  pin>> ')
    trial+=1
    if input_pin==pin:
        print('correct')
        break
    else:
        print('incorrect')