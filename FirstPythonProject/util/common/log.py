import logging
# 创建一个logger
from util.common import config
import time


class LoggerUtil(object):
    def __init__(self):
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.DEBUG)

        # 定义handler的输出格式
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        # 创建一个handler，用于写入日志文件
        #是否是正式环境
        is_prod = config.getConfigByKey("prod").lower()
        if is_prod == 'true':

            fh = logging.FileHandler('../logs/'+time.strftime("%Y-%m-%d")+'-log.log', mode='w', encoding='UTF-8')
            fh.setLevel(logging.DEBUG)
            fh.setFormatter(formatter)
            self.logger.addHandler(fh)
        # 再创建一个handler，用于输出到控制台
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)
        ch.setFormatter(formatter)
        # 给logger添加handler
        self.logger.addHandler(ch)

    def debug(self, message):
        self.logger.debug(message)

    def info(self, message):
        self.logger.info(message)

    def warn(self, message):
        self.logger.warning(self,message)

    def error(self, message):
        self.logger.error(message)




