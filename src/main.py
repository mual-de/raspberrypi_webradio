from audio_player.interface import AudioInterface
from hardware_handling.hardware import Hardware
from database.database import PlaylistDatabase
import vlc
import time

class Webradio():
    def __init__(self):
        print("LOAD DB")
        self._db_ = PlaylistDatabase("test","test","test")
        print("LOAD VLC")
        self._audioInterface_ = AudioInterface('http://streams.radiobob.de/bob-classicrock/aac-64/mediaplayer')
        print("LOAD HARDWARE")
        self._hardware_ = Hardware(self.changeStation)
        # audioInterface.changeStation('http://streams.radiobob.de/bob-live/mp3-192/mediaplayer')
        print("webradio started")

    def changeStation(self,frequency, broadcastingTechnology):
        url = self._db_.getStationURL(frequency,broadcastingTechnology)
        print("NEW URL: %s", url)
        self._audioInterface_.changeStation(url)







if __name__=="__main__":
    Webradio()