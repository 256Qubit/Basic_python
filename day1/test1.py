import keyword

# print(keyword.kwlist)
# print(len(keyword.kwlist))
# python语言在定义变量时不需要指定变量的数据类型，python会根据变量值自动实现变量类型确定
num1 = 999
print(f'num1={num1},type(num1)={type(num1)}')
# 单引号，双引号，三引号，嵌套书写非常简单，不需要转义
vs_true = True
print(f'vs_true={vs_true},type(vs_true)={type(vs_true)}')
name1 = '玛利亚'
name2 = "MaLiYa"
name3 = '''MaLiYa'''
names = ['张三', '李四', '王五', '赵六']
print(f'name1={name1},type(name1)={type(name1)}')
# 数列类型：有序，可重复，可扩展
print(f'names={names},type(names)={type(names)}')
# 覆盖后来tuple类型的数据会覆盖掉原来list类型的数据
# 变量名称相同时候内存会发生的状况
# 元祖类型；有序，可重复，不可扩展
names = ('张三', '李四', '王五', '赵六', '朱八')
print(f'names={names},type(names)={type(names)}')
# 集合类型：无序，不可重复，可扩展
# 内部是通过一套算法来实现的
names = {'张三', '李四', '王五', '赵六', '朱八'}
print(f'names={names},type(names)={type(names)}')
# 字典类型：key->value dictionary 键值对
stu_dict = {'stu_id': '1001', 'name': '张三', 'age': '18', 'score': '99'}
print(f'stu_dict={stu_dict},type(stu_dict)={type(stu_dict)}')
student_no = 1
# %06d表示总共有六位不足的用0补齐
print('%06d' % student_no)
price = 9.00
weight = 5.00
money = price * weight
print('%.2f,%.2f,%.2f' % (price, weight, money))
name = '小美'
age = 18
print('%s,%d' % (name, age))
scale = 10.00
print('%.2f%%' % scale)
# 多个数据需要百分号后加上小括号进行数据拼接
print('%.2f%%' % (scale,))
