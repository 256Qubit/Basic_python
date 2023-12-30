def fact(n):
    if n == 0:
        return 1
    else:
        return n + fact(n - 1)


numbers = eval(input('请输入整数：'))
print(fact(numbers))

i = 1

Sum = 0

while i <= 100:
    Sum += i
    i += 1

print(f'Sum={Sum}')

r = range(1, 11, 2)

for i in range(1, 11, 2):
    print(i, end='\t')

print('\n')
i = 1

while i < 10:
    i = i + 1
    print(i, end='\t')

print('\n')

summer = 0
for i in range(0, 100, 1):
    summer += i

print(f'summer={summer}')

count = 0
# range(10)表示从0开始循环10次等同于range(0,9,1)
for i in range(0, 10, 1):
    for j in range(0, 10, 1):
        count += 1

print(f'count={count}')

count_1 = 0

for i in range(1, 2, 1):
    for j in range(1, 366, 1):
        count_1 += 1
        # print(f'地球完成了第{j}次自转')
    # print(f'地球完成了第{i}次公转')

print(f'count_1={count_1}')

for i in range(1, 5, 1):
    for j in range(1, 5, 1):
        print('*', end='\t')  # 内层控制了列
    print('*')  # 外层控制了行
# count_2 = 1

