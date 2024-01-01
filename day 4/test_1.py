for i in range(10):
    if i == 5:
        continue
    print(f'i={i}', end='\t')

print('\n')

for i in range(3):
    PassWord = input('PassWord:')
    if PassWord == '666':
        break
    else:  # else属于if判断
        print('')
else:  # else 属于for循环，在for循环结束后执行，如果for循环中途break跳出循环则不执行
    print('frieze')

# 行 生成数字为[0,1,2,3,4]
for i in range(5):
    for j in range(i + 1):
        print('*', end='\t')
    print()
for i in range(5):
    for j in range(4 - i):
        print('*', end='\t')
    print()

print('\n')

for i in range(5):
    for j in range(5 - i):
        print('*', end='\t')
    print()
for i in range(9):
    for j in range(i + 1):
        print(f'{(j + 1)}x{(i + 1)}={(j + 1) * (i + 1)}', end='\t')
    print()
print()

row = 5
for i in range(1, row, 1):
    for j in range(i):
        print(' ', end='')
    for k in range((row - 1) * 2 - (2 * i - 1)):
        print('*', end='')
    print()
    # 控制空格
# num_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# num_2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# for i in range(9):
#     for j in range(i + 1):
#         print(f'{num_1[i]}x{num_2[j]}={num_1[i]*num_2[j]}', end='\t')
#     print()
