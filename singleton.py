import threading


def singleton(cls):
    __instances = {}
    def getinstance(*args, **kwargs):
        if cls not in __instances:
            __instances[cls] = cls(*args, **kwargs)
        return __instances[cls]
    return getinstance

def singleThread(cls:threading.Thread):
    __threads = {}
    def getinstance(*args, **kwargs):
        if cls not in __threads:
            __threads[cls] = cls(*args, **kwargs)
            __threads[cls].start()
            # __threads[cls].join()
        return __threads[cls]
    return getinstance