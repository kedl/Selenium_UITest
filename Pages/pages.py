# -*- coding:utf-8 -*-
# @Author  :'Dennie'
# @Time    : 2017/1/12 00:16
# @File    : pages.py

from base import base

class MainPage(base.base):

	def __init__(self):
		"""
		Init browser type and set url address
		:return:None
		"""
		driver = base.base('chrome')
		self.driver = driver
		self.url = "https://www.amazon.cn/"

	def bool_Display_status(self, element):
		"""
		Verify that the element is in the current page.
		:return: True or False
		"""
		self.driver.get(self.url)
		self.driver.max_window()
		self.driver.find_element("id=twotabsearchtextbox")
		self.driver.send_keys("id=twotabsearchtextbox",u"软件测试")
		self.driver.click("class=nav-input")
		self.driver.Open_new_window("""xpath=.//*[@id='result_0']/div/div[@class='a-row a-spacing-mini']/div[@class='a-row a-spacing-none']/a""")
		self.driver.click("id=add-to-cart-button")
		return self.driver.get_Display(element)

	def get_Price(self, element):
		"""
		Get the price.
		:return: str Price
		"""
		self.driver.get(self.url)
		self.driver.max_window()
		self.driver.find_element("id=twotabsearchtextbox")
		self.driver.send_keys("id=twotabsearchtextbox",u"软件测试")
		self.driver.click("class=nav-input")
		self.driver.Open_new_window("""xpath=.//*[@id='result_0']/div/div[@class='a-row a-spacing-mini']/div[@class='a-row a-spacing-none']/a""")
		self.driver.click("id=add-to-cart-button")
		ele_text = self.driver.get_Text(element)
		price = ele_text[2:]
		return price