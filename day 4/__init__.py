array1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
array2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]

count = 1
for i in range(9):
    for j in range(count):
        print(f'{array1[i]}x{array2[j]}={array1[i] * array2[j]}', end='\t')
    count = count + 1
    print('')
print(f'-----------------------------------------------------------------------')

sum = 1
for i in range(9):
    for j in range(sum):
        print(f'{array2[j]}x{array1[i]}={array1[i] * array2[j]}', end='\t')
    sum = sum + 1
    print('')

print(f'-----------------------------------------------------------------------')
for i in range(1, 10, 1):
    for j in range(1, i + 1, 1):
        print(f'{i}x{j}={i * j}', end='\t')
    print('')

while True:
    choice = input(f'y/n:')
    if choice == 'y' or choice == 'Y':
        print('y')
        break
    if choice == 'done':
        break
    else:
        print('n')
print('program done')

array_1 = [11, 12, 13, 14, 15, 16, 17, 18, 19]
array_2 = [11, 12, 13, 14, 15, 16, 17, 18, 19]

variable_1 = 1
variable_2 = 9

for i in range(9):
    for j in range(variable_1):
        # for k in range(variable):
        print(f'{array_2[j]}x{array_1[i]}={array_1[i] * array_2[j]}', end='\t')
    variable_1 += 1
    print('')

for i in range(1, 6, 1):
    for j in range(6 - i, 0, -1):
        print('*', end='\t')
    print('')

for i in range(1, 10, 1):
    for j in range(10 - i, 0, -1):
        print(f'{array_2[j]}x{array_1[i]}={array_1[i] * array_2[j]}', end='\t')
    print('')
print(f'--------------------------------------------------------------------------------------------------')
for i in range(9):
    for j in range(variable_2):
        # for k in range(variable):
        print(f'{array_2[j]}x{array_1[i]}={array_1[i] * array_2[j]}', end='\t')
    variable_2 = 9-variable_2
    print('')
print(f'--------------------------------------------------------------------------------------------------')
