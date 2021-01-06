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

细心的读者朋友应该会发现我上面的代码片段中标签**ul**是没有闭合的，但是运行之后你会发现运行结果是闭合的，并且还自动添加了**html**和**body**标签。

这是因为我们调用了**tostring( )**方法帮助我们将HTML文本进行修正，但是要注意的是**tostring( )**方法`返回的结果是byte类型`，因此这里调用了tostring( )方法即可输出修正后的HTML代码。使用decode( )方法可以将byte类型的数据转成str类型的数据。

当然，etree这个模块也可以直接读取文本文件进行解析，具体代码如下所示：

```python
from lxml import etree


html = etree.parse('./test.html', etree.HTMLParser())
result = etree.tostring(html)
print(result.decode('utf-8'))
```

其中文件test.html的内容就是上面示例的HTML代码。

## 获取所有的节点

我们一般会使用 // 开头的Xpath规则来选取所有符合要求的节点，假如我需要获取所有的节点，示例代码如下所示：

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

上述内容所描述的是xpath的在爬虫应用中常见使用方法，如果各位小伙伴想要继续深入学习的话，可以参考w3c进行学习，网址如下：

```
https://www.w3school.com.cn/xpath/xpath_syntax.asp
```



# 实战

上面的内容是描述xpath的使用语法，建议大家要花一个小时左右的时间去练习。

那么接下来就带大家进入实战演练了，乘热打铁是最好的学习方式。

今天我带来的内容就是爬取`必应壁纸`。

# 准备工作

**工欲善其事，必现利其器**。玩爬虫也是同样的道理。

首先，安装好两个库：**lxml与requests**。

```
pip install lxml
pip install requests
```

# 需求分析

爬取的网址：`https://bing.ioliu.cn/`

## 抓包分析

首先打开开发者工具，随便点击一张图片进入它的高清大图，点击network进行抓包，在点击图片的下载按钮。

![](https://routing-ospf.oss-cn-beijing.aliyuncs.com/image-20201231214939778.png)

点击下载按钮之后，你会发现，浏览器向图中的网址发起了请求，点击进去之后发现这个就是高清图片的链接地址。

从而我们的第一个需求就是获取所有图片的链接地址。

## 获取图片链接

为什么要获取图片链接呢？

首先，你思考一下，每一张图片你都要点击下载按钮来将图片保存到本地吗？如果你不懂爬虫那当然没有办法了。但是，我们懂爬虫的人还会这么干吗？

既然每一次点击下载按钮，浏览器都是向对应的高清大图发起请求，那么也就是说我们可以获取到所有的图片链接，然后利用Python模拟浏览器向这些链接发起请求，即可下载这些图片。

链接如下：

```
https://h2.ioliu.cn/bing/LoonyDook_ZH-CN1879420705_1920x1080.jpg?imageslim
```



## 关于翻页

打开网页之后，你会发现起码有100页的图片。那这100页的图片怎么样获取呢？

很简单，依然还是先分析每一页的URL地址，看看有没什么变化规律。

```
# 第二页
https://bing.ioliu.cn/?p=2
# 第三页
https://bing.ioliu.cn/?p=3
```

其实看到上面的URL变化之后，我想你也应该明白了变化的规律了吧。

# 功能实现

## 构造每一页的链接

其实就是实现简单的翻页功能。

具体代码示例如下所示：

```python
def get_page_url():
    page_url = []
    for i in range(1,148):
        url = f'https://bing.ioliu.cn/?p={i}'
        page_url.append(url)
    return page_url
```

上面代码的功能是构造每一页的链接。将链接保存在page_url中。

## 获取每一页中的图片链接

![](https://routing-ospf.oss-cn-beijing.aliyuncs.com/image-20210101005956495.png)

在上图中你会发现，图片的链接就藏在了`data-progressive`里面，这不就是img标签的属性吗？有何难？

但是细心的朋友就会发现，这个链接和我们最开始抓包的链接是不一样的，到底哪里不一样呢？

我们来具体看看

```
https://h2.ioliu.cn/bing/LoonyDook_ZH-CN1879420705_1920x1080.jpg?imageslim
http://h2.ioliu.cn/bing/LoonyDook_ZH-CN1879420705_640x480.jpg?imageslim
```

发现了吗？分辨率是不一样的。其他都相同的，那只要将分辨率替换掉就可以了呀。

具体代码如下所示：

```python
def get_img_url(urls):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36'
    }
    img_urls = []
    count = 1
    for url in urls[:3]:
        time.sleep(5)
        text = requests.get(url, headers=headers).content.decode('utf-8')
        html = etree.HTML(text)
        img_url = html.xpath('//div[@class="item"]//img/@data-progressive')
        img_url = [i.replace('640x480', '1920x1080') for i in img_url]
        print(f'正在获取第{count}页链接')

        img_urls.extend(img_url)
        count += 1
    return img_urls
```

上面的代码是获取每一页的图片链接，将链接保存在img_urls中。

## 保存图片

```python
 def save_img(self, img_urls):

        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36'
        }
        count = 1
        
        for img_url in img_urls:
            content = requests.get(img_url, headers=headers).content
            print(f'正在下载第{count}张')
            with open(f'../image/{count}.jpg', 'wb') as f:
                f.write(content)
            count += 1
```

保存图片的代码还是比较简单的，可以将获取到的所有图片链接作为参数传进来，进行逐个访问，即可。

# 最后

本次分享到这里就结束了，如果你读到了这里，那说明本篇文章对你还是有所启发的，这也是我分享的初衷。

**路漫漫其修远兮，吾将上下而求索**。

我是**啃书君**，一个专注于学习的人，**你懂的越多，你不懂的越多**。更多精彩内容，我们下期再见！



