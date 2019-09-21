import threading
import time
from smbus2 import SMBus
from .adc_knob import BigKnob
from .switch import Switch

class Hardware(threading.Thread):
    
    def __init__(self, callbackFunction):
        threading.Thread.__init__(self)
        self._switches_ = Switch(False)
        self._callbackFunction_ = callbackFunction
        self._ARDUINO_ADRESS_ = 0x08
        # start i2c bus
        self._i2cBus_ = SMBus(1)
        self._bigKnob_ = BigKnob()
        self._stationId_ = 0
        self.start()
        self._setOutputLEDInit_()

    def _getInputStates_(self):
        # update needed ...
        #switchByte = self._i2cBus_.read_byte_data(self._ARDUINO_ADRESS_,1)
        switchByte = 0xFF
        self._modeSwitch_ = Switch(bool(switchByte%0x01))
        self._frequencyBand1Active = bool(switchByte%0x02)
        self._frequencyBand2Active = bool(switchByte%0x04)
        self._frequencyBand3Active = not (self._frequencyBand1Active or self._frequencyBand2Active)
        oldStationId = self._stationId_
        self._stationId_ = self._bigKnob_.getActualStation()
        if self._stationId_ != oldStationId:
            self._stationChanged_ = True


    def _setOutputLEDInit_(self):
        self._ledData_ = [0x0C]
        self._i2cBus_.write_i2c_block_data(self._ARDUINO_ADRESS_,0,self._ledData_)

    def run(self):
        while True:
            time.sleep(0.02)
            self._getInputStates_()
            if self._stationChanged_:
                self._stationChanged_ = False
                print("station changed")
                print(self._stationId_)
                print("NEW CHANNEL!")
                self._callbackFunction_(self._stationId_,"FM")

            