import cv2
from queue import Queue
from threading import Thread

class VideoStream:
    def __init__(self, device=0, size=100):
        self.stream = cv2.VideoCapture(device)
        self.stream.set(cv2.CAP_PROP_FPS, 10)
        self.stopped = False
        self.queue = Queue(maxsize=size)

    def start(self):
        thread = Thread(target=self.update, args=())
        thread.daemon = True
        thread.start()
        return self

    def update(self):
        while self.stopped is False:

            if not self.queue.full():
                (grabbed, frame) = self.stream.read()

            if not grabbed:
                self.stop()
                return

            self.queue.put(frame)

    def read(self):
        return self.queue.get()

    def check_queue(self):
        return self.queue.qsize() > 0

    def stop(self):
        self.stopped = True
        self.stream.release()



