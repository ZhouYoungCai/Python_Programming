t5 = 1, 2, 3
print(type(t5))  # 1、直接使用逗号分隔

t3 = (1, 2, 3)
print(t3)
t4 = ('a', 'b', 'c')
print(t4)  # 2、通过小括号填充元素

t1 = tuple()
print(type(t1))
t2 = tuple([1, 2, 3])
print(t2)
print(type(t2))  # 3、通过构造函数tuple()