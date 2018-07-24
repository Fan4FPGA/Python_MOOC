#-*- coding:utf-8 -*-
#自动轨迹绘制
#根据 脚本绘制轨迹

#基本思路
# -1 定义数据文件格式
# -2 编写程序，根据文件接口解析参数绘制图形
# -3 编制数据文件

#数据接口定义
#   300，        0，              144，    1，0，0
#   行进距离    转向（1右0左）    角度     R G B （0-1的浮点数）

import turtle as t
t.title('自动轨迹绘制')
t.setup(800, 600, 0, 0)
t.pencolor("red")
t.pensize(5)

#数据读取
datals = []
f = open("data.txt")
for line in f:
    line = line.replace("\n","")
    datals.append(list(map(eval, line.split(","))))
f.close()
#自动轨迹绘制
for i in range(len(datals)):
    t.pencolor(datals[i][3],datals[i][4],datals[i][5])
    t.fd(datals[i][0])
    if datals[i][1]:
        t.right(datals[i][2])
    else:
        t.left(datals[i][2])
t.done()


