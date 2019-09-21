class Switch():
    
    def __init__(self, state):
        self._oldState_ = state
        self._state_ = state


    def getActualState(self):
        return self._state_

    def getLastState(self):
        return self._oldState_

    def changeState(self, value):
        self._oldState_ = self._state_
        self._state_ = value

    def toogleState(self):
        self._oldState_ = self._state_
        self._state_ = not self._state_