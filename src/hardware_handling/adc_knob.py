class BigKnob():
    """This class implements a virtual representation of the big frequency select knob mounted in the front panel.
    Using the frequency select knob makes it possible to select a single station from a list of webradio stations.
    Therefor the hardware knob is connected to a potentiometer and an ADC with an I2C Interface which is used to
    get the actual value here.
    """

    def __init__(self, i2cAdress, onChangeFunction):
        pass