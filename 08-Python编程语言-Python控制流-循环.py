# 01、pythonpython控制流--循环语句
#     循环一句允许我们执行一个语句或语句组多次
# 	python提供了for循环和while循环
# 	封装重复操作
# 	python最重要的基础语法之一
# 	for-in循环
# 	    使用场景：明确知道循环执行的次数或者要对容器进行迭代
# 	range函数：range（101）可以产生一个0到100的整数序列，
#                range（1，100）可以产生一个1到99的整数序列
# 			   range（1,100,20）可以产生一个1到99的奇数序列，其中的2 是步长
# 	a = 1
# 	while a<6:
# 	    print(a)
# 		a = a+1
# 		if a == 3:
# 		    break
# 02、什么是循环
# 	循环语句允许我们执行一个语句或语句组多次
# 	python提供了for循环和while循环
# 	右图是大多数编程语言中循环语句的一般形式
# 03、循环的作用
# 	封装重复操作
# 	Python最重要的基础语法之一
# 04、for-in循环
# 	使用场景：
# 	明确的知道循环执行的次数或者要对一个容器进行迭代（后面会讲到）
# 	range 函数
# 	range(101)可以产生一个0到100的整数序列。
# 	range(1, 100)可以产生一个1到99的整数序列。
# 	range(1, 100, 2)可以产生一个1到99的奇数序列，其中的2是步长。
# 	# 使用for 循环遍历列表中的元素
# for i in [1,2,3]:
# 	print(i)
#
# 	# for 循环结合 range函数
# for i in range(1, 100, 2):
# 	print(i)
# 05、while 循环
# 	满足条件，进入循环
# 	需要设定好循环结束条件
# 06、while循环示例
# count = 0
# # 	# while循环条件，满足条件执行循环体内代码
# while count<5:
# # count 变量+1，否则会进入死循环
# 	count += 1
# 	print(count)
# 07、break-跳出整个循环体
# 	# while循环
count = 0
# while循环条件，满足条件执行循环体内代码
# while count<5:
# # count 变量+1，否则会进入死循环
# 	count += 1
# 	print(count)
# 	if count == 3:
# 		break
list_demo = [ 1, 2, 3, 4, 5, 6]
# 循环遍历列表
for i in list_demo:
  # 如果i 等于三，那么跳出整个for循环
  # 不再打印后面的4、5、6
	print(i)
	if i == 3:
		break
# 08、break-跳出整个循环体
# 	# while循环
# 	count = 0
# 	# while循环条件，满足条件执行循环体内代码
# 	while count<5:
# 	  # count 变量+1，否则会进入死循环
# 	  count += 1
# 	  if count == 3:
# 		break
# 	list_demo = [ 1, 2, 3, 4, 5, 6]
# 	# 循环遍历列表
# 	for i in list_demo:
# 	  # 如果i 等于三，那么跳出整个for循环
# 	  # 不再打印后面的4、5、6
# 	  print(i)
# 	  if i == 3:
# 		break
# 09、pass
# 	pass:
# 	没有实质性含义，通常占位使用
# 	不影响代码的执行逻辑
# 	print("hogwarts")
# 	pass
# 	print("school")
# 10、for 循环-实例
# 	计算1~100 求和
# 	使用分支结构实现1~100之间的偶数求和
# 	不使用分支结构实现1~100之间的偶数求和
# 11、for 循环-实例
# 	计算1~100 求和
# 	使用分支结构实现1~100之间的偶数求和
# 	不使用分支结构实现1~100之间的偶数求和
# 12、for 循环-实例
# 	计算1~100 求和
# 	使用分支结构实现1~100之间的偶数求和
# 	不使用分支结构实现1~100之间的偶数求和