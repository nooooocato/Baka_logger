import os
import threading
import logging
from queue import Queue
# from singleton import singleThread

# @singleThread
class LogWriterThread(threading.Thread):

    def __init__(self, log_queue: Queue, log_path: str):
        super().__init__()
        self.logger = logging.getLogger(log_path)
        self.logger.setLevel(logging.DEBUG)

        file_handler = logging.FileHandler(log_path, encoding='utf-8')

        formatter = logging.Formatter(
            '%(asctime)s - %(levelname)s - "%(message)s"')
        file_handler.setFormatter(formatter)
        self.logger.addHandler(file_handler)

        self.log_queue = log_queue
        self.log_path = log_path
        self.lock = threading.Lock()
        

    def run(self):
        while True:
            if self.log_queue.empty():
                break
            log_data = self.log_queue.get()
            level, content = log_data
            eval(f"self.{level}(\"{content}\")")

    def info(self, msg):
        self.logger.info(msg)

    def warning(self, msg):
        self.logger.warning(msg)

    def error(self, msg):
        self.logger.error(msg)

    def critical(self, msg):
        self.logger.critical(msg)

    def exception(self, msg):
        self.logger.exception(msg)