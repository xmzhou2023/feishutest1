# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.common.exceptions import TimeoutException
from libs.common.time_ui import sleep
from libs.common.logger_ui import log
from libs.common.connect_sql import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

"""     值校验的各种方法     """

def value_assert_equal(a,b):
    try:
        assert a == b, log.warning("断言失败: 两值不等 | a:{} b:{}".format(a, b))
        log.info("断言成功: 两值相等 | a:{} b:{}".format(a, b))
    except Exception as e:
        pass

def value_assert_Notequal(a,b):
    try:
        assert a != b, log.warning("断言失败: 两值相等 | a:{} b:{}".format(a, b))
        log.info("断言成功: 两值不等 | a:{} b:{}".format(a, b))
    except Exception as e:
        pass

def value_assert_True(x):
    try:
        assert bool(x) is True, log.warning("断言失败: 该值不为True值 | x:{}".format(x))
        log.info("断言成功: 该值为True值 | x:{}".format(x))
    except Exception as e:
        pass

def value_assert_False(x):
    try:
        assert bool(x) is False, log.warning("断言失败: 该值不为False值 | x:{}".format(x))
        log.info("断言成功: 该值为False值 | x:{}".format(x))
    except Exception as e:
        pass

def value_assert_Is(a,b):
    try:
        assert a is b, log.warning("断言失败:  a 不是 b | a:{} b:{}".format(a, b))
        log.info("断言成功: a 是 b | a:{} b:{}".format(a, b))
    except Exception as e:
        pass

def value_assert_IsNot(a,b):
    try:
        assert a is not b, log.warning("断言失败: a 是 b | a:{} b:{}".format(a, b))
        log.info("断言成功: a 不是 b | a:{} b:{}".format(a, b))
    except Exception as e:
        pass

def value_assert_IsNone(x):
    try:
        assert x is None, log.warning("断言失败: 该值不为None | x:{}".format(x))
        log.info("断言成功: 该值为None | x:{}".format(x))
    except Exception as e:
        pass

def value_assert_IsNoneNot(x):
    try:
        assert x is not None, log.warning("断言失败: 该值为None | x:{}".format(x))
        log.info("断言成功: 该值不为None | x:{}".format(x))
    except Exception as e:
        pass

def value_assert_In(a,b):
    try:
        assert a in b, log.warning("断言失败: a 不包含 b | a:{} b:{}".format(a, b))
        log.info("断言成功: a 包含 b | a:{} b:{}".format(a, b))
    except Exception as e:
        pass

def value_assert_InNot(a,b):
    try:
        assert a not in b, log.warning("断言失败: a 包含 b | a: {} b:{}".format(a, b))
        log.info("断言成功: a 不包含 b | a: {} b: {}".format(a, b))
    except Exception as e:
        pass


def value_assert_Instance(a,b):
    try:
        assert isinstance(a,b), log.warning("断言失败: a: {} 类型：{}".format(a, b))
        log.info("断言成功: a: {} 类型： {}".format(a, b))
    except Exception as e:
        pass

def value_assert_IsInstanceNot(a,b):
    try:
        assert not isinstance(a,b), log.warning("断言失败: a: {} 类型：{}".format(a, b))
        log.info("断言成功: a: {} 类型：{}".format(a, b))
    except Exception as e:
        pass

"""     页面元素校验的方法     """

class DomAssert(object):

    def __init__(self, driver):
        self.driver = driver
        self.timeout = 20
        self.wait = WebDriverWait(self.driver, self.timeout)

    def assert_att(self, word):
        """页面是否存在某文字"""
        try:
            att = self.driver.find_element(By.XPATH,'//*[contains(text(),{})]'.format(word)).text
            assert word in att, log.warning("断言失败：页面不存在该标识 | 关键字:{}".format(word))
            log.info("断言成功：页面存在该标识 | 关键字:{}".format(word))
        except Exception as e:
            return e

    def assert_title(self, word):
        """当前页面标题是否是指定title"""
        try:
            att = self.driver.switch_to.window(self.driver.window_handles[-1])
            assert word in att.title, log.warning("断言失败：标题为预期不符 | 标题:{}".format(word))
            log.info("断言成功：标题为预期一致 | 标题:{}".format(word))
        except Exception as e:
            return e

    def assert_url(self, word):
        """当前页面是不是指定url"""
        try:
            att = self.driver.current_url
            assert word in att, log.warning("断言失败：URL为预期不一致 | URL:{}".format(word))
            log.info("断言成功：URL为预期一致 | URL:{}".format(word))
        except Exception as e:
            return e

    def assert_page_source(self, word):
        """当前断言页面不包含not found"""
        try:
            assert word not in self.driver.page_source, log.warning("断言失败：页面包含此标识 | 标识:{}".format(word))
            log.info("断言成功：页面不包含此标识| 标识:{}".format(word))
        except Exception as e:
            return e

"""     数据库断言     """

class SQLAssert(object):

    def __init__(self, driver):
        self.driver = driver
        self.timeout = 20
        self.wait = WebDriverWait(self.driver, self.timeout)

    def assert_sql(self, word, sql):
        """页面是否存在某文字"""
        sql_list = query_db(sql)
        sql_colum = []
        for i in sql_list:
            sql_colum.append(str(list(i.values())[0]))
        try:
            assert word in sql_colum, log.warning("断言失败: 该内容不存在数据列表中 | word:{}".format(word))
            log.info("断言成功: 该内容存在数据列表中 | word:{}".format(word))
        except Exception as e:
            return e

if __name__ == "__main__":
   # print(value_assert_equal(1,2))
   # print(value_assert_Notequal(1,2))
   # print(value_assert_True(0))
   # print(value_assert_False(1))
   # print(value_assert_Is(2, 2))
   # print(value_assert_IsNot(2,2))
   # print(value_assert_IsNone(None))
   # print(value_assert_IsNoneNot(1))
   # print(value_assert_In(3, {3,2}))
   # print(value_assert_InNot(3, {3,2}))
   print(value_assert_Instance("abc",str))
   print(value_assert_IsInstanceNot(2,int))



