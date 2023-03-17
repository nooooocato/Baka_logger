import queue


class LogProxy:

    def __init__(self, destinations: list):
        self.destinations: list = destinations
        self.log_queues: dict = {
            # destination
            # for destination in destinations
        }  #字典推导式
        # print(self.destinations,self.log_queues)

    def add_log(self, level, content, destination):
        if destination in self.destinations:
            self.log_queues[destination].put((level,content))
        else:
            raise ValueError("Invalid destination: {}".format(destination))

    # def get_num_destinations(self):
    #     return len(self.log_queues)

    def add_destination(self, destination: str):
        if destination not in self.destinations:
            self.destinations.append(destination)
            self.log_queues[destination] = queue.Queue()
        else:
            return
            # raise ValueError(
            #     "Destination already exists: {}".format(destination))
