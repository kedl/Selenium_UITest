# -*- coding:utf-8 -*-
# @Author  :'Dennie'
# @Time    : 2017/1/12 14:29
# @File    : runTests.py

import unittest
import HTMLTestRunner
from Test_Cases import TestCase
import time

if __name__ == '__main__':
    """
    Run test case and write test result to file.
    """
    # suite = unittest.makeSuite(TestCase.Test_Amazon_Functions)
    suite = unittest.TestLoader().loadTestsFromTestCase(TestCase.Test_Amazon_Functions)
    path = './test_Result/Test_Reports/'
    filename = '-result.html'
    now = time.strftime("%Y-%m-%d_%H-%M-%S", time.localtime())
    fp = open(path + now + filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(
        fp, title=u'My tests', description=u'This is a report test')
    runner.run(suite)
    fp.close()
