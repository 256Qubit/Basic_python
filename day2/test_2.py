import random

num = random.randint(0, 2)

string = ['石头', '剪刀', '布']
string_1 = ['电脑', '您']

print(f'num={string[num]}')

strategy = int(input('请输入一个0~2的整数：'))
count = 0

if 0 <= strategy <= 2:
    for i in range(5):
        if strategy == 0 and num == 1:
            print(f'{string_1[0]}出', string[strategy])
            print(f'{string_1[1]}出', string[num])
            print(f'{string_1[1]}赢了')
        elif strategy == 1 and num == 2:
            print(f'{string_1[0]}出', string[strategy])
            print(f'{string_1[1]}出', string[num])
            print(f'{string_1[1]}赢了')
        elif strategy == 2 and num == 0:
            print(f'{string_1[0]}出', string[strategy])
            print(f'{string_1[1]}出', string[num])
            print(f'{string_1[1]}赢了')
        elif strategy == 0 and num == 2:
            print(f'{string_1[0]}出', string[strategy])
            print(f'{string_1[1]}出', string[num])
            print(f'{string_1[0]}赢了')
        elif strategy == 1 and num == 0:
            print(f'{string_1[0]}出', string[strategy])
            print(f'{string_1[1]}出', string[num])
            print(f'{string_1[0]}赢了')
        elif strategy == 2 and num == 1:
            print(f'{string_1[0]}出', string[strategy])
            print(f'{string_1[1]}出', string[num])
            print(f'{string_1[0]}赢了')
        elif strategy == num:
            print(f'{string_1[0]}出', string[strategy])
            print(f'{string_1[1]}出', string[num])
            print(f'平局！')
    else:
        print(f'输入不合法！')


i = 1
while i <= 100:
    if i % 2 == 0:
        print(i, end='\t')
    i += 1


def fact(n):
    if n == 0:
        return 1
    else:
        return n + fact(n - 1)


num = eval(input('输入一个整数'))
print(fact(num))

