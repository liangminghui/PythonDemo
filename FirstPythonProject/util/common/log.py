import logging
# 创建一个logger
from util.common import config


class LoggerUtil(object):
    def __init__(self):
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.DEBUG)

        # 创建一个handler，用于写入日志文件
        fh = logging.FileHandler('../logs/test.log', mode='w', encoding='UTF-8')
        fh.setLevel(logging.DEBUG)
        # 再创建一个handler，用于输出到控制台
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)
        # 定义handler的输出格式
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        fh.setFormatter(formatter)
        ch.setFormatter(formatter)
        # 给logger添加handler
        self.logger.addHandler(fh)
        self.logger.addHandler(ch)

    def debug(self, message):
        self.logger.debug(message)

    def info(self, message):
        print(message)
        self.logger.info(message)

    def warn(self, message):
        self.logger.warning(self,message)

    def error(self, message):
        self.logger.error(message)

config.getConfigByKey("port1")


