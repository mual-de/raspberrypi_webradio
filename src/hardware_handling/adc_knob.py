import Adafruit_ADS1x15

class BigKnob():
    """This class implements a virtual representation of the big frequency select knob mounted in the front panel.
    Using the frequency select knob makes it possible to select a single station from a list of webradio stations.
    Therefor the hardware knob is connected to a potentiometer and an ADC with an I2C Interface which is used to
    get the actual value here.
    """

    _LINEARMAPPING_ = {
        "102" : 215,
        "101" : 2890,
        "100" : 5860,
        "99"  : 8948,
        "98"  : 11750,
        "97"  : 14420,
        "96"  : 17470,
        "95"  : 19780,
        "94"  : 22160,
        "93"  : 24220,
        "92"  : 26850
    }

    def __init__(self):
        
        # start adafruit ads1115 adc lib
        self._adc_ = Adafruit_ADS1x15.ADS115()


    def getActualFMFrequency(self):
        """Get fm frequency as shown on display
        """
        counter = self._adc_.read_adc(0,gain=1)

        for key,val in BigKnob._LINEARMAPPING_:
            # check if measured value can be key +- 30% failure
            if counter >= (val - val*0.3) and counter <= (val + val*0.3):
                return key

        return "0"

    def getActualStation(self):
        return int(self.getActualFMFrequency()) - 93