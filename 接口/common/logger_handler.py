import logging


class LoggerHandler(logging.Logger):
    def __init__(self,
                 name='root',
                 level='DEBUG',
                 file=None,
                 format='%(asctime)s - %(filename)s - %(lineno)d - %(name)s - %(levelname)s - %(message)s - %(process)s'):
        super().__init__(name)

        # 设置日志收集器级别
        self.setLevel(level)

        fmt = logging.Formatter(format)

        # 初始化处理器
        if file:
            file_handler = logging.FileHandler(file)
            file_handler.setLevel(level)
            file_handler.setFormatter(fmt)
            self.addHandler(file_handler)
        stream_handler = logging.StreamHandler()
        stream_handler.setLevel(level)
        stream_handler.setFormatter(fmt)
        self.addHandler(stream_handler)


# 在初始化的时候就初始化对象，然后其余地方用的时候，直接导入对象，不用实例化对象，这样可以保持整个项目统一
logger = LoggerHandler('python_api', file='log_my.txt')

if __name__ == '__main__':
    logger = LoggerHandler()
    logger.debug('hello world')


