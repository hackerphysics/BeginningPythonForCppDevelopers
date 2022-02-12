# 类和面向对象

## 定义类

在Python中定义一个类：

```python
class Bird:
    pass # 当你什么也不想做的时候，可以使用pass
```

在Python3中，所有类默认继承自object类，所以虽然我们这个类看起来什么都没有，但它也包含了丰富的内容，我们可以用 dir 这个方法来查看一个类或者一个函数的内部细节，打印 dir(Bird) 的结果，你会看到如下内容：

```shell
['__class__',
 '__delattr__',
 '__dict__',
 '__dir__',
 '__doc__',
 '__eq__',
 '__format__',
 '__ge__',
 '__getattribute__',
 '__gt__',
 '__hash__',
 '__init__',
 '__init_subclass__',
 '__le__',
 '__lt__',
 '__module__',
 '__ne__',
 '__new__',
 '__reduce__',
 '__reduce_ex__',
 '__repr__',
 '__setattr__',
 '__sizeof__',
 '__str__',
 '__subclasshook__',
 '__weakref__']
```

可以看出，这些默认提供的方法名前后都有两个下划线，这些方法在Python内被称为**魔法方法**，用来实现一些特殊的功能，会在一些特殊的时机被系统调用。

## 给类增加成员变量

现在我们给这个鸟类增加一点东西：

```python
class Bird:
    color = "red"
    age = 1
    childrens = []
```

Python中并没有常量的概念，所以一切成员都是变量。这意味着，我们可以随意对他们进行修改。

```python
b = Bird()
b.color = "green"
b.color # green
```

## 给类增加方法

```python
class Bird:
    color = "red"
    age = 1
    childrens = []
    def eat(self): # self 可以类比于 c++ 中的this
        print("eat")
    def grow(self):
        self.age += 1 # 注意，在类方法中引用类成员必须用 self.
```

在类中定义的方法（method）的第一个参数必须为self，这反应了类中方法和普通函数的区别，这么约定的原因后面会讲到，接下来我们就可以调用这些方法了：

```python
b = Bird()
b.eat()
b.grow()
print(b.age)
# eat
# 2
```

## 构造方法

在Python里面，构造方法的名字统一为__init__， 这是个魔法方法，在上面魔法方法列表中你能找到它，这说明定义类的时候默认就会从object父类继承一个__init__方法，只不过这个方法基本什么都不会做。如果我们想自己定义一个构造方法，那么直接覆盖它就好，也就是重载。

```python
class Bird:
    color = "red"
    age = 1
    childrens = []
    def __init__(self): 
        self.age = 0 # 进行一些初始化的操作
        self.color = ""
    def eat(self): # self 可以类比于 c++ 中的this
        print("eat")
    def grow(self):
        self.age += 1 # 注意，在类方法中引用类成员必须用 self.
```

现在，构造函数帮助我们做了一些初始化的工作，我们可以试一下效果：

```python
b = Bird()
print(b.age)
# 0
```

可以看出，初始化会覆盖初始定义的变量值。所以看起来最开始的定义没有什么用，对不对？不如把它去掉呢？

```python
class Bird:
    color = "red"
    childrens = []
    def __init__(self): 
        self.age = 0 # 进行一些初始化的操作
        self.color = ""
    def eat(self): # self 可以类比于 c++ 中的this
        print("eat")
    def grow(self):
        self.age += 1 # 注意，在类方法中引用类成员必须用 self.
        
b = Bird()
print(b.age)
# 0
```

果然可以。**在C++中，我们使用一个变量的时候总是需要预先定义，但是在Python中并不需要这样，你只需要在用的时候直接用就可以，使用的同时也完成了定义。**

## 多个构造方法？

在C++中，我们通常会给一个类定义多个构造方法，来满足不同场景下的需求，不同的构造方法拥有不同的参数类型或参数个数（这是一种多态的技术）。在Python里面可以这样吗？我们试一下，看看会发生什么：

```python
class Bird:
    color = "red"
    childrens = []
    def __init__(self): 
        self.age = 0 # 进行一些初始化的操作
        self.color = ""
    def __init__(self, age): # 另外一个构造方法
        self.age = age 
        self.color = ""
    def eat(self): # self 可以类比于 c++ 中的this
        print("eat")
    def grow(self):
        self.age += 1 # 注意，在类方法中引用类成员必须用 self.
        
b = Bird()
print(b.age)
```

这一次，我们失败了：

```shell
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
~\AppData\Local\Temp/ipykernel_47416/476329091.py in <module>
     13         self.age += 1 # 注意，在类方法中引用类成员必须用 self.
     14 
---> 15 b = Bird()
     16 print(b.age)

TypeError: __init__() missing 1 required positional argument: 'age'
```

仔细看错误信息（**这很重要，每次出错的时候记得都要先这样做**），Python在告诉我们少输入了age这个参数，看起来两个构造函数Python只接受第二个：

```python
b = Bird(3)
print(b.age)
# 3
```
这样调用之后果然成功了，你会发现，虽然我们写了两个构造函数，但是Python只实现了第二个，其实第一个是被第二个偷偷覆盖了，并且Python不会给我们报任何错误，除非你去调用那个并不存在的构造函数。

> Python语言的特性就是这样，只有当你执行到具体的代码时，才会暴露出错误。有的时候开发很迅速，测试也很顺畅，但依然有一些问题被隐藏起来了，只有在运行的时候才会暴露。Python作为一门脚本语言，动态解释执行，固然有足够多的优点，但是相比于编译语言还是有一些缺点的，使用的时候需要注意。

那么，我们如何实现多个构造函数呢？ 仔细想想，我们需要的并不一定是多个构造函数，我们需要的是在不同场景下完成不同的构造。因为Python可接受的参数非常灵活，所以很多需求完全可以在一个函数内实现。

比如，我们可以用默认参数：

```python
class Bird:
    color = "red"
    childrens = []
    def __init__(self, age = 0): 
        self.age = age # 进行一些初始化的操作
        self.color = ""
    def eat(self): # self 可以类比于 c++ 中的this
        print("eat")
    def grow(self):
        self.age += 1 # 注意，在类方法中引用类成员必须用 self.
```


还有更灵活的方式，

```python
class Bird:
    color = "red"
    childrens = []
    def __init__(self,  *args, **kwargs): 
        if "age" in kwargs:
            self.age = kwargs["age"] # 进行一些初始化的操作
        else:
            self.age = 0
        self.color = ""
    def eat(self): # self 可以类比于 c++ 中的this
        print("eat")
    def grow(self):
        self.age += 1 # 注意，在类方法中引用类成员必须用 self.
b = Bird(age = 3)
print(b.age)
# 3
```

所以在Python中有很多灵活的方式来实现这些需求。

## 静态成员变量

C++中有静态成员变量，可以在不对类进行实例化的情况下调用，Python中有没有呢？我们重新看一下这个类的定义，

```python
class Bird:
    color = "red"
    age = 1
    childrens = []
```
我们试一下直接访问这些变量：

```python
Bird.color
# red
Bird.age
# 1
```

所以，在类中直接定义的成员变量默认都与可以通过类名访问，等价于C++中的静态变量。

```python
class Bird:
    color = "red"
    childrens = []
    def __init__(self): 
        self.age = 0 # 进行一些初始化的操作
        self.color = "green"
    def eat(self): # self 可以类比于 c++ 中的this
        print("eat")
    def grow(self):
        self.age += 1 # 注意，在类方法中引用类成员必须用 self.
        
b = Bird()
print(b.color)
print(Bird.color)
print(b.age)
print(Bird.age)
```

```shell
green
red
0
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)
~\AppData\Local\Temp/ipykernel_47416/519595942.py in <module>
     14 print(Bird.color)
     15 print(b.age)
---> 16 print(Bird.age)

AttributeError: type object 'Bird' has no attribute 'age'

```

注意观察，这里我们看到了两个有意思的现象：
- 通过类名访问color和通过对象访问color，得到的值不一样
- 在类方法中定义的变量age，通过类名是无法访问的

## 类对象和实例对象

Python的代码在编译时，无论是函数，还是类，都生成了相应的对象，无论这个类是否实例化，都生成了类对象。这也是为什么在不创建新对象的前提下你可以直接访问类里面的内容。那么这个类对象和手动创建的新对象之间有什么区别呢？

```python
class Bird:
    pass
b = Bird()
# type
print(type(Bird))
print(type(b))

# <class 'type'>
# <class '__main__.Bird'>

```
我们看到他们的类型（type）是不一样的，在没有实例化之前，类对象的类型统一为 "type"。我们再直接打印他们，看看他们会输出什么：

```python
class Bird:
    pass
b = Bird()

print((Bird))
print((b))

# <class '__main__.Bird'>
# <__main__.Bird object at 0x000001DEAD20D6A0>

```
> 打印对象实际上调用了对象的魔法方法：\_\_str\_\_(), str(obj)函数也会调用这一魔法方法，如果你希望将object转成自定义的字符串，你可以重新定义这一方法。

打印类名得到一个class的描述（和type(b)的输出一样！，想想为什么？）， 打印创建的对象带有额外的地址信息，这个地址就是对象在内存中的地址。

总之，类对象和实例化的对象之间还是有区别的。 类对象就是一个静态对象，可以类比于C++中的静态类。所以，在Python中你不需要创建静态成员和静态方法，类中定义的所有变量和方法都是静态的，听起来是不是有点不可思议？我们自己验证一下是否确实如此：

```python
class Bird:
    color = "red"
    childrens = []
    def __init__(self): 
        self.age = 0 # 进行一些初始化的操作
        self.color = "green"
    def eat(self): # self 可以类比于 c++ 中的this
        print("eat")
    def grow(self):
        self.age += 1 # 注意，在类方法中引用类成员必须用 self.

print(Bird.color)
# red
print(Bird.childrens)
# []
print(Bird.age)
# AttributeError: type object 'Bird' has no attribute 'age' ! 注意，思考一下为什么不能访问 age？
Bird.eat()
# TypeError: eat() missing 1 required positional argument: 'self'  ？ 为什么会失败
```

不是说好了类对象中的所有方法都是静态方法吗，为什么调用eat方法会失败呢？ 仔细阅读错误提示！Python告诉我们，我们少输入了一个参数。那如果我们随便传入一个参数呢？

```python
Bird.eat(1)
# eat
```

居然调用成功了！

实际上，因为eat方法中并没有使用self这个参数，所以你传入任何东西都可以，这个方法还能正常工作。 那么请思考一下，为什么在实例化后的对象上面调用eat方法就不需要传入参数呢？ 其实很简单，是Python偷偷帮助我们给方法传入了这一个参数。请记住，这正是方法和函数的重要区别之一！**对象在调用方法的时候会偷偷传入一个参数放到第一个位置。**

那么这个self参数究竟是什么呢？ 我们在上面提到过，可以把它类比于C++的this。为了探究这一点，我们不妨再做点实验：

```python
Bird.grow(1) # 如法炮制，尝试调用grow方法
# AttributeError: 'int' object has no attribute 'age'
```

这一次我们失败了，Python告诉我们 int 对象没有age属性。因为我们在grow函数中使用了self这个参数，并且调用了self的属性 self.age。我们传入了一个整数1，于是报了上面的错误。而当你调用 b.grow() 的时候，情况会有所不同，首先，在创建对象b的时候会调用构造方法__init__， 在那里会创建age这个属性，然后Python会把对象本身作为参数传入到grow，self自然也就具有了这个属性。调用self.age就好比c++中调用this->age。

到这里还没结束…… 我们再想想，Python给我们的错误提示只是说： 'int' object has no attribute 'age'， 可没有说必须要传入一个Bird的对象进来啊？ 看一下下面的代码：

```python
class VirtualBird:
    age = 100

class Bird:
    color = "red"
    childrens = []
    def __init__(self): 
        self.age = 0 # 进行一些初始化的操作
        self.color = "green"
    def eat(self): # self 可以类比于 c++ 中的this
        print("eat")
    def grow(self):
        self.age += 1 # 注意，在类方法中引用类成员必须用 self.
        print(self.age)

Bird.grow(VirtualBird)
# 101
```

我们用一个“假鸟”成功欺骗了Python！看起来，self这个参数仅仅是一个参数，Python约定会在调用方法的时候把对象本身传进来，当然你也可以传进来别的东西，只要保证方法本身能正常工作！**Python里面有很多的约定，你可以遵守，也可以不遵守**，甚至self这个参数命也是约定! 不信你看：

```python
class VirtualBird:
    age = 100

class Bird:
    color = "red"
    childrens = []
    def __init__(self): 
        self.age = 0 # 进行一些初始化的操作
        self.color = "green"
    def eat(self): # self 可以类比于 c++ 中的this
        print("eat")
    def grow(you):
        you.age += 1 # 注意，在类方法中引用类成员必须用 self.
        print(you.age)

Bird.grow(VirtualBird)
# 101
```

Python真是一门自由的语言，如果和C++相比，在这里你仿佛完全不受束缚了。不过要小心，自由也是有代价的，他会让有些错误更加隐蔽，写代码的时候可不要大意了。

于是，类对象下面的方法都是静态方法（严格来说应该叫函数，下面会有说明），即使是带self参数的也是如此。
Python类对象
1. Python是脚本语言，Pythonn的代码在编译时，无论是函数，还是类，都生成了相应的对象，无论这个类是否实例化，都生成了类对象
2. Python类对象是一个静态对象,一旦生成，就不再变化
3. 类对象生成时，init构造函数没有运行,所以调用类方法时，init构造方法的实例属性不存在，不可以调用init方法中self.xxx实例属性
4. 类属性是类对象的静态变量
5. 类方法/函数是类对象的静态方法

当一个类被实例化后，会调用init方法，然后在内存中生成一个新的对象，拥有一份属于自己的属性，和类对象之间相互独立。

```python
class Bird:
    color = "red"
    age = 1
    childrens = []
    def __init__(self): 
        self.age = 0 # 进行一些初始化的操作
        self.color = "green"
    def eat(self): # self 可以类比于 c++ 中的this
        print("eat")
    def grow(self):
        self.age += 1 # 注意，在类方法中引用类成员必须用 self.
        
b = Bird()
print(b.color)
print(Bird.color)

# green
# red

```

可以看出，改变实例对象的属性值并不会影响类对象的属性值。

## 静态方法

回顾一下我们上面调用类对象静态方法的方式：在调用eat方法的时候必须传入一个dummy的参数，这看起来非常不方便，如果我们确定这是一个类的静态，方法，是否可以不要self这个参数呢？

```python
class Bird:
    def eat():
        print("eat")

Bird.eat()
# eat
```
确实可以，这样看起来自然多了。不过这带来了新的问题：

```python
class Bird:
    def fly(self):
        print("bird fly")
    def eat():
        print("eat")

b= Bird()
b.fly()
b.eat()
# bird fly
# TypeError: eat() takes 0 positional arguments but 1 was given

```

如果这样定义，实例对象就无法调用这一方法了，因为实例对象在调用的时候总是偷偷传入了一个参数。在C++里面，静态方法不管用类名还是新建的对象都可以正常调用，在Python里面就不能有类似的方法吗？当然有,而且实现起来很简单:

```python
class Bird:
    def fly(self):
        print("bird fly")
    @staticmethod
    def eat():
        print("eat")

Bird.eat()
b= Bird()
b.fly()
b.eat()
# eat
# bird fly
# eat
```
可以看到,现在不管怎么调用鸟儿都可正常吃了.

## 装饰器/注解

这个 @staticmethod 看起来有点神秘,它是如何工作的呢? 

你可以自己写一个装饰器:

装饰器把方法变成了函数~


## 方法和函数的区别



## 魔法方法:\_\_get\_\_


## 类方法

类方法和静态方法之间有一些区别,

定义在class中的函数，在实例化的时候才会变成方法，否则它依然只是个函数。

## 类继承

### 调用超类方法

### Override

## 异常