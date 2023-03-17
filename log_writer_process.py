import multiprocessing

from threading import Thread
from log_writer_thread import LogWriterThread
from log_proxy import LogProxy
from singleton import singleton


@singleton
class LogWriterProcess(multiprocessing.Process):

    def __init__(self):
        super().__init__()
        self.proxy = LogProxy([])
        self.log_queues = self.proxy.log_queues
        self.destinations = self.proxy.destinations
        self.threads = {}
        # self.log_directory = self.proxy.
        # self.num_threads = num_threads

    def run(self):
        for destination in self.destinations:
            if (destination not in self.threads):
                thread: Thread = LogWriterThread(self.log_queues[destination],
                                                 destination)
                # 用字典储存线程，以destination为key，存在的线程就不创了，就直接run
                thread.start()
                self.threads.update({destination: thread})
        #         # print(threads)

        for thread in self.threads:
            self.threads[thread].run()
            self.threads[thread].join()  #等待所有线程跑完，才能跑下一波

        # Done, all threads have finished.

    # def stop(self):
    #     for i in range(self.num_threads):
    #         self.log_queue.put(
    #             None)  # Send sentinel value to each thread to signal exit
