# 验证码转换：SbU8 -> sbu8 (忽略大小写)
import secrets
import string


def generate_verification_code(length):
    characters = string.ascii_letters + string.digits
    # join为连接符表示将join中的字符拼接后再与join前的字符拼接随后返回
    code_random = ''.join(secrets.choice(characters) for _ in range(length))
    return code_random


# 示例用法
code = generate_verification_code(4)
print(code)

# charts = string.ascii_letters + string.digits
# Id = ''.join(secrets.choice(charts) for _ in range(11))
# print(Id)

input_code = input(f'请输入验证码：')
# 将验证码全部转为小写或者大写
# code = code.lower()
# input_code = input_code.lower()
# 大写为:upper,小写为lower()

code = code.upper()
input_code = input_code.upper()

if code == input_code:
    print('successful')
else:
    print('defeat')

# print(f 'code={code},input_code={input_code}')
language = "Python|Java|Php|JavaScript|C++|C|Swift|HTML"

a = language.split('|')
# print(a[0])
# print(a[1])
# print(a[2])
# print(a[3])
# print(a[4])
# print(a[5])
# print(a[6])
# print(a[7])
# for i in range(len(a)):
#     # a = a[i]
#     print(a[i])
for word in a:
    print(word)
print(a)

Merge_0 = '|'.join(a)
print(Merge_0)
Merge_1 = '->'.join(a)
print(Merge_1)

a1 = a[2:5:1]
# 列表切片a[star:stop:step]
Merge_2 = '|'.join(a1)
print(Merge_2)

a2 = a[::-1]
# 逆向切片
print(a2)

password = input(f'请输入密码：')
value = password.isdecimal()
# 判断字符串是否由十进制的数字组成
if value:
    print('Congratulation on successful logging in.')
else:
    print('The password only contains pure numbers and no letters.', '\n')
    print('Please check and re_enter.')


Merge_item_0 = 'Hello,Python,Python'
Merge_item_1 = 'Hello,Python,Python'

copy = Merge_item_0.replace('Python', 'China')

Copy = Merge_item_1.replace('Python', 'USA', 1)
print(copy)
print(Copy)


