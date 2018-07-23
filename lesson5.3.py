#-*- coding:utf-8 -*-

#通第三方库将.py变成可执行文件
#pyinstaller是第三方库
#www.pyinstaller.org
#安装工具pip
#执行pip指令
#Windows 环境下（cmd命令行） 执行 pip install pyinstaller

#pip指令会联网下载并自动安装

#installer 库说明
#pip 

#pyinstaller -F <文件名.py>
#常用参数
#-h 查看帮助
#--clean 清理打包过程中的临时文件
#-D ,-onedir 默认值，生成dist文件夹 不建议使用，建议使用-F参数
#-F ，-onefile 只生成一个可执行文件
#-i <图标文件名.ico>  指定打包程序使用的图标


#只需要在打包的电脑需要安装pyinstaller


#科赫雪花
#-分形机会是一种迭代的几何图形
#科赫曲线

import turtle
def kehi(n, size):
    if n==0:
	    turtle.fd(size)
    else:
        for angle in [0, 60, -120, 60]:
            turtle.left(angle)
            kehi(n-1,size/3)
def main():
    turtle.penup() 
    turtle.setup(800,500)
    turtle.goto(-150,50)
    turtle.pensize(2)
    turtle.pendown()
    kehi(3,300)
    turtle.right(120)
    kehi(3,300)
    turtle.right(120)
    kehi(3,300)
    turtle.penup()
    turtle.goto(-80,-50)
    turtle.pendown()
    turtle.pencolor("green")
    turtle.write('送给狗狗的雪花',font = ("Arial", 18, "normal"))
    turtle.hideturtle()
    turtle.done()
main()