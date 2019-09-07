import threading
from switches import Switches

class Hardware(threading.Thread):

    def __init__(self, callbackFunction):
        threading.Thread.__init__(self)
        self._switches_ = Switches()
        self._callbackFunction_ = callbackFunction
        self.start()

    def run(self):
        while True:
            if not self._switches_.getModeState() and 
            