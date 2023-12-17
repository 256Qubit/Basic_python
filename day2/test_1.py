from termcolor import colored, cprint


# cprint("TESTING TERMCOLOR", "red")
#
class SqList:
    def __init__(self, capacity=0):
        self.capacity = capacity
        self.data = [None] * self.capacity
        self.size = 0

    # 获取顺序表长度
    def get_size(self):
        return self.size

    # 创建顺序表
    def create_sqlist(self, a):
        for i in range(len(a)):
            # 出现上溢出则自动将容量扩充两倍
            if self.size == self.capacity:
                new_capacity = self.capacity * 2
                self.resize(self, new_capacity)
            self.data[self.size] = a[i]
            self.size += 1

    # 打印顺序表
    def display(self):
        if self.size == 0:
            print("None")
        print(*self.data[:self.size])  # 去框

    # 修改线性表的最大容量
    def resize(self, new_capacity):
        if new_capacity >= self.capacity:
            self.data = self.data + [None] * (new_capacity - self.capacity)
        else:
            self.data = self.data[:new_capacity]
        self.capacity = new_capacity

    # 表尾插入元素
    def add_element(self, element):
        # 出现上溢出则自动将容量扩充两倍
        if self.size == self.capacity:
            self.resize(self.size * 2)
        self.data[self.size] = element
        self.size += 1

    # 指定index位置插入元素
    def insert_element(self, index, element):
        if self.size == self.capacity:
            self.resize(self.size + 1)
        for i in range(self.size, index, -1):
            self.data[i] = self.data[i - 1]
        self.data[index] = element
        self.size += 1

    # 删除指定index位置元素
    def delete_element(self, index):
        for i in range(index, self.size - 1):
            self.data[i] = self.data[i + 1]
        self.size -= 1

    # 修改指定index位置元素
    def modify_item(self, index, x):
        self.data[index] = x

    # 查找第一个数值为num的元素
    def get_num(self, num):
        for i in range(self.size):
            if self.data[i] == num:
                return i
        return -1

    # 获取元素
    def get_item(self, index):
        return self.data[index]


score_of_chinese = int(input(f'请输入语文成绩：'))
score_of_mathematics = int(input(f'请输入数学成绩：'))
score_of_english = int(input(f'请输入英语成绩：'))

sqlist = SqList(3)
sqlist.create_sqlist(list(range(3)))
# sqlist.get_size()
sqlist.modify_item(0, score_of_chinese)
sqlist.modify_item(1, score_of_mathematics)
sqlist.modify_item(2, score_of_english)
sqlist.display()
if 0 <= int(sqlist.data[0]) and int(sqlist.data[1]) and int(sqlist.data[2]) <= 100:
    if int(sqlist.data[0]) >= 60:
        print(f'语文成绩及格')
    else:
        def bold_text(text):
            return f"\033[1m{text}\033[0m"


        print(bold_text("警告："))
        print('\t', bold_text("语文成绩不及格！！！"))

    if int(sqlist.data[1]) >= 60:
        print(f'数学成绩及格')
    else:
        def bold_text(text):
            return f"\033[1m{text}\033[0m"


        print(bold_text("警告："))
        print('\t', bold_text("数学成绩不及格！！！"))

    if int(sqlist.data[2]) >= 60:
        print(f'英语成绩及格')
    else:
        def bold_text(text):
            return f"\033[1m{text}\033[0m"


        print(bold_text("警告："))
        print('\t', bold_text("英语成绩不及格！！！"))
else:
    print(f'成绩非法！！！')

if int(sqlist.data[0]) > int(sqlist.data[1]):
    if int(sqlist.data[0]) > int(sqlist.data[2]):
        print(f'您的成绩最好学科为【语文】')
    else:
        print(f'您的成绩最好学科为【英语】')
else:
    if int(sqlist.data[1]) > int(sqlist.data[2]):
        print(f'您的最好成绩学科为【数学】')
    else:
        print(f'您的成绩最好学科为【英语】')

num1 = int(input(f'请输入第一个数字：'))
num2 = int(input(f'请输入第二个数字：'))
num3 = int(input(f'请输入第三个数字：'))

# 使用三目运算符两两比较大小
# 结构为：num1 条件 num2，条件有两种状态(true/false)，如果结果为true，返回num1。如果结果为false,返回num2.
second_max = num1 if num1 > num2 else num2
first_max = second_max if second_max > num3 else num3

print(f'max={first_max}')

category = input(f'您是否为会员(y:会员 n:非会员)：')
consumption_amount = int(input(f'请输入您消费的金额：'))

# 会员判断
if category == 'y' or category == 'Y':  # 会员折扣
    if consumption_amount >= 200:
        consumption_amount = consumption_amount * 0.8
        print(f'折后价格为{consumption_amount}')
    elif consumption_amount >= 100:
        consumption_amount = consumption_amount * 0.9
        print(f'折后价格为{consumption_amount}')
    else:
        consumption_amount = consumption_amount
        print(f'折后价格为{consumption_amount}')
elif category == 'n' or category == 'N':  # 非会员折扣
    if consumption_amount >= 200:
        consumption_amount = consumption_amount * 0.95
        print(f'折后价格为{consumption_amount}')
    else:
        consumption_amount = consumption_amount
        print(f'折后价格为{consumption_amount}')
else:
    print(f'输入非法！！！')
