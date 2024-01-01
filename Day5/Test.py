s = 'hello world'
t = "hello world"
index = s.index('o')

print(f'index = {index}')

print("first is", format(t))

print("我叫{}，今年{}岁".format("小a", 18))
print("我叫{},今年{}岁".format("小e", 19))

print("我是{0},\n他是{1},\n她是{1},\nra是{1}".format("部落", "联盟"))
print("小明喜欢{1},{2}和{0}".format("海绵宝宝", "机器猫", "海贼王", "火影忍者", "龙珠"))
print("我今年{age}岁,我在读{college}".format(age=18, college="大学"))
print("我今年{age}岁,我在读{college}".format(college="大学", age=18))
print("我是要当{0},他是要当{1}，这个世界只有一个{truth}"
      .format("海贼王", "火影", truth="真理"))
a = ["鸣人", "火影", "雏田"]
print("我是{},我是要当{}的男人".format(a[0], a[2]))
print("我是{},我是要当{}的男人".format(*a))
print("我是{1},我是要当{2}的男人".format(*a))
v = {"name": "孙悟空", "skill": "龟派气功"}
print("我是{name}，我的绝招是{skill}".format(**v))
name = ["卡卡罗特", "界王拳"]
names = {"nickname": "孙君", "skill": "元气弹"}
print("我是{0},我的绝招是{skill}".format(*name, **names))
print("我是{nickname},我的绝招是{1}".format(*name, **names))
a = ["卡卡罗特"]
dic = {"name": "超级赛亚人"}
print("我是{0}，我也是{0},因为我是正义的战士，所以我变成了{name}".
      format("卡卡罗特", *a, **dic))
