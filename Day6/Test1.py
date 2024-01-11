name = ["a", "b", "v", "d", "f", "o", "o"]

name.remove("o")
print(name)

# pop如果不传递坐标，默认删除最后一个
name.pop(0)
print(name)

name.clear()
print(name)

name.extend(["李一", "李二", "李三", "李四"])
print(name)
