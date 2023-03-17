import threading
from log_writer_process import LogWriterProcess

class SuperLogger(threading.Thread):
    def __init__(self, level, content, destination) -> None:
        super().__init__()
        self.log_process = LogWriterProcess()
        self.log_quenes = self.log_process.proxy
        self.log_quenes.add_destination(destination),
        self.log_quenes.add_log(level, content, destination),
        self.log_process.run(),
        self.start()