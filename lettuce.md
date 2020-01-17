# python + lettuce 搭建自动化测试 BDD框架

## python

[python官网](https://www.python.org/)
自取地址，安装过程不再多加阐述

```
 $ python -version
 

```

## lettuce
 基于python的BDD自动化测试框架，和cucumber妥妥表兄弟
```
 $ pip install lettuce_webdriver
 $ pip install nose
 $ pip install lettuce

```
```
BDD语法

Given
When
And
Then
```
## 目录结构

```
--tests/feature/login.feature
------/step_definitions/steps.py   （步骤定义文件）
-----/support/run.py  (驱动文件)

python 语法坑：
#coding:utf-8
放在顶部
```

login.feature

```
Feature: login   
  
Scenario: login in the   
  Given I go to "http://121.36.8.180/login"
     When I set the id "modal_uname_input" with "vip000000081"
     And I set the id "modal_upass_input" with "123456"  
     And I click id "startLogin" with baidu once
     Then I close browser
 ```
steps.py
```
#coding=utf-8
#!/usr/bin/python
# -*- coding: <encoding name> -*-

from lettuce import *  
from lettuce_webdriver.util import assert_false  
from lettuce_webdriver.util import AssertContextManager  
  
def input_frame(browser, attribute):
    xpath = "//input[@id='%s']" % attribute  
    elems = browser.find_elements_by_xpath(xpath)  
    return elems[0] if elems else False  

def click_button(browser,attribute):
    xpath = "//button[@id='%s']" % attribute
    elems = browser.find_elements_by_xpath(xpath)
    return elems[0] if elems else False


#定位输入框输入关键字
@step('I set the id "(.*?)" with "(.*?)"')
def baidu_text(step,field_name,value):
    with AssertContextManager(step):  
        text_field = input_frame(world.browser, field_name)  
        text_field.clear()  
        text_field.send_keys(value)

#点击按钮
@step('I click id "(.*?)" with baidu once')
def baidu_click(step,field_name):
    with AssertContextManager(step):
        click_field = click_button(world.browser,field_name)
        click_field.click()

#关闭浏览器
@step('I close browser')
def close_browser(step):
    world.browser.quit()
```

run.py
```
#coding=utf-8
#!/usr/bin/python
# -*- coding: <encoding name> -*-

from lettuce import before, world  
from selenium import webdriver  
import lettuce_webdriver.webdriver
from PIL import ImageGrab  
 
@before.all  
def setup_browser():  
    world.browser = webdriver.Chrome('F:/downloads/chromedriver_win32/chromedriver.exe')

```

```
$lettuce              查看运行结果，需要进入tests目录下
```