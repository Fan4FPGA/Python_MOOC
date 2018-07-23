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


#n阶汉诺塔
'''
count = 0
def hanoi(n, src, dst, mid):
    global count
    if n == 1:
        print("{}:{}-->{}".format(1,src,dst))
        count += 1
    else:
        hanoi(n-1,src,mid,dst)
        print("{}:{}-->{}".format(n,src,dst))
        count += 1
        hanoi(n-1,mid,dst,src)
hanoi(2,'src','dst','mid')
'''


#基本统计值问题
'''
总个数 len()
求和: for ... in 
平均值：求和/总个数
方差：各个数据与平均数差的平方的二和的平均数
中位数 ，排序，奇数 中间位置，偶数中间两个除2

'''

'''
# -*- coding:utf-8 -*-
def getnum():           #获取用户不定长度的输入
    nums = []           #定义一个列表
    iNumStr = input("请输入数据（回车退出）:")
    while iNumStr != "":
        nums.append(eval(iNumStr))
        iNumStr = input("请输入数据（回车退出）:")
    return nums

def mean(numbers):
    s = 0.0
    for num in numbers:
        s = s + num
    return s / len(numbers)

def dev(numbers, mean):
    sdev = 0.0
    for num in numbers:
        sdev = sdev + (num - mean)**2
        temp = sdev / (len(numbers )-1)
    return pow(temp, 0.5)
#sorted 函数可对列表进行排序操作
def median(numbers):
    sorted(numbers)
    size = len(numbers)
    if size % 2 == 0:
        med = (numbers[size//2-1] + numbers[size//2])/2
    else:
        med = numbers[size//2]
    return  med
#整数除法//


n = getnum()
m = mean(n)
d = dev(n,m)
me = median(n)

print("平均值:{},方差:{:.2},中位数:{}.".format(m, d, me))
'''

'''
上述代码主要训练
-获取多个数据，从控制台获取多个不确定数据的方法，使用while语句
-分隔多个函数，模块化的设计放大
-充分利用函数：充分利用python提供的内容函数,比如sorted（），len（），pow（）
'''




#
#字典类型及操作
#

'''
映射 
是一种键（索引）和值（数据）的对应关系

内部颜色 ： 红色
外部颜色 ： 蓝色

列表 0 ~ n 默认的索引

字典 用户自定义
字典是映射的而体现
字典是键 值 队的集合

使用{} 或dict 创建，键值对用；表示

{<键1>:<值1>， <键2>:<值2>， ... ，<键n>:<值n>;}
在字典变量中,通过键获得值
<字典变量> = {<键1>:<值1>; <键2>:<值2>; ... ;<键n>:<值n>;}
值 = 字典变量[键]
字典变量[键] = 值




可以通过[]

'''
'''
d = {"CN":"BJ", "USA":"PD", "FR":"PR"}
print(d["CN"])
'''
'''
生成一个空的字典
de = {}
type(de)  #type(x) 返回x的数据类型
<class "dict">
'''

'''
字典的函数和方法
del d[k] 删除字典d中键k的数据值
k in d 判断键k是否咋字典d中
d.keys() 返回字典d中多余键的信息
d.values() 返回字典d中所有值的信息
d.items() 返回字典d所有键值对的信息
返回的不是列表
d.get(k,<default>) 键值k存在，返回对应的值，不存在则返回default的值
d.pop(k,<default>) 键值k存在，取出对应的键值对，不存在则返回default的值
d.popitem() 随机从字典取出一个键值对，以元组的形式返回
d.clear() 删除所有键值对
d.len(d) 返回字典d元素的个数
'''

#应用场景

#jiba库的使用
#中文分词第三方库
#精确模式，全模式，搜索引擎模


'''
jieba.lcut(s)  返回一个列表类型的分词结果，精确模式
jieba.lcut(s，cut_all = True) 全模式，存在冗余
jieba.lcut_for_search(s) 搜索引擎模式，存在冗余
jieba.add_word(w) 向分词词典添加新词

'''

'''
import  jieba as  J
s = "中华人民共和国是一个伟大的国家"
words = J.lcut(s)
for word in words:
    print(word)
#print(J.lcut(s, cut_all = True))
#print(J.lcut_for_search(s))
'''


#实例10文本词频统计问题
'''
def gettxt():
    txt = open("hamlet.txt","r").read()
    txt = txt.lower()
    for ch in '!"#$%^&*()_+,./:;<=>?@[\\]{}|.':
        txt = txt.replace(ch," ")
    return txt

hamletTxt = gettxt()
words = hamletTxt.split()
counts = {}
for word in words:
    counts[word] = counts.get(word,0) + 1
items = list(counts.items())
items.sort(key=lambda x:x[1], reverse=True)
print("The Top 10 words in the hamlet:")
for i in range(10):
    print(items[i][0],items[i][1])
'''

'''
import jieba
txt = open("threekingdoms.txt","r", encoding="utf-8").read()
words = jieba.lcut(txt)
counts = {}
for word in words:
    if len(word) == 1:
        continue
    else:
        counts[word] = counts.get(word,0) + 1
items = list(counts.items())
items.sort(key=lambda x:x[1], reverse=True)
for i in range(15):
    print(items[i][0], items[i][1])
'''
import jieba
excludes = {"将军","却说","荆州","二人","不可","不能","如此"}
txt = open("threekingdoms.txt", "r", encoding='utf-8').read()
words  = jieba.lcut(txt)
counts = {}
for word in words:
    if len(word) == 1:
        continue
    elif word == "诸葛亮" or word == "孔明曰":
        rword = "孔明"
    elif word == "关公" or word == "云长":
        rword = "关羽"
    elif word == "玄德" or word == "玄德曰":
        rword = "刘备"
    elif word == "孟德" or word == "丞相":
        rword = "曹操"
    else:
        rword = word
    counts[rword] = counts.get(rword,0) + 1
for word in excludes:
    del counts[word]
items = list(counts.items())
items.sort(key=lambda x:x[1], reverse=True)
for i in range(10):
    word, count = items[i]
    print ("{0:<10}{1:>5}".format(word, count))










