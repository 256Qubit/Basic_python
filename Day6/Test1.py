name = ["a", "b", "v", "d", "f", "o", "o"]

name.remove("o")
print(name)

# pop如果不传递坐标，默认删除最后一个
name.pop(0)
print(name)

# 清楚列表，清楚后列表仍旧存在s
name.clear()
print(name)

name.extend(["李一", "李二", "李三", "李四"])
print(name)

del name
# 删除列表，删除后列表已经不存在


# 数字列表排序,默认是升序
numbers = [55, 44, 465, 653, 42, 75, 13, 11]
numbers.sort()
print(numbers)

# 添加reverse=True,降序排序
numbers.sort(reverse=True)
print(numbers)

# sorted方法是将原列表复制一份随后排序，排序结果不会影响原先列表
result = sorted(numbers)
print(result)

num_list = [i for i in range(11)]
print(num_list)

Num_list = [i for i in range(1, 100, 1) if i % 3 == 0]
print(Num_list)

numbers_1_list = [10, 20, 40, 30, 94, 69, 78, 81]
numbers_2_list = [11, 41, 21, 31, 43, 64, 75, 85]
nub_1 = numbers_1_list + numbers_2_list
mub1 = sorted(nub_1)
print(mub1)
nub_2 = numbers_1_list * 3
mub2 = sorted(nub_2)
print(mub2)
max1 = max(numbers_1_list)
print(max1)
max2 = max(numbers_2_list)
print(max2)
min1 = min(numbers_1_list)
print(min1)
min2 = min(numbers_2_list)
print(min2)
numbers_3_list = [11, 22, 33, 44, 55, 66, 77, 88, 99, 11, 66, 22]
count = numbers_3_list.count(66)
print(count)

numbers_4_list = ["张三", "李四", "王五", "赵六", "孙七"]
for name in numbers_4_list:
    print(name)
# (0, '张三')->元祖类型(下标,:'元素值')
# enumerate 迭代函数 可以同时记录该元素的下标和元素值
for name in enumerate(numbers_4_list):
    print(name)
for index, name in enumerate(numbers_4_list):
    print(index, name)

list_data = [[11, 22], [22, 33, 44], [44, 55, 66,77]]
# 封装写法
for list_i in list_data:
    for list_j in list_i:
        print(list_j, end='\t')
    print()

# 获取元素下标

for i in range(len(list_data)):
    for j in range(len(list_data[i])):
        print(f'{i},{j}', end='\t')
    print()
# 原始写法
for i in range(len(list_data)):
    for j in range(len(list_data[i])):
        print(list_data[i][j], end='\t')
        # print(f'{i},{j}', end='\t')
    print()

for list_i in list_data:
    group_sum = 0
    for list_j in list_i:
        group_sum += list_j
    print(f'group_sum = {group_sum}')
    count += group_sum
    print()
print(f'count={count}')
