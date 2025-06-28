# 第一题：判断变量数据类型
x = 10
y = "10"
z = True

print(f"x的类型是：{type(x)}")
print(f"y的类型是：{type(y)}")
print(f"z的类型是：{type(z)}")

# 第二题：计算圆的面积
radius = float(input("请输入圆的半径："))
pi = 3.14
area = pi * radius ** 2
print(f"圆的面积是：{area}")

# 第三题：字符串转换
str_num = "3.14"
float_num = float(str_num)
int_num = int(float_num)

print(f"字符串{str_num}转换为浮点数是：{float_num}")
print(f"浮点数{float_num}转换为整数是：{int_num}")
print("观察转换结果发现,浮点数转整数会丢失小数部分")