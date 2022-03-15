import logging, time, os
from functools import wraps
import traceback

BASE_PATH = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))

LOG_PATH = os.path.join(BASE_PATH, "log")
if not os.path.exists(LOG_PATH):
    os.mkdir(LOG_PATH)

class Logger():

    def __init__(self):
        #创建日志路径和时间
        """  知识点解析      #time strftime() 函数接收以时间元组，并返回以可读字符串表示的当地时间，格式由参数 format 决定。"""
        self.logname = os.path.join(LOG_PATH, "{}.log".format(time.strftime("%Y%m%d")))
        # 创建一个logger日志对象
        self.logger = logging.getLogger("log")
        # 设置默认的日志级别
        self.logger.setLevel(logging.DEBUG)
        # 创建日志格式对象
        self.formater = logging.Formatter(
            '[%(asctime)s][%(filename)s %(lineno)d][%(levelname)s]: %(message)s')

        #创建FileHandler对象
        """mode = 'a'"""
            #a=append=追加，即 给文件保存写入内容，不是覆盖之前已有文件中内容，而是放在最后，追加到最后。
            #一般append追加，适用于 log日志的处理：保留之前log，追加写入新log。
        self.filelogger = logging.FileHandler(self.logname, mode='a', encoding="UTF-8")
        # 创建StreamHandler对象
        self.console = logging.StreamHandler()

        # FileHandler对象自定义日志级别
        self.console.setLevel(logging.DEBUG)
        self.filelogger.setLevel(logging.DEBUG)

        #设置两个地方的格式
        self.filelogger.setFormatter(self.formater)
        self.console.setFormatter(self.formater)

        #logger日志对象加载FileHandler对象
        self.logger.addHandler(self.filelogger)
        # logger日志对象加载StreamHandler对象
        self.logger.addHandler(self.console)

Logger = Logger().logger

def decorate_log(func):
    @wraps(func) # @wraps(func)的作用: 不改变使用装饰器原有函数的结构(如name, doc)
    def log(*args, **kwargs):
        Logger.info(f'------{func.__name__}用例执行------')
        try:
            func(*args, **kwargs)
        except Exception as e:
            Logger.error(f'------{func.__name__}用例失败，失败原因：{e}------')
            Logger.error(f"{func.__name__} 用例 is error,here are details:{traceback.format_exc()}")
            raise e
        else:
            Logger.info(f'------{func.__name__}执行成功------')
    return log


@decorate_log
def yong_liu7():
    assert 2==2
if __name__ == '__main__':
    yong_liu7()

