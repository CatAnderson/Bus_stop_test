class BusStop:
    def __init__(self, name):
        self.queue = []
        self.name = name

    def add_to_queue(self, passengers):
        self.queue.append(passengers)

    def queue_length(self):
        return len(self.queue)

    def clear(self):
        self.queue.clear()
        

