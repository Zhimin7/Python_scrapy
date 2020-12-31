# 使用XPath

XPath，全称XML Path Language，即XML路径语言，它是在XML语言中查找信息的语言。它最初是用来搜寻XML文档的，但是它同样适用于HTML文档的搜索。

在上一篇文章中讲述了正则表达式的使用方法，正则表达式的难度还是比较大的，如果不花足够多的时间去做的话还是比较难的，所以今天就来分享比正则简单的内容，方便大家接下来的学习。

## XPath常用规则

XPath的规则是非常丰富的，本篇文章无法一次性全部概括，只能为大家介绍几个常用的规则。

|  表达式  |           描述           |
| :------: | :----------------------: |
| nodename |  选取此节点的所有子节点  |
|    /     | 从当前节点选取直接子节点 |
|    //    |  从当前节点选取子孙节点  |
|    .     |      选取当前子节点      |
|    ..    |   选取当前节点的父节点   |
|    @     |         选取属性         |

## 准备工作

在使用之前得先安装好lxml这个库，如果没有安装请参考下面的安装方式。

```python
pip install lxml
```

## 案例导入

现在通过实例来xpath对网页解析的过程

```python
from lxml import etree


text = '''
<div>
    <ul>
        <li class="item-0"><a href="link1.html">first-item</a></li>
        <li class="item-1"><a href="link2.html"></a>second-item</li>
        <li class="item-inactive"><a href="link3.html">third-item</a></li>
        <li class="item-1"><a href="link4.html">fourth-item</a></li>
        <li class="item-0"><a href="link5.html">fifith-item</a></li>
    

</div>
'''
html = etree.HTML(text)
result = etree.tostring(html)
print(result.decode('utf-8'))
```

这里首先通过lxml这个库导入etree这个模块，然后声明一段HTML文本，调用HTML类进行初始化，这就成功构造了xpath对象。

细心的读者朋友应该会发现我上面的代码片段中标签**ul**是没有闭合的，但是运行之后你会发现运行结果是闭合的，并且帮助我们添加了html和body标签。

这是因为我们调用了tostring( )方法帮助我们将HTML文本进行修正，但是要注意的是tostring( )方法返回的结果是byte类型，因此这里调用了tostring( )方法即可输出修正后的HTML代码。

当然，etree这个模块也可以直接读取文本文件进行解析，具体代码如下所示：

```python
from lxml import etree


html = etree.parse('./test.html', etree.HTMLParser())
result = etree.tostring(html)
print(result.decode('utf-8'))
```

其中文件test.html的内容就是上面示例的HTML代码。

## 获取所有的节点

我们一般会使用//开头的Xpath规则来选取所有符合要求的节点，假如我需要获取所有的节点，示例代码如下所示：

```python
from lxml import etree


html = etree.parse('./test.html', etree.HTMLParser())
result = html.xpath('//*')
print(result)
```

首先对上面的代码做简单的说明，这里的 * 代表匹配全部，所以所有的节点都会获取到，返回值是一个列表。

每个元素是Element类型，其中后面跟的就是节点的名称。

运行结果如下所示：

```
[<Element html at 0x1a0334c39c0>, <Element body at 0x1a0334c3a80>, <Element div at 0x1a0334c3ac0>, <Element ul at 0x1a0334c3b00>, <Element li at 0x1a0334c3b40>, <Element a at 0x1a0334c3bc0>, <Element li at 0x1a0334c3c00>, <Element a at 0x1a0334c3c40>, <Element li at 0x1a0334c3c80>, <Element a at 0x1a0334c3b80>, <Element li at 0x1a0334c3cc0>, <Element a at 0x1a0334c3d00>, <Element li at 0x1a0334c3d40>, <Element a at 0x1a0334c3d80>]

```

从上面的运行结果你会发现，html、body、div、ul、li等等节点。

## 获取指定节点

例如，在这里我要获取到所有的li节点，那该怎么办呢？其实很简单，具体代码示例如下所示：

```python
from lxml import etree


html = etree.parse('./test.html', etree.HTMLParser())
result = html.xpath('//li')
print(result)

```

通过上面的几个例子，不知道大家有没有明白节点的含义。

其实节点的含义你可以理解为当前的html文档开始的地方。

如果上面的代码你修改一段，变成这样：

```python
result = html.xpath('/li')
```

运行之后你会发现列表是空的，因为该文档的的子节点中没有 li 这个节点，li 是该文档的子孙节点，而该文档的子节点是html。

所以，你将代码这样修改：

```python
result = html.xpath('/html')
# 另一种写法
result = html.xpath('.')
```

运行之后你会惊喜的发现，成功获取到了html节点。

## 子节点与子孙节点

通过/或//即可查好元素的子节点或者是子孙节点，假如你想要选择 li 节点下的所有 a 节点可以这样实现，具体代码如下所示：

```python
from lxml import etree


html = etree.parse('./test.html', etree.HTMLParser())
result = html.xpath('//li/a')
print(result)
```

先对上面的代码做简要的说明：//li表示获取所有的li节点，/a表示获取 li 节点下的子节点 a 。

或者也可以这样写，你可以先获取到所有的 ul 节点，再获取 ul 节点下的所有**子孙节点** a 节点。

具体示例代码如下所示：

```python
from lxml import etree


html = etree.parse('./test.html', etree.HTMLParser())
result = html.xpath('//ul//a')	# 注意//a
print(result)

```

运行上面的代码你会发现结果是相同的。

## 获取父节点

通过上面的几个例子，想必应该知道何为子节点与子孙节点。那么如何寻找父节点呢？这里可以通过 .. 来实现。

比如，我现在要选中href属性为link4.html的a节点，然后再获取其父节点，再获取其class属性。看着内容好多，那就要一个一个来，不要着急。

具体代码示例如下所示：

```python
from lxml import etree


html = etree.parse('./test.html', etree.HTMLParser())
result = html.xpath('//a[@href="link4.html"]/../@class')
print(result)
```

运行结果

```python
['item-1']
```

## 属性的匹配

在选取数据的时候，可以使用@符号进行属性的过滤，比如：这里通过选取 li 标签属性class为item-0的节点，可以这样实现：

```python
from lxml import etree


html = etree.parse('./test.html', etree.HTMLParser())
result = html.xpath('//li[@class="item-0"]')
print(result)
```

你可以试着运行上面的代码，你会发现匹配到了两个正确的结果。

## 文本获取

在整个HTML文档中肯定会有很多的文本内容，有些恰恰是我们需要的，那么应该如何获取这些文本内容呢？

接下来可以尝试使用text( )方法获取节点中的文本。

具体代码实例如下所示：

```python
from lxml import etree


html = etree.parse('./test.html', etree.HTMLParser())
result = html.xpath('//li[@class="item-0"]/a/text()')
print(result)
```

试着运行上面的代码，你会发现，已经获取到了所有class属性为item-0的 li 节点下的文本。

## 获取标签属性值

在编写爬虫的过程中，很多时候我们需要的数据可能是属性值，那就要学会如何来获取我们想要的属性值了。

例如，我想要获取 li 节点下的a节点的所有href属性，具体代码示例如下所示：

```python
from lxml import etree


html = etree.parse('./test.html', etree.HTMLParser())
result = html.xpath('//li/a/@href')
print(result)
```

通过@href就获取到了该节点的href属性值，当然，它们都是以列表的形式返回。

## 属性多值的匹配

在编写前端代码的时候，有些节点为了方便可能就会存在多个值，那么就要使用contains函数了，例如：

```python
from lxml import etree

text = '''
<li class="li li-first"><a href="link.html">first item</a></li>

'''
html = etree.HTML(text)
result = html.xpath('//li[contains(@class, "li")]/a/text()')
print(result)

```



要是你说我怎么记得住这些函数，那好，还可以这样写。

具体代码示例如下：

```python
from lxml import etree

text = '''
<li class="li li-first"><a href="link.html">first item</a></li>

'''
html = etree.HTML(text)
result = html.xpath('//li[@class="li li-first"]/a/text()')
print(result)
```

看出区别了吗？

运行上面的两段代码，你会发现结果是一样的。

## 多属性匹配

另外，我们写写爬虫的时候会遇到另一种情况，那就是在一个标签内存在多个属性。那此时可以用and操作符来连接

具体代码示例如下所示：

```python
from lxml import etree

text = '''
<li class="li li-first" name="item"><a href="link.html">first item</a></li>

'''
html = etree.HTML(text)
result = html.xpath('//li[contains(@class, "li") and @name="item"]/a/text()')
print(result)
```

## xpath运算符的简单介绍

从上面的示例你应该知道了，and是xpath的运算符，xpath的运算符也是比较多的，那么接下来对xpath运算符做简单的介绍。

| 运算符 |                       描述                        |
| :----: | :-----------------------------------------------: |
|   or   |                        或                         |
|  and   |                        与                         |
|   \|   | 计算两个节点集，//li \| //a 获取li和a元素的节点集 |
|   +    |                       加法                        |
|   -    |                       减法                        |
|   *    |                       乘法                        |
|  div   |                       除法                        |
|   =    |                       等于                        |
|   !=   |                      不等于                       |
|   <    |                       小于                        |
|   >    |                       大于                        |
|   >=   |                     大于等于                      |
|   <=   |                     小于等于                      |
|  mod   |                     计算余数                      |

## 按序选择

有时候，我们编写爬虫的时候可能会匹配到几个相同的 li 节点，但是，我只需要第一个或者最后一个就可以了。那这时该怎么样处理那？

这时可以通过索引的方式，传入指定的索引，获取指定节点。

具体代码示例如下所示：

```python
from lxml import etree

text = '''
<div>
    <ul>
        <li class="item-0"><a href="link1.html">first-item</a></li>
        <li class="item-1"><a href="link2.html"></a>second-item</li>
        <li class="item-inactive"><a href="link3.html">third-item</a></li>
        <li class="item-1"><a href="link4.html">fourth-item</a></li>
        <li class="item-0"><a href="link5.html">fifith-item</a></li>
    </ul>

</div>
'''
html = etree.HTML(text)
# 获取第一个li节点
result = html.xpath('//li[1]/a/text()')
print(result)
# 获取最后一个li节点
result = html.xpath('//li[last()]/a/text()')
print(result)
# 获取位置小于3的li节点
result = html.xpath('//li[position()<3]/a/text()')
print(result)
# 获取倒数第三个li节点
result = html.xpath('//li[last()-2]/a/text()')
print(result)
```



# 最后

今天是2020的最后一天，希望各位小伙伴可以挣到更多的钱，没有脱单的小伙伴抓紧脱单，找到你的另一半，陪你共度一生。

**路漫漫其修远兮，吾将上下而求索**。

我是**啃书君**，一个专注于学习的人，**你懂的越多，你不懂的越多**。更多精彩内容我们下期再见！