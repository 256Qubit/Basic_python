# /t 水平制表符，类似于四个空格
print('\t')
# /n 换行符
print('\n')
print('a\nb')
# \ 反斜杠 如果要输出\要写\\
print('\\')
print("she say:'hello'")
print('she say:\'hello\'')
# print输出函数默认自动换行
print('hello', end='')  # end=空字符串
print('world')
print('hello', end='\t')
print('world')  # end='\n'默认为换行，其中内容可以指定为其他内容
# print 函数可以跟多个变量
num1 = 10
num2 = 20
print(num1, num2)
print(f'num1={num1},num2={num2}')
# .format() 填充参数
print('num1={0},num2={1}'.format(num1, num2))
print('num1={1},num2={0}'.format(num1, num2))

number1 = '10'
number2 = '20'
# 两个字符串相加就是两个字符串的相拼接
# 网页中的输入框;input类型（都是字符串类型的）
result = number1 + number2
print(f'result={result}')

# int+int 就是数学运算
n1 = int(number1)
n2 = int(number2)
result = n1 + n2
print(f'result={result}')

f1 = 66.66
f2 = 88.88

result = f1 + f2
print(f'result={result}')

# 浮点型转整数型就是丢弃掉小数后部分
# int+float->float 只要有浮点数参与运算其结果就是浮点型
n1 = int(f1)
n2 = int(f2)
result = n1 + n2
print(f'result={result}')

# [input]
# input是python提供的输入函数

name = input('请输入：')
age = input('请输入：')

print('%s\t%s' % (name, age))

# input输入函数返回的是string类型
number5 = int(input('请输入第一个整型数：'))
number6 = int(input('请输入第二个整型树：'))

Sum = number6 + number5
# summer = int(number6)+int(number5)

print(f'Sum={Sum}')

t_shirt = float(input('请输入t_shirt的单价：'))
pants = float(input('请输入pants的单价：'))

t_shirt_count = int(input('请输入t_shirt的件数：'))
pants_count = int(input('请输入pants的件数：'))

value = (t_shirt * t_shirt_count + pants * pants_count)

discount = 0.88
discounts_value = value * discount

print(f'总价为%.1f' % (discounts_value,))

r1 = 10 / 3
print(f'r1={r1}')
r2 = 10 // 3
print(f'r2={r2}')
r3 = 2 ** 4
print(f'r3={r3}')
r4 = 10 % 4
print(f'r4={r4}')

# 复合赋值运算符：一个变量如果在自身的基础上发生改变，那么此时就可以选择使用复合运算符

mun = 10
# mun = mun+1
mun += 1

print(f'mun={mun}')

n = 10
n += 1
print(f'n={n}')

n = 10
n -= 1
print(f'n={n}')

n = 10
n *= 1
print(f'n={n}')

n = 10
n /= 1
print(f'n={n}')

n = 10
n %= 1
print(f'n={n}')
# 逗号表达式 元组解包
n1, n2, n3 = 10, 20, 30
# n1,n2,n3=(10,20,30,40,50)
# 可以定义多个相同类型的变量

print(f'n1={n1},n2={n2},n3={n3}')

t1 = 10
t2 = 20

contrast_result = t1 != t2

print(f'contrast_result={contrast_result},type(contrast_result)={type(contrast_result)}')
# print(contrast_result={contrast_result},type(contrast_result)={type(contrast_result)}')

gender = input('请输入性别')
# gender = input('请输入性别')
age = int(input('请输入年龄：'))
# age = int(input('请输入年龄：'))

# and 并且 特点：全真为真，一假则假

var1 = gender == 'Male' and age >= 18
print(f'var1={var1}')

gender = input('请输入性别')
age = int(input('请输入年龄：'))

# or 并且 特点：一真则真，全假则假

var2 = gender == 'Male' or age >= 18
print(f'var2={var2}')

s1 = 10
s2 = 20

result = s1 == s2
print(f'result={result}')
print(f'result={not result}')

print(f'result={result}')
print(f'result={not result}')

t_shirt = float(input(':'))
pants = float(input(':'))

t_shirt_count = float(input(':'))
pants_count = float(input(':'))

normal_price = t_shirt * t_shirt_count + pants * pants_count
print(f'normal_price={normal_price}')

year_of_birth = int(input(f'Please enter your year of birth:'))
age = 2023 - year_of_birth
# if为一个整体，整体条件如果成立整体就会被执行，如果不成立就都不执行
if age > 18:
    print(f'You age is:'.format(age))
    print(f'You are an adult')
else:
    print(f'You age is:'.format(age))
    print(f'You are not adult')

score = int(input(f'Please enter your score:'))

result_1 = 'A'
result_2 = 'B'
result_3 = 'C'
result_4 = 'D'

if 90 < score <= 100:
    format_string_1 = "You score is {},You Get a [{}]".format(score, result_1)
    print(format_string_1)
elif 80 <= score < 90:
    format_string_2 = "You score is {},You Get a [{}]".format(score, result_2)
    print(format_string_2)
elif 60 <= score < 80:
    format_string_3 = "You score is {},You Get a [{}]".format(score, result_3)
    print(format_string_3)
else:
    format_string_4 = "You score is {},You Get a [{}]".format(score, result_4)
    print(format_string_4)


    def bold_text(text):
        return f"\033[1m{text}\033[0m"


    print('\n')
    print(bold_text("Warm:"))
    print('\t', bold_text("Failed grades"))
# print("\033[1mFailed grades\033[0m")

    # from termcolor import colored print('You score is:'.format(score), 'and You Get a'.format(result_4),
    # colored("Failed grades", 'red', attrs=['bold']))

