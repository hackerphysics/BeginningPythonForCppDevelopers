# Python基本知识

## 安装

借助搜索引擎，不难安装Python。值得一提的是，除了单独安装Python的发行版本，你还可以选择安装Anaconda，它包含了Python，同时还自带了很多方便的工具，相当于是一个打包后的工具集合。除此之外，Anaconda还可以提供虚拟环境，这在你学会Python之后的真正开发过程中会很有用。

### Python版本

历史上Python2和Python3共存了很长一段时间，给初学者带来了很多不便，幸运的是，Python2已经渐渐退出历史舞台，所以初学者只需要学习Python3就好，确保你安装了最近的Python3版本即可。

## Hello World

Python是一门解释性的脚本语言，如果你用过MATLAB，不难理解什么是解释性语言。

**第一种运行Python的方式**

在命令行中直接运python.exe，你将进入 Python 的REPL，直接打印hello world!

![20220125172013](http://haipeng-openwrite.oss-cn-beijing.aliyuncs.com/images%5C99e0bf8a7a99bd2af6d8f21c22d523f8.png)

什么是REPL？看看wiki上面怎么说：

> A read–eval–print loop (REPL), also termed an interactive toplevel or language shell, is a simple interactive computer programming environment that takes single user inputs, executes them, and returns the result to the user; a program written in a REPL environment is executed piecewise. The term usually refers to programming interfaces similar to the classic Lisp machine interactive environment. Common examples include command-line shells and similar environments for programming languages, and the technique is very characteristic of scripting languages.
> 
> 读取-评估-打印循环（REPL），也称为交互式顶层或语言外壳，是一种简单的交互式计算机编程环境，它接受单个用户输入、执行它们并将结果返回给用户； 在 REPL 环境中编写的程序是分段执行的。 该术语通常指的是类似于经典 Lisp 机器交互环境的编程接口。 常见的例子包括命令行 shell 和编程语言的类似环境，该技术非常具有脚本语言的特征。

虽然REPL是脚本语言的特征，但是并非只有像Python这样的脚本语言才有REPL，很多编译语言也提供了这样的功能，比如scala。如果你用过ROOT [https://root.cern/install/](https://root.cern/install/) ，ROOT不就是一个C++的REPL？
> ROOT是通过LLVM技术对C++代码进行了运行时编译，并非使用了传统的编译器，所以才能**executed piecewise**（一段段代码的执行）。

**第二种运行Python的方式**

你也可以把Python代码写在一个文件里面，然后用如下命令运行：
```shell
python code.py
```

**第N种运行Python的方式**

Python如果和其他工具组合，还可以有更多种运行方式，比如在各种IDE里面、在jupyter notebook里，但这些运行方式最终都会调用python程序，只是给大家提供了一些便利而已。

## 注释

Python里面有两种注释：
```python
# 这是一行注释
print("hello world") #这是行尾注释
"""
这是多行注释
"""
```

## 引号

关于引号，Python里面有个非常聪明的设计：单引号和双引号都可以表示引号，效果等价，但不能同时生效。不能同时生效的意思是，如果你用单引号包围一个字符串，那么在字符串内的双引号就不用加反斜杠了，反之亦然。

把上面的双引号替换掉，效果是一样的。

```python
# 这是一行注释
print('hello world') #这是行尾注释
'''
这是区域注释
''''
```

```python
s = '我是双引号",我是两个双引号""'
s = "我是单引号',我是两个单引号''"
```

## 类型和变量

## 类型转换

## 运算符和表达式

### 算术运算符

### 逻辑运算符

### 位运算符

### 特殊的表达式

条件表达式  

lambda 表达式

## 流程控制

<!-- 三目运算符 -->

## 数据结构

## 类型注解

## 输入与输出

## 标准库

## Python和System交互

## 语法糖

什么是语法糖？
