
def fact(n):
    if n == 0:
        return 1
    else:
        return n + fact(n-1)


numbers = eval(input('请输入整数'))
print(fact(numbers))

i = 1

Sum = 0

while i <= 100:
    Sum += i
    i += 1

print(f'Sum={Sum}')