# Python基本知识

## 安装

借助搜索引擎，不难安装Python。值得一提的是，除了单独安装Python的发行版本，你还可以选择安装Anaconda，它包含了Python，同时还自带了很多方便的工具，相当于是一个打包后的工具集合。除此之外，Anaconda还可以提供虚拟环境，这在你学会Python之后的真正开发过程中会很有用。

**Python版本**

历史上Python2和Python3共存了很长一段时间，给初学者带来了很多不便，幸运的是，Python2已经渐渐退出历史舞台，所以初学者只需要学习Python3就好，确保你安装了最近的Python3版本即可。

## Hello World

Python是一门解释性的脚本语言，如果你用过MATLAB，不难理解什么是解释性语言。C++是一门编译性语言，几乎只有一种运行方式： 编译 -> 运行。相比之下，解释性语言的运行方式比较多。

**第一种运行Python的方式**

在命令行中直接运python.exe，你将进入 Python 的REPL，直接打印hello world!

![20220125172013](http://haipeng-openwrite.oss-cn-beijing.aliyuncs.com/images%5C99e0bf8a7a99bd2af6d8f21c22d523f8.png)

什么是REPL？

> 读取-评估-打印循环（REPL），也称为交互式顶层或语言外壳，是一种简单的交互式计算机编程环境，它接受单个用户输入、执行它们并将结果返回给用户； 在 REPL 环境中**编写的程序是分段执行的**。 该术语通常指的是类似于经典 Lisp 机器交互环境的编程接口。 常见的例子包括命令行 shell 和编程语言的类似环境，该技术非常具有脚本语言的特征。
> A read–eval–print loop (REPL), also termed an interactive toplevel or language shell, is a simple interactive computer programming environment that takes single user inputs, executes them, and returns the result to the user; a program written in a REPL environment is executed piecewise. The term usually refers to programming interfaces similar to the classic Lisp machine interactive environment. Common examples include command-line shells and similar environments for programming languages, and the technique is very characteristic of scripting languages.

虽然REPL是脚本语言的特征，但并非只有Python/Javascript这样的脚本语言才有REPL，很多编译语言也提供了这样的功能，比如scala。如果你用过ROOT [https://root.cern/install/](https://root.cern/install/) ，你会发现它其实就是C++的REPL。
> ROOT是通过LLVM技术对C++代码进行了运行时编译，并非使用了传统的编译器，所以才能**executed piecewise**（一段段代码的执行）。

**第二种运行Python的方式**

你也可以把Python代码写在一个文件里面，然后用如下命令运行：

```python
print("hello world")
```

```shell
python code.py
```

**其他运行Python的方式**

Python可以很方便地在其他工具中运行，Pycharm、VS Code、jupyter notebook，等等，这些IDE或编辑器会帮助我们调用Python解释器，更加方便。

## 注释

和C++一样，Python里面也有两种注释：一种是单行注释，另一种是多行注释:smile:。

```python
# 这是一行注释
print("hello world") #这是行尾注释
"""
这是
多行注释
"""
```

## 变量和类型

与C++不同，在Python里面你可以直接使用任何变量，不需要显示指定变量的类型，也不需要提前声明，这和MATLAB里面的用法类似。

```python
a = 1
a = "hell0"
a = 0.5
```

容易看出，我们给变量a先后赋值了整数类型，字符串类型和浮点数。既然变量的类型是随时有可能变的，那么我们怎么知道它到底是什么类型呢？可以利用type函数：

```python
type(a)
```

类型系统是任何编程语言的基础，下面是Python里面内置的一些数据类型，

| 类型    | 例子                |
|---------|---------------------|
| int     | a = 1               |
| float   | a = 0.5             |
| str     | a = "hello"         |
| bool    | a = True/False      |
| complex | a = 1 + 2j          |
| bytes   | a = b"hello"        |
| set     | a = set() #空集合   |
| list    | a = list() #空列表  |
| tuple   | a = tuple() #空元组 |
| dict    | a = dict() #空字典  |

在Python3中float是64位的。int是动态长度的长整型，理论上支持无限大的数字。bytes类型就是二进制类型，将数据保存为字节数组，一个字节数组其实就是二进制串。字符串前面加上 b 就代表该字符串是用字节数组的方式存储的。在Python里面没有char类型。complex是复数类型，在C++之中也是没有的。

:bulb: **类型推断**

Python会自动推断赋值表达式右侧的数据类型，然后给变量设置对应的类型，类似C++中的auto关键字的作用。类型推断是编程语言中很重要的一个特性，优雅的编程语言都会支持类型推断。

:bulb: **关于引号**

Python里面有个非常聪明的设计：单引号和双引号都可以表示引号，效果等价，但不能同时生效。不能同时生效的意思是，如果你用单引号包围一个字符串，那么在字符串内的双引号就是普通字符，就不用加反斜杠了，反之亦然。

```python
s = '我是双引号",我是两个双引号""'
s = "我是单引号',我是两个单引号''"
```

此外，还有一种三引号（三个单引号或三个双引号等价），三引号可以包含多行字符串：

```python
s = '''
多行
字符串
'''
```

多行字符串会把每行的尾部自动加上换行符号，然后合并成一个字符串，多行字符串在你处理长字符串的时候可能有用。

:bulb: **原始字符串 （raw string）**

原始字符串是“所见即所得”的字符串，你只需要在字符串之前加上r，就不用再对字符进行转义了。这在处理Windows下的文件路径时尤其有用，可以提供很多方便：

```python
"""
不用再担心自己忘记把一个反斜杠转换成两个反斜杠了。
"""
path = r"C:\users\xxx" 

s = r'''
多行 \n
字符串
'''
```

:bulb: **格式化字符串**

字符串格式化虽然简单，但是非常常用的一个功能。在Python里面有以下几种方法：

```python
a = "I am"
b = 18
c = "years old."

# 方法一： 很类似C的风格
s = "%s %d %s" % (a, b, c)

# 方法二.a： 自动识别格式，
s = "{0} {1} {2}".format(a, b, c)

# 方法二.b：
s = "{} {} {}".format(a, b, c)

# 方法二.c： b的一个变体，可以自己控制顺序
s = "{0} {1} {2}".format(a, b, c)

# 方法二.d： 可以利用名字格式化，更加可读
s = "{prefix} {age} {suffix}".format(prefix = a, age = b, suffix = c)

# 方法二.e：利用字典
data = {"prefix":"I am", "age":18,"suffix":"years old."}
s = "{prefix} {age} {suffix}".format(**data) 
# **代表把字典的key-value解开，按照单独的key-value pair 传递，效果和方法d等同

# 方法三.a
s = f"{a} {b} {c}"

# 方法三.b
# 支持表达式
s = f"{a} {3*6} {c}"

# 方法三.c
# 你可以直接在大括号里调用函数，实际上，你可以直接在这里“写代码”。
s = f"{a} {get_years_old()} {c}"

```

:link: [Python 3's f-Strings](https://realpython.com/python-f-strings/)

推荐使用第三种方式，当你习惯之后，你会忘掉前两种:smile:。

## 数据结构

set、list、tuple、dict都是容器类型，元组tuple就是不可修改的列表list。与set，list，dict相对应，C++的标准库里也支持list，set，map等类型，不过在Python里使用它们会异常方便。

**创建**

```python
# 创建列表的几种方式
a = []
a = list()
a = [1,2,3]
a = [1,2,"hello"] #列表中可以容纳任何object，在C++里你很难做到这一点
```

```python
# 创建元组
a = ()
print(type(a))
a = tuple()
a = (1,2,3)
a = (1,2,"hello")
```

```python
# 创建字典， 类似C++标准库中的map
a = dict()
a = {}
a = {1:"d", "2":9} # key 和 value的值也是任意的对象，这点和C++不同
```

```python
# 创建集合
a = set()
a = {1,"d", "2",9,1.0,1} # 集合里的元素也可以是任何对象，这点和C++不同
```

**访问元素**

- 按下标访问列表

```python
# 访问列表
a = [1,2,"hello"]
a[0] # 1
a[2] # hello
a[-1] # hello, 负数代表反方向，很容易理解
```

> 访问元组的方式相同。set类型不可以用下标访问，思考一下为什么？:thinking:

- 按key访问字典

```python
# 访问字典
a = {1:"d", "2":9}
a[1] # "d"
a["2"] # 9
```

- 切片 slicing

可以用range函数来创建一个连续整数列表，range函数生成的其实是迭代器，关于什么是迭代器后面会仔细讲，这里你只需要知道必须用list函数把迭代器转换成列表。

```python
a = list(range(10)) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
a[0:1] # [0]
a[2:4] # [2,3]
a[-2:-1] # [8]
```

- 遍历访问


**添加元素**

```python
# 集合
a = set()
a.add(1)
a.add("ok")

# 列表
a = []
a.append(1)
a.append("ok")

# 字典
a = {}
a.update({"name":"wang"})
a.update({"age":18})
```


**删除元素**

```python
# 集合
a = set()
a.add(1)
a.add("ok")
a.remove("ok")

# 列表
a = []
a.append(1)
a.append("ok")
a.remove("ok")

# 字典
a = {}
a.update({"name":"wang"})
a.update({"age":18})
del a["name"]
```

**遍历元素**

遍历这些容器的时候我们需要用到 in 这个运算符，list，tuple，set的遍历方式都是一样的：

```python
a = [1,2,"ok"]
for x in a:
    print(x)
```

字典比较特殊，它每个元素其实是个 key-value的pair，所以按照排列组合，你有很多种去迭代它的方式：

```python
a = {}
a.update({"name":"wang"})
a.update({"age":18})

for x in a: # 默认迭代keys
    print(x)
# output：
# name
# age

for x in a.keys():
    print(x)
# output：
# name
# age

for x in a.values():
    print(x)
# output：
# wang
# 18

for k,v in a.items(): # k,v = (k,v)
    print(k,v)
# output：
# name : wang
# age : 18
```

items() 函数返回的元素其实是个长度为2的元组，元组在任何时候都可以直接展开成多个元素。

## 类型转换

类型之间的转换方法如下表：

|         | int            | float              | str                  | bool                 | complex                | bytes    |
|---------|----------------|--------------------|----------------------|----------------------|------------------------|----------|
| int     | ——             | float(1) > 1.0     | str(1) > "1"         | bool(1) > True       | complex(1) > 1+0j      | ——       |
| float   | int(0.5) > 0   | ——                 | str(0.5) > "0.5"     | bool(0.5) > True     | complex(0.5) > 0.5+0j  | ——       |
| str     | int("1") > 1   | float("0.5") > 0.5 | ——                   | bool("False") > True | complex("1+2j") > 1+2j | b"hello" |
| bool    | int(False) > 0 | float(False) > 0.0 | str(False) > "False" | ——                   | complex(False) > 0j    | ——       |
| complex | ——             | ——                 | str(1+2j) > "1+2j"   | bool(1+2j) > True    | ——                     | ——       |
| bytes   | 同 str2int     | 同str2float        | ——                   | 同str2bool           | 同str2complex          | ——       |

其中bytes类型可以被当作字符串，只不过是字符串的另外一种表示方法。如果要将int或者float转换成bytes，则需要考虑到诸如字节数，大端或小端等细节，用到的场景比较少，在此就不做介绍了。

其他类型转换成bool类型的时候，只有为**零**为**空**的时候才会被转换成False，其他情况一律转换成True，这一点需要注意。

```python
bool(set()) # False
bool([]) # False
bool({}) # False
bool("") # False
bool(0) # False
bool(0.0) # False
```

## 运算符和表达式

**消失的小括号、大括号和分号**

在Python里面我们不需要使用大括号来包裹一个代码块，具有相同**缩进**的代码会自动属于一个代码块。所以大括号在这里消失了。
```c++
if (a == b) {
    printf("ok");
}
```

```Python
if a == b:
    print("ok")
```

运算符和表达式比较基础，可以直接参考： [https://www.runoob.com/python/python-operators.html](https://www.runoob.com/python/python-operators.html) 

绝大部分运算发符在C++之中都有对应，这里值得一提的是Python中的逻辑运算符直接使用： and、or、not，理解起来非常方便。

```python
a = True
b = False
if a and b:
    print("ok")
if a or b:
    print("ok")
if not a:
    print("ok")
```

另外，Python中还有一个成员运算符：in，用来判断一个元素是否在另一个容器里面。这和for循环中使用的in有些像，但功能不太相同。

```python
a = [1,2,5]
if 1 in a:
    print("ok")
```

## 流程控制

条件语句和循环控制语句比较基础，和C++中没有太大区别，可以直接参考以下链接：

[条件语句](https://www.runoob.com/python/python-if-statement.html)
[循环语句](https://www.runoob.com/python/python-loops.html)

## IO和文件操作

- 读文件


- 写文件


- 读二进制文件

- 写二进制文件


## Python和System交互

在Python里面你可以非常方便的和系统进行交互：



## 标准库


## 语法糖

:link: [https://blog.csdn.net/five3/article/details/83474633](https://blog.csdn.net/five3/article/details/83474633)
:link: [https://medium.com/analytics-vidhya/syntactic-sugar-in-python-3e61d1ef2bbf](https://medium.com/analytics-vidhya/syntactic-sugar-in-python-3e61d1ef2bbf)

语法糖（Syntactic sugar），也译为糖衣语法，是由英国计算机科学家彼得·约翰·兰达（Peter J. Landin）发明的一个术语，指计算机语言中添加的某种语法，这种语法对语言的功能并没有影响，但是更方便程序员使用。通常来说使用语法糖能够增加程序的可读性，从而减少程序代码出错的机会。

- 条件赋值

```python
b = 2 
c = 3

if b > c:
    a = b
else:
    a = c

# 更优雅的写法
# 等价于C++种的 a = c > b ? c : a
a = c if c > b else b

```
虽然Python中没有问号和冒号组成的三目运算符,但是可以用if else的条件赋值代替.

- 多元赋值

```python
a = 1; b = 2; c = 3

# 更优雅的写法
a,b,c = 1,2,3
```

- 列表推导式

如果我们想把一个列表中的每个元素变成平方:

```python
a = [0,1,2,3,5,6]
b = []
for x in a:
    b.append(x**2)

# 更优雅的写法
b = [x**2 for x in a]
```

> 如果使用 numpy, 你还可以对array直接进行操作

- 集合推导式

- 字典推导式

