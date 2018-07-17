# -*- coding:utf-8 -*-
'''
#组合数据类型
#集合类型及操作
#序列类型及操作元组和列表
#实例
#基本统计值计算
#字典类型及操作
#jieba库使用中文分词库
'''
'''
1、集合
多个元素的无无序组合，集合元素不可被修改且独立，不可变数据类型
用{，，，，} 以及set（） 
'''
#集合操作 交& 差- 补^ 并| 比较 >=<
#集合类型提供了方法：.add()  .discard() .pop() 等方法
#两个重要的应用场景：包含关系的比较 。数据去重


#包含关系比较
#数据去重
'''
A = {"py",12,'fs'}
try:
    while True:
	    print(A.pop())
except:
    pass
'''
'''
A = {"py",12,'fs'}
if 12 in A:
    print('TURE')
'''

'''
序列类型
序列具有先后关系的一组元素，有顺序
是一个基本类型

字符串类型 元组类型 列表类型 都是序列类型
元素存在正向递增序号 和反向递减序号

x in s 		不在False 在True
x not in s 在False 不在True
s + t 连接连个序列
s*n 或 n*s 将s复制n次
s[i] 索引 返回s中的第i个元素可正可负
s[i:j] 或 s[i:j:k] 切片 返回序列s中的第i到j的以k为步长的元素子序列
'''

'''
#将列表元素取反
ls = ["python",123,".io"]
print(ls[::-1])
'''

'''
序列的方法：
len(s) 返回s的长度
min(s)返回最小（需要可比较）
max(s)返回最大（需要可比较）
s.index(s)	
s.index(x,i,j) 返回序列s的i位置开始到j第一次出现x的位置
s.count(x) 返回s中出现x的总次数
'''
#ls = ["python",123,".io"]
'''
元组类型 一旦创建就不能被修改
使用()或tuple()创建 ，元素用都和分隔
'''

'''
def func():
	return 1,2
#1,2本事就是元组
'''
'''
creature = "cat", "dog", "tiger", "human"
color = (0x100010, "bulue", creature)
print(color)

color 更大的元组
'''

#元组继承序列所有的方法
'''
creature = "cat", "dog", "tiger", "human"
B = creature[::-1]
print(B)
print(creature)
'''
#不改变原来的元组
'''
creature = "cat", "dog", "tiger", "human"
color = (0x100010, "bulue", creature)
print(color[-1][-1])   #creature[-1] = "human"
'''

#列表类型 可随意被修改 使用[] 或list()创建 
'''
creature = ["cat", "dog", "tiger", "human"]
creature2 = creature
print(creature2)   #[]和list()真正创建一个列表，赋值仅传递引用，两个名字都指向同一个列表
'''

#ls = ["cat", "dog", "tiger", "human"]
'''
ls[i] = x 使用x替换ls的第i个元素
ls[i:j:k] = it 用列表it替换切片后对应元素的子列表
del ls[i] 删除ls的i个元素
del ls[i:j:k] 删除i到j以k为步长的元素
ls +=it 更新ls将it中元素增加到列表ls后
ls*n=更新列表ls，其元素重复n次
ls.append(x) 增加一个元素x
ls.clear() 删除ls中的所有元素
ls.copy()复制一个新的列表
ls.insert(i,x)在列表第i位置增加一个元素,原i位置的以后的元素位置向后移一位
ls.pop(i)将ls中的i位置的元素取出，并删除原列表对应位置的元素
ls.remove(x) 将ls中出现的第一个x删除掉
ls.reverse()表将列表中的元素反转
'''


'''
ls = ["cat", "dog", "tiger", "human"]
ls.insert(2,"FFFF")
print(ls)
print(ls[0])
ls.reverse()
print(ls)
'''

