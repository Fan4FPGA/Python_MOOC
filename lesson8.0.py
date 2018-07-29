#-*- coding:utf-8 -*-
'''----------------------------------------------------------------------------
数字类型处理
整数类型的无限范围及4种进制表示
- 浮点数类型的近似无限范围、小尾数及科学计数法
- +、-、
*
、/、//、%、
**、二元增强赋值操作符
- abs()、divmod()、pow()、round()、max()、min()
- int()、float()、complex()

字符串处理
正向递增序号、反向递减序号、<字符串>[M:N:K]
- +、
*
、len()、str()、hex()、oct()、ord()、chr()
- .lower()、.upper()、.split()、.count()、.replace()
- .center()、.strip()、.join(）、.format()格式化

程序分支
单分支 if 二分支 if-else 及紧凑形式
- 多分支 if-elif-else 及条件之间关系
- not and or > >= == <= < !=
- 异常处理 try-except-else-finally

循环
- for…in 遍历循环: 计数、字符串、列表、文件…
- while无限循环
- continue和break保留字: 退出当前循环层次
- 循环else的高级用法: 与break有关

函数定义
使用保留字def定义函数，lambda定义匿名函数
- 可选参数(赋初值)、可变参数(*b)、名称传递
- 保留字return可以返回任意多个结果
- 保留字global声明使用全局变量，一些隐式规则

代码复用递归
- 模块化设计：松耦合、紧耦合
- 函数递归的2个特征：基例和链条
- 函数递归的实现：函数 + 分支结构

集合类型
- 集合使用{}和set()函数创建
- 集合间操作：交(&)、并(|)、差(-)、补(^)、比较(>=<)
- 集合类型方法：.add()、.discard()、.pop()等
- 集合类型主要应用于：包含关系比较、数据去重

序列类型及操作
- 序列是基类类型，扩展类型包括：字符串、元组和列表
- 元组用()和tuple()创建，列表用[]和set()创建
- 元组操作与序列操作基本相同
- 列表操作在序列操作基础上，增加了更多的灵活性

字典
- 映射关系采用键值对表达
- 字典类型使用{}和dict()创建，键值对之间用:分隔
- d[key] 方式既可以索引，也可以赋值
- 字典类型有一批操作方法和函数，最重要的是.get()

文件的操作
- 文件的使用方式：打开-操作-关闭
- 文本文件&二进制文件，open( , )和.close()
- 文件内容的读取：.read() .readline() .readlines()
- 数据的文件写入：.write() .writelines() .seek()

一维数据的处理
- 数据的维度：一维、二维、多维、高维
- 一维数据的表示：列表类型(有序)和集合类型(无序)
- 一维数据的存储：空格分隔、逗号分隔、特殊符号分隔
- 一维数据的处理：字符串方法 .split() 和 .join()

二维数据的处理
- 二维数据的表示：列表类型，其中每个元素也是一个列表
- CSV格式：逗号分隔表示一维，按行分隔表示二维
- 二维数据的处理：for循环+.split()和.join()
--------------------------------------------------------------------------------'''