# -*- coding:utf-8 -*-
# @Author  :'Dennie'
# @Time    : 2017/1/11 23:51
# @File    : TestCase.py

import unittest
from Pages import pages
import logging,time

def wLogging(log):
	"""
	Record Run Log.
	:param log:
	:return:
	"""
	path = './test_Result/Test_logs/'
	now = time.strftime("%Y-%m-%d_%H-%M-%S",time.localtime())
	filename = '-Tests_log.log'
	logging.basicConfig(level=logging.DEBUG,
						format='%(asctime)s wLog: %(levelname)s [** %(message)s **]',
						datefmt='%Y-%m-%d %H:%M:%S',
						filename=path + now + filename,
						filemode='w')
	logging.info(log)

class Test_Amazon_Functions(unittest.TestCase):
	"""
	Here is test case.
	"""
	def setUp(self):
		"""
		Init.
		"""
		wLogging('[--------------Begin Init--------------]')
		self.pages = pages.MainPage()
		wLogging('[--------------End   Init--------------]')

	@unittest.skip#Skip this case
	def test_addStatus(self):
		"""
		Test and verify that text "商品已加入购物车" appears.
		"""
		wLogging('[--------------Begin run case addStatus--------------]')
		add_Status = self.pages.bool_Display_status("id=huc-v2-order-row-confirm-text")
		self.assertTrue(add_Status)
		wLogging('[--------------This test case ends--------------]')

	def test_bookPrice(self):
		"""
		Test and verify that book price is "20.40".
		"""
		wLogging('[--------------Begin run case bookPrice--------------]')
		book_Price = self.pages.get_Price("""xpath=.//*[@id='hlb-subcart']/div[@class='a-row a-spacing-micro']/span/span[@class='a-color-price hlb-price a-inline-block a-text-bold']""")
		self.assertEqual(book_Price,'20.40')
		wLogging('[--------------This test case ends--------------]')

	def tearDown(self):
		"""
		End test, quit the driver and close all the windows.
		"""
		self.pages.quit()