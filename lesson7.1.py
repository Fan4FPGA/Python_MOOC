#-*- coding=utf-8 -*-

#文件和数据格式化
#文件和文件类型吗，以及读写，打开关闭

#文件的类型
#-文件是数据的抽象和集合

#本质上所有文都是二进制方式存储的
#由单一特定编码组成的文件 如utf-8
#文本文件可看作长字符串

#二进制文件 都是以0 1组成无编码

'''

'''
#文本
'''
tf = open("f.txt", "rt")
print(tf.readline())
tf.close()
'''
#二进制
'''
tf = open("f.txt", "rb")
print(tf.readline())
tf.close()
'''

#打开 - 操作 - 关闭

#文件打开
# 变量[文件句柄] = open（文件名和路径， 打开模式[读或写，文本或二进制]）

#文件打开模式   'r' 只读模式，默认至，如果文件不存在返回FileNotFoundError
#               'w' 覆盖写模式，文件不存在则创建，存在则完全覆盖
#               'x' 创建写模式，文件存在则创建，存在则返回FileExistsError
#               'a' 追加模式，文件不存在则创创建，存在则在文件最后追加
#               'b'二进制模式
#               't'文本文件模式，默认
#               '+'/r/w/x/a一起使用，在原来功能基础上增加读写功能



# a.read(size) 不给参数读出去全部，给参数读出size长度
# a.readline(size)  不该参数读入一行内容，给参数读入该行前size长度
# a.readlines(hint) 读入文件所有行，每行为元素列表，如给出参数，读入前hint行

#文件的全文本操作
#方法一
'''
fname  = input("请输入要打开的文件名称:")
fo = open(fname,"r")
txt = fo.read() #一次全部读入
#对全文txt进行处理
fo.close()
'''

#方法二
'''
fname  = input("请输入要打开的文件名称:")
fo = open(fname,"r")
txt = fo.read(2)
while txt != "":

    # 对txt进行处理
    txt = fo.read(2)
fo.close()
'''

#文件的逐行操作
#方法一
'''
fname  = input("请输入要打开的文件名称:")
fo = open(fname,"r")
for line in fo.readlines():
    print(line)         #一次读入，分行处理
fo.close()
'''

#方法二
'''
fname  = input("请输入要打开的文件名称:")
fo = open(fname,"r")
for line in fo:
    print(line)         #分行读入，分行处理
fo.close()
'''

#文件写入

# a.write(s) 向文件写入一个字符串或一个字节流
''' f.write("xxxxxx")'''
# a.writelines(lines) 将一个元素为字符串的列表写入文件
'''
ls = ["str1","str0"]
f.writelines(ls)
'''
# a.seek(offset) 改变当前文件操作指针的位置 offset 含义 0 - 文件开头 1 - 当前位置 2 - 文件结尾

#try ... except ... 的使用
#文件打开模式 ‘r’ 只读模式，默认至，如果文件不存在返回FileNotFoundError
import time
try:
    tf = open("d.txt")
except FileNotFoundError:
    log = open("open.log", "a+")
    log.write(str(time.ctime())+" ")
    log.write("FileNotFoundError\n")
    log.close()
    print("FileNotFoundError")