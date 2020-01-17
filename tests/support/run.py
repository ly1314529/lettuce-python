#coding:utf-8

import unittest
import HTMLTestRunner


class DemoTest(unittest.TestCase):

    def test_one(self):
        print('第一条case')
    def test_two(self):
        print('第二条case')
#调整缩进后就会不执行main
if __name__ == '__main__':
    print("开始main")
    suite = unittest.TestSuite()
    suite.addTest(DemoTest('test_one'))
    suite.addTest(DemoTest('test_two'))

    filename = 'F:\\test.html'
    #这里之前w，一直报错，现在改成wb+，输出结果了，泪奔呀，搞了好长时间的
    fp = open(filename, 'wb+')
    #这里了引用写的是HtmlTestRunner，一直报错，找半天原因
    #runner = HTMLTestRunner.HTMLTestRunner(stream=fp, output='E:/test.html',report_title=u'test-results',
                                           #descriptions=u'第一个python unittest')
    #runner = HTMLTestRunner.HTMLTestRunner(stream=fp,report_title=u"test-results",descriptions=u"第一个python unittest")
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=u"百度测试报告", description=u"用例测试情况")

    runner.run(suite)

    fp.close()
        