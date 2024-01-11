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

