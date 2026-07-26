for i in range (1,10):
    print(i)

bag=['red','green','blue','yellow']
for ball in bag:
    print(ball)

name='Rakshith'
for index , letter in enumerate(name):
    print(letter*(index+1))

total=0
for i in range(1,11):
    total+=i
print(total)

vowels='aeiou'
a='this is rakshith'
count=0
for letter in a:
    if letter in vowels:
        count+=1
print(count)

for i in range (1,11):
    print(f'2*{i}={2*i}')

for i in range (2,11):
    for j in range (1,11):
        print(f'{i}*{j}={i*j}')