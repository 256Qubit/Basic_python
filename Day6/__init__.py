
name = ["a", "b", "v", "d", "f", "o", "o"]

name.append("王五")
print(name)

name.insert(0,"赵二")
print(name)

Merge = ["李一", "李二", "李三", "李四"]
name.extend(Merge)
print(name)

var_1 = name[::-1]

print(var_1)

var_2 = name[0:6:1]

print(var_2)
