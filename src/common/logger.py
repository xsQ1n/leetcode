from encodings import utf_8
import logging
import time
class Logger(object):
    """
    set logger format
    """

    def __init__(self, name) -> None:
        self.logger = logging.getLogger(f"{name}")

    def getlogger(self, leavel):
        self.setlogger(leavel)
        return self.logger

    def setlogger(self,leavel):
        self.logger.setLevel(leavel)
        # 创建一个处理器handler  StreamHandler()控制台实现日志输出
        shell_header = logging.StreamHandler()
        # 创建一个格式器formatter（日志内容：当前时间，文件，日志级别，日志描述信息）
        shell_formatter = logging.Formatter(fmt="%(asctime)s %(pathname)s %(lineno)dline"
                                               "[%(levelname)s]: %(message)s",datefmt="%Y/%m/%d %H:%M:%S")
        # 关联控制台日志器—处理器—格式器
        self.logger.addHandler(shell_header)
        shell_header.setFormatter(shell_formatter)
        shell_header.setLevel(leavel)
        
        #创建文件处理器，日志写入文件(执行一次建立一个、一天建立一个)
        #file_header = logging.FileHandler(filename="./log/{}.log".format(time.strftime("%Y%m%d_%H%M%S",time.localtime())), encoding="utf8")
        file_header = logging.FileHandler(filename="./log/{}.log".format(time.strftime("%Y%m%d",time.localtime())), encoding="utf8")
        #设置日志文件格式
        file_formatter = logging.Formatter(fmt="%(asctime)s %(pathname)s %(lineno)dline"
                                               "[%(levelname)s]: %(message)s",datefmt="%Y/%m/%d %H:%M:%S")
        self.logger.addHandler(file_header)
        file_header.setFormatter(file_formatter)
        file_header.setLevel(leavel)
    