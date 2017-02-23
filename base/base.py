# -*- coding:utf-8 -*-
# @Author  :'Dennie'
# @Time    : 2017/1/11 20:57
# @File    : base.py
# @Python Version: 3.5


'''
This is a simpler automated testing,based on selenium webdriver2.0.
'''

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


class base(object):
    """
    Run class initialization method, the default is proper to driver the Chrome browser.
    Of course, you can also pass parameter for other browser, such as Firefox browser for the 'firefox', the Internet Explorer browser for 'ie'.
    """

    def __init__(self, browser='chrome'):
        if browser == 'chrome':
            driver = webdriver.Chrome()
        elif browser == 'firefox':
            driver = webdriver.Firefox()
        elif browser == 'ie':
            driver = webdriver.Ie()
        try:
            self.driver = driver
        except Exception:
            raise NameError(
                "Not found this browser,You can enter 'firefox', 'chrome' or 'ie'.")

    def get(self, url):
        """
        Open url,same as get.
        :param url:Input a url to get.
        :return: None

        Usage:
        driver.get("https://www.baidu.com")
        """
        self.driver.get(url)

    def max_window(self):
        """
        Set browser window maximized.
        :return:None

        Usage:
        driver.max_window()
        """
        self.driver.maximize_window()

    def set_window_size(self, wide, high):
        """
        Set browser window wide and high.
        :param wide:
        :param high:
        :return: None

        Usage:
        driver.set_window_size(wide,high)
        """
        self.driver.set_window_size(wide, high)

    def wait(self, seconds):
        """
        Implicitly wait.All elements on the page.
        :param seconds:
        :return:None

        Usage:
        driver.wait(5)
        """
        self.driver.implicitly_wait(seconds)

    def find_element(self, element):
        """
        Judge element positioning way.
        :param element:
        :return:element

        Usage:
        driver.find_element("id=kw")
        """
        if "=" not in element:
            raise NameError("SyntaxError: invalid syntax, lack of '='.")

        idx = element.index('=')
        by = element[:idx]
        value = element[idx + 1:]

        if by == "id":
            return self.driver.find_element_by_id(value)
        elif by == "name":
            return self.driver.find_element_by_name(value)
        elif by == "class":
            return self.driver.find_element_by_class_name(value)
        elif by == "text":
            return self.driver.find_element_by_link_text(value)
        elif by == "xpath":
            return self.driver.find_element_by_xpath(value)
        elif by == "css":
            return self.driver.find_element_by_css_selector(value)
        else:
            raise NameError(
                "Please enter correct targeting elements,'id','name','class','text','xpath' or 'css'.")

    def wait_element(self, element, seconds=5):
        """
        Waiting for an element to display.
        :param element:
        :param seconds:int
        :return:None
        """
        if "=" not in element:
            raise NameError("SyntaxError: invalid syntax, lack of '='.")

        idx = element.index('=')
        by = element[:idx]
        value = element[idx + 1:]

        if by == 'id':
            WebDriverWait(self.driver, seconds, 10).until(
                EC.presence_of_element_located((By.ID, value)))
        elif by == 'name':
            WebDriverWait(self.driver, seconds, 10).until(
                EC.presence_of_element_located((By.NAME, value)))
        elif by == 'class':
            WebDriverWait(self.driver, seconds, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, value)))
        elif by == 'text':
            WebDriverWait(self.driver, seconds, 10).until(
                EC.presence_of_element_located((By.LINK_TEXT, value)))
        elif by == 'xpath':
            WebDriverWait(self.driver, seconds, 10).until(
                EC.presence_of_element_located((By.XPATH, value)))
        elif by == 'css':
            WebDriverWait(self.driver, seconds, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, value)))
        else:
            raise NameError(
                "Please enter the correct targeting elemens,'id','name','class','text','xpath' or 'css'.")

    def send_keys(self, element, text):
        """
        Operation input content after clear.
        :param element:
        :param text:str
        :return:
        Usage:
        driver.send_keys("id=kw","test")
        """
        self.wait_element(element)
        self.find_element(element).clear()
        self.find_element(element).send_keys(text)

    def click(self, element):
        """

        :param element:
        :return:
        """
        self.wait_element(element)
        self.find_element(element).click()

    def get_attribute(self, element, attribute):
        """
        Gets the value of an element attribute.
        :param element:
        :param attribute:str
        :return:attribute value
        Usage:
        driver.get_attribute("id=kw","attribute")
        """
        self.wait_element(element)
        return self.find_element(element).get_attribute(attribute)

    def get_screenshot(self, file_path):
        """
        Get the current window screenshot.
        :param file_path:
        :return:
        """
        self.driver.get_screenshot_as_file(file_path)

    def close(self):
        """
        Close the window.
        :return:
        """
        self.driver.close()

    def quit(self):
        """
        Quit the driver and close all the windows.
        :return:None
        """
        self.driver.quit()

    def Open_new_window(self, element):
        """
        Open the new window and switch the handle to the newly opened window.
        :param element:
        :return:None
        Usage:
        driver.open_new_window(id=testID)
        """
        current_windows = self.driver.current_window_handle
        self.find_element(element).click()
        all_handles = self.driver.window_handles
        for handle in all_handles:
            if handle != current_windows:
                self.driver.switch_to.window(handle)

    def get_Title(self):
        """
        Get window title.
        :return:title
        """
        return self.driver.title

    def get_Display(self, element):
        """
        Gets the element to display.
        :param element:
        :return: True or False
        """
        self.wait_element(element)
        return self.find_element(element).is_displayed()

    def get_Text(self, element):
        """
        Get element text information.
        :param element:
        :return: str:ele_Text
        """
        self.wait_element(element)
        ele_Text = self.find_element(element).text
        return ele_Text
