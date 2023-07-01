import threading

class MyMessenger(threading.Thread):
    def run(self):
        # When we just make a loop and we don't care about in which loop are we. We just type underscore(_) instead 'x' or etc.
        for _ in range(10):
            print(threading.currentThread().getName())

x = MyMessenger(name='Send out messages')
y = MyMessenger(name='Receive messages')

x.start()
y.start()