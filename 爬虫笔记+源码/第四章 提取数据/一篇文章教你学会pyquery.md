# 什么是pyquery

pyquery是类似于jquery的网页解析工具，让你使用jquery的风格来遍历xml文档，它使用lxml操作html的xml文档，它的语法与jquery很像，和我们之前所讲的解析库xpath与Beautiful Soup比起来更加灵活与简便，并且增加了添加类和移除节点的操作，这些操作有时会为提取信息时带来极大的便利。

# 使用pyquery

如果你对web有所了解，并且比较喜欢使用CSS选择器，那么这里有一款更适合你的解析库——jquery。

## 准备工作

在使用之前，请确保已经安装好qyquery库。安装教程如下所示：

```
pip install pyquery
```

## 初始化

和Beautiul Soup一样，在初始化pyquery的时候，也需要传入html文本来初始化一个pyquery对象。

初始化的时候一般有三种传入方式：传入字符串、传入URL、传入html文件。

- **字符串初始化**

```python
html = '''
<div>
    <ul>
        <li class="item-0">first-item</li>
        <li class="item-1"><a href="link2.html">second item</a></li>
        <li class="item=-0 active"><a href="link3.html"><span class=""bold>third item</span></a></li>
        <li class="item-1 active"><a href="link4.html">fourth item</a></li>
        <li class="item-0"><a href="link5.html">fifth item</a></li>        
    </ul>
</div>
'''

from pyquery import PyQuery as pq


doc = pq(html)
print(doc)
print(type(doc))
print(doc('li'))
```

先对上面的代码做简单的描述：

首先引入PyQuery对象，取名为pq。然后声明一个长HTML字符串，并将其当作参数传给PyQuery类，这样就成功的进行了初始化。

接下来将css选择器作为参数传入初始化对象，在这个示例中我们传入`li`节点，这样就可以选择所有的`li`节点.。

- **URL初始化**

初始化对象的参数不仅可以是字符串，还可以是网页的URL，这时可以将URL作为参数传入初始化对象。

具体代码如下所示：

```python
from pyquery import PyQuery as pq


doc = pq('https://www.baidu.com', encoding='utf-8')
print(doc)
print(type(doc))
print(doc('title'))
```

试着运行上面的代码你会发现，我们成功的获取到了百度的`title`节点和网页信息。

PyQuery对象会先请求这个URL，然后用得到的HTML内容完成初始化，这其实就相当于网页源代码以字符串的形式传递给初始化对象。

因此，还可以这样写代码：

```python
from pyquery import PyQuery as pq
import requests


url = 'https://www.baidu.com'
doc = pq(requests.get(url).content.decode('utf-8'))
print(doc)
print(type(doc))
print(doc('title'))
```

运行结果与上面那段代码的运行结果是一致的。

- **文件初始化**

除了传递URL以外还可以传递本地的文件名，此时只要传递本地文件名，此时将参数指定为filename即可。

具体代码如下所示：

```python
from pyquery import PyQuery as pq


doc = pq(filename='baidu.html')
print(doc)
print(type(doc))
print(doc('title'))
```

以上三种初始化的方式都是可以的，当然最常用的初始化方式还是以字符串的形式传递。

## 基本CSS选择器

```python
html = '''
<div id="container">
    <ul class="list">
        <li class="item-0">first-item</li>
        <li class="item-1"><a href="link2.html">second item</a></li>
        <li class="item=-0 active"><a href="link3.html"><span class=""bold>third item</span></a></li>
        <li class="item-1 active"><a href="link4.html">fourth item</a></li>
        <li class="item-0"><a href="link5.html">fifth item</a></li>        
    </ul>
</div>
'''

from pyquery import PyQuery as pq


doc = pq(html)
print(doc('#container .list li'))
print(type(doc('#container .list li')))

```

初始化PyQuery对象之后，传入CSS选择器`#container .list li`将所有符合条件的节点输出，并且运行上面的代码之后你会发现它的类型依然还是PyQuery类型。

## 查找节点

下面介绍一些常用的查询函数，这些函数与jQuery函数的用法是完全相同的。

- **子节点**

查找子节点时需要用到`find()`方法，并传入的参数是CSS选择器，以前面的html为例子。

```python
from pyquery import PyQuery as pq


doc = pq(html)
print(doc.find('li'))
print(type(doc.find('li')))
```

调用`find()`方法，将节点名称`li`传入该方法，获取所有符合条件的内容。类型依然还是PyQuery。

当然我们还可以这样写：

```python
from pyquery import PyQuery as pq


doc = pq(html)
items = doc('.list')
print(type(items))
lis = items.find('li')
print(type(lis))
print(lis)
```

首先先选取class为`list`的节点，然后调用`find()`方法，传入CSS选择器，选取内部的``li`节点，最后打印输出。

其实`find()`方法是查找所有的子孙节点，要获取所有的子节点可以调用`chirdren()`方法。具体代码如下所示：

```python
from pyquery import PyQuery as pq


doc = pq(html)
items = doc('.list')
lis = items.children()
print(lis)
print(type(lis))
```

如果想要筛选子节点中符合条件的节点，可以向`chirdren()`方法传入CSS选择器。具体代码如下所示：

```python
from pyquery import PyQuery as pq


doc = pq(html)
items = doc('.list')
lis = items.children('.active')
print(lis)
print(type(lis))
```

试着运行上面的代码你会发现，这里已经成功获取到了class为`active`的节点。

- **父节点**

我们可以调用`parent()`方法来获取某个节点的父节点。

```python
html = '''
<div id="container">
    <ul class="list">
        <li class="item-0">first-item</li>
        <li class="item-1"><a href="link2.html">second item</a></li>
        <li class="item=-0 active"><a href="link3.html"><span class=""bold>third item</span></a></li>
        <li class="item-1 active"><a href="link4.html">fourth item</a></li>
        <li class="item-0"><a href="link5.html">fifth item</a></li>        
    </ul>
</div>
'''

from pyquery import PyQuery as pq


doc = pq(html)
items = doc('.list')
container = items.parent()
print(container)
print(type(container))
```

先对上面的代码做简要的说明：

首先选取class为`list`的节点，然后再调用`parent()`方法得到其父节点，其类型依然还是PyQuery类型。

这里的父节点是直接父节点，但是如果要获取祖父节点，可以调用`parents()`方法。

```python
html = '''
<div class="wrap">
    <div id="container">
        <ul class="list">
            <li class="item-0">first-item</li>
            <li class="item-1"><a href="link2.html">second item</a></li>
            <li class="item=-0 active"><a href="link3.html"><span class=""bold>third item</span></a></li>
            <li class="item-1 active"><a href="link4.html">fourth item</a></li>
            <li class="item-0"><a href="link5.html">fifth item</a></li>        
        </ul>
    </div>

</div>

'''

from pyquery import PyQuery as pq


doc = pq(html)
items = doc('.list')
container = items.parents()
print(container)
print(type(container))
```

运行上面的代应为码之后，你会发现这里输出的内容有四个，因为class为`list`节点的祖父节点有四个，分别是：container、wrap、body、html。在初始化对象的时候已经添加上了body和html节点。

- **兄弟节点**

除了可以获取到父节点和子节点之外，还可以获取到兄弟节点。如果需要获取兄弟节点，可以调用`siblings()`方法。

具体代码如下所示：

```python
html = '''
<div class="wrap">
    <div id="container">
        <ul class="list">
            <li class="item-0">first-item</li>
            <li class="item-1"><a href="link2.html">second item</a></li>
            <li class="item-0 active"><a href="link3.html"><span class=""bold>third item</span></a></li>
            <li class="item-1 active"><a href="link4.html">fourth item</a></li>
            <li class="item-0"><a href="link5.html">fifth item</a></li>        
        </ul>
    </div>

</div>

'''

from pyquery import PyQuery as pq


doc = pq(html)
items = doc('.list .item-0.active')
print(items.siblings())
```

这里首先选取类为`.item-0.active`的节点，再调用`siblings()`方法获取到该节点的兄弟节点。

试着运行上面的代码，你会发现获取到其他四个兄弟节点。

## 遍历

通过上面的代码可以观察到，pyquery的选择结果可能是多个节点，也可能是单个节点，类型都是PyQuery类型，并没有向Beautiful Soup那样的列表。

对于单个节点来说，可以直接打印输出，也可以直接转成字符串。

```python
from pyquery import PyQuery as pq


doc = pq(html)
items = doc('.list .item-0.active')
print(items)
print(str(items))
print(type(items))
```

对于多个节点，可以通过调用`item()`方法，将获取的内容转换成生成器类型，在通过遍历的方式输出。

具体代码如下所示：

```python
from pyquery import PyQuery as pq


doc = pq(html)
lis = doc('li').items()
print(lis)
for li in lis:
    print(li, type(li))
```

运行上面的代码，你会发现输出变量`lis`的结果是生成器，因此可以遍历输出。

## 获取信息

一般来说，在网页里面我们需要获取的信息有两类：一类是文本内容，另一类是节点属性值。

- **获取属性**

获取到某个PyQuery类型的节点之后，就可以通过`attr()`方法来获取属性。

具体代码如下所示：

```python
from pyquery import PyQuery as pq


doc = pq(html)
a = doc('.list .item-0.active a')
print(a.attr('href'))
```

先获取class为`list`下面的class为`item-0 active`的节点下的`a`节点，这时变量`a`是PyQuery类型，再调用`attr()`方法并传入属性值`href`。

当然也可以通过调用attr属性来获取属性。

```python
print(a.attr.href)
```

你会发现输出结果与上面的代码是一样的。

当然，我们也可以获取到所有`a`节点的属性，具体代码如下所示：

```python
html = '''
<div class="wrap">
    <div id="container">
        <ul class="list">
            <li class="item-0">first-item</li>
            <li class="item-1"><a href="link2.html">second item</a></li>
            <li class="item-0 active"><a href="link3.html"><span class=""bold>third item</span></a></li>
            <li class="item-1 active"><a href="link4.html">fourth item</a></li>
            <li class="item-0"><a href="link5.html">fifth item</a></li>        
        </ul>
    </div>

</div>

'''

from pyquery import PyQuery as pq


doc = pq(html)
a = doc('a').items()
for item in a:
    print(item.attr('href'))
```

但是如果代码这样写：

```python
from pyquery import PyQuery as pq


doc = pq(html)
a = doc('a')
print(a.attr('href'))
```

运行上面的代码之后，你会发现只获取到第一个`a`节点的`href`属性。

所有这个是需要注意的地方！！

- **提取文本**

提取文本与提取属性的逻辑是一样的，首先获取到class为PyQuery的节点，再调用`text()`方法获取文本。

首先来获取一个节点的文本内容。具体代码如下所示：

```python
html = '''
<div class="wrap">
    <div id="container">
        <ul class="list">
            <li class="item-0">first-item</li>
            <li class="item-1"><a href="link2.html">second item</a></li>
            <li class="item-0 active"><a href="link3.html"><span class=""bold>third item</span></a></li>
            <li class="item-1 active"><a href="link4.html">fourth item</a></li>
            <li class="item-0"><a href="link5.html">fifth item</a></li>        
        </ul>
    </div>

</div>

'''

from pyquery import PyQuery as pq


doc = pq(html)
a = doc('.list .item-0.active a')
print(a.text())
```

试着运行上面的代码你会发现成功获取`a`节点的文本内容。

接下来我们就来获取多个`li`节点的文本内容。

具体代码如下所示：

```python
html = '''
<div class="wrap">
    <div id="container">
        <ul class="list">
            <li class="item-0">first-item</li>
            <li class="item-1"><a href="link2.html">second item</a></li>
            <li class="item-0 active"><a href="link3.html"><span class=""bold>third item</span></a></li>
            <li class="item-1 active"><a href="link4.html">fourth item</a></li>
            <li class="item-0"><a href="link5.html">fifth item</a></li>        
        </ul>
    </div>

</div>

'''

from pyquery import PyQuery as pq


doc = pq(html)
items = doc('li')
print(items.text())
```

运行上面的代码，你会发现该代码成功获取到了所有节点名称为`li`的文本内容，中间用空格隔开。

如果你想要一个一个获取，那还是少不了生成器，具体代码如下所示：

```python
from pyquery import PyQuery as pq


doc = pq(html)
items = doc('li').items()
for item in items:
    print(item.text())
```

## 节点操作

pyquery提供了一系列方法对节点进行动态修改，比如为某个节点添加一个class，移除某个节点，这些操作有时会为提取信息带来便利。

- **add_class和remove_class**

```python
html = '''
<div class="wrap">
    <div id="container">
        <ul class="list">
            <li class="item-0">first-item</li>
            <li class="item-1"><a href="link2.html">second item</a></li>
            <li class="item-0 active"><a href="link3.html"><span class=""bold>third item</span></a></li>
            <li class="item-1 active"><a href="link4.html">fourth item</a></li>
            <li class="item-0"><a href="link5.html">fifth item</a></li>        
        </ul>
    </div>

</div>

'''

from pyquery import PyQuery as pq


doc = pq(html)
li = doc('.list .item-0.active')
print(li)
li.remove_class('active')
print(li)
li.add_class('active')
print(li)
```

运行结果如下所示：

```
<li class="item-0 active"><a href="link3.html"><span class="" bold="">third item</span></a></li>
            
<li class="item-0"><a href="link3.html"><span class="" bold="">third item</span></a></li>
            
<li class="item-0 active"><a href="link3.html"><span class="" bold="">third item</span></a></li>
```

上面有三段输出内容，首先先获取一个`li`节点，然后再删除`active`类属性，第三段代码是添加`active`类属性。

## 伪类选择器

CSS选择器之所以强大，还有一个很重要的原因，那就是它可以支持多种多样的伪类选择器，例如选择第一个节点、最后一个节点、奇偶数节点、包含某一文本的节点。

```python
html = '''
<div class="wrap">
    <div id="container">
        <ul class="list">
            <li class="item-0">first-item</li>
            <li class="item-1"><a href="link2.html">second item</a></li>
            <li class="item-0 active"><a href="link3.html"><span class=""bold>third item</span></a></li>
            <li class="item-1 active"><a href="link4.html">fourth item</a></li>
            <li class="item-0"><a href="link5.html">fifth item</a></li>        
        </ul>
    </div>

</div>

'''

from pyquery import PyQuery as pq


doc = pq(html)
li = doc('li:first-child')	# 第一个li节点
print(li)
li = doc('li:last-child')	# 最后一个li节点
print(li)
li = doc('li:nth-child(2)')	# 第二个位置的li节点
print(li)
li = doc('li:gt(2)')	# 第三个之后的li节点
print(li)
li = doc('li:nth-child(2n)')	# 偶数位置的li节点
print(li)
li = doc('li:contains(second)')	# 包含second文本的li节点
print(li)
```

至此，关于pyquery的所有内容都讲完了，接下来就进入实战了，光说不练肯定是不行的，只有通过实战才能正真学会刚刚所学会的知识。

# 实战

本次我带来的实战内容是爬取猫眼电影的TOP100的排行榜及评分情况。

## 准备

**工欲善其事，必先利其器**。首先，我们要准备几个库：pyquery、requests。

安装过程如下：

```
pip install pyquery
pip install requests
```

## 前言

寒假又到来了，小伙伴们准备怎么过呢？

在大冬天里，躲在被窝刷剧是最舒服的，好怀念当年的生活啊~

所以今天就来爬取猫眼电影的TOP100排行榜，为冬眠做好准备。

网站链接：

`https://maoyan.com/board/4`

## 需求分析与功能实现

### 获取电影名称

![](https://routing-ospf.oss-cn-beijing.aliyuncs.com/image-20210117140615861.png)

从上图可以看到我们需要的信息藏在class为`board-item-main`的`div`标签下的`a`标签内，因此我们需要获取其文本信息。

核心代码如下所示：

```python
movie_name = doc('.board-item-main .board-item-content .movie-item-info p a').text()
```

### 获取主演信息

![](https://routing-ospf.oss-cn-beijing.aliyuncs.com/image-20210117141318141.png)

从上图可以看到，主演的信息位于`board-item-main`的子节点`p`标签内，因此我们可以这样获取主演信息。

核心代码如下所示：

```python
p = doc('.board-item-main .board-item-content .movie-item-info')
star = p.children('.star').text()
```

### 获取上映时间

从前面的图片也可以看到，上映时间的信息与主演信息的节点是兄弟节点，所以我们可以这样写代码。

```python
p = doc('.board-item-main .board-item-content .movie-item-info')
time = p.children('.releasetime').text()
```

### 获取评分

要获取每一部电影的评分相对要复杂一些，为什么这样说呢？我们来看下面的图片。

![](https://routing-ospf.oss-cn-beijing.aliyuncs.com/image-20210117142657860.png)

从上面的图片可以看到，整数部分与小数部分被分割了成了两部分。因此需要分别获取两部分的数据，在进行拼接即可。

核心代码如下所示：

```python
score1 = doc('.board-item-main .movie-item-number.score-num .integer').text().split()
score2 = doc('.board-item-main .movie-item-number.score-num .fraction').text().split()
score = [score1[i]+score2[i] for i in range(0, len(score1))]
```

### 关于翻页

打开网页的时候，你会发现榜单一共有10页，每一页的URL都不相同，那该怎么办呢？总不能每一次都手动更换URL地址吧。

先来观察前四页的URL地址吧。

```
https://maoyan.com/board/4	# 第一页
https://maoyan.com/board/4?offset=10	# 第二页
https://maoyan.com/board/4?offset=20	# 第三页
https://maoyan.com/board/4?offset=30	# 第四页
```

观察完之后，我想不需要我过多叙述它的特点了吧。

接下来我们就可以构建每一页的URL地址了，具体代码如下所示：

```python
    def get_url(self, page):
        url = f'https://maoyan.com/board/4?offset={page}'
        return url
    if __name__ == '__main__':
    maoyan = MaoYan()
    for page in range(10):
        url = maoyan.get_url(page*10)
```

## 结果展示

![](https://routing-ospf.oss-cn-beijing.aliyuncs.com/image-20210117144210588.png)

# 最后

本次分享到就此结束，如果你从开头读到这里，想必文章对你是有所帮助的，这也是我分享知识的初衷。

没有什么是可以一蹴而就的，生活如此，学习亦是如此！

**路漫漫其修远兮，吾将上下而求索**。

我是**啃书君**，一个专注于学习的人。**你懂的越多，你不懂的越多**，更多精彩内容我们下期再见！	



















































