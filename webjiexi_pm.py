# -*- coding:utf-8 -*-


"""
#1.网页解析方式
1）xpath(简单）
2）正则（最难）
3)css(需要懂网页css）
4）bs4（比xpath难一点点）

2.xpath的基本用法
1）环境准备：
    火狐浏览器
    firebug
    firepath
2）基本操作
//元素标签名
例如：//div，查找网页内所有的div

//元素标签名[@属性名=‘内容’]
例如：//div[@class='box']查找class为box的div

//元素标签名[第几个]
例如：//[@class='box'][2],查找符合条件的第二个div

//元素1/元素2/元素3...
例如：//ul/li/div/a/img,查找ul下的div下的a下的img标签

//元素1/@属性名
例如：//ul/li/div/a/img/@src,查找ul下的li下的div下a下img的src属性

//元素/text()
例如://a/text(), 获取a标签之间的文本(一级文本)

//元素//text()
例如://div[@class='box']//text(), 获取class为div下的所有文本

//li[contains(@class,'')]
//元素[contains(@属性名,'相关属性')]
例如：//div[contains(@class,'zhangsan')] 查找class中包含张三的div

//*[@属性='值']
例如://*[@name='lisi']查找所有name为lisi的元素

"""

