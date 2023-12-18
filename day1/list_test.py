# print('*')
for i in range(5):
    for j in range(i + 1):
        print('*', end='\t')
    print()

for i in range(0, 5, 1):
    print(f'i={i}', end='\t')
print('\n')

for i in range(5):  # [0,1,2,3,4]
    for j in range(5 - i):  # [5,4,3,2,1]
        print('*', end='\t')
    print('')
print('\n')

count_2 = 5
for i in range(5):
    for j in range(count_2):
        print('*', end='\t')
    count_2 = count_2 - 1
    print(f'count_2={count_2}')
    print('')

print('\n')

count_1 = 5
for i in range(5):
    for j in range(count_1):
        print('*', end='\t')
    count_1 = count_1 - 1
    print('')

print('\n')

count = 1
for i in range(5):
    for j in range(count):
        print('*',end='\t')
    count = count+1
    print('')
count = 4
for i in range(5):
    for j in range(count):
        print('*', end='\t')
    count = count-1
    print('')