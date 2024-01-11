s = 'hello world'
t = "hello,world"
index = s.index('o')
# isalnum 判断一串字符串是否全部由数字和字母组成，如果不是则传回false，是则返回true
value1 = s.isalnum()
value2 = t.isalnum()

s.capitalize()
print(s)
# 逆向查找
value3 = s.rindex('o')
print(f'value3={value3}')

value4 = s.find('o')
print(f'value4={value4}')
print(f'value1 = {value1}')
print(f'value2 = {value2}')

print(f'index = {index}')

print("first is", format(t))

# format的用法

print("我叫{}，今年{}岁".format("小a", 18))
print("我叫{},今年{}岁".format("小e", 19))

print("我是{0},\n他是{1},\n她是{1},\nra是{1}".format("部落", "联盟"))
print("小明喜欢{1},{2}和{0}".format("海绵宝宝", "机器猫", "海贼王", "火影忍者", "龙珠"))
print("我今年{0}岁了,读{1},我家住在{address}".format("1", "一", address="翻斗花园一号"))
# .format可以采用{0}{1}的方式自动填充.format中的内容
# 注意事项：采用此方法标数字必须从0开始
print("我今年{age}岁,我在读{college}".format(age=18, college="大学"))
print("我今年{age}岁,我在读{college}".format(college="大学", age=18))
print("我是要当{0},他是要当{1}，这个世界只有一个{truth}"
      .format("海贼王", "火影", truth="真理"))
a = ["鸣人", "火影", "雏田"]
print("我是{},我是要当{}的男人".format(a[0], a[2]))
print("我是{},我是要当{}的男人".format(*a))
print("我是{1},我是要当{2}的男人".format(*a))
v1 = {"name": "小红", "address": "翻斗花园一号"}
print("我是{name},住在{address}".format(**v1))
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
