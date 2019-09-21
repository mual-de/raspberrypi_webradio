import vlc
import time
import threading

class AudioInterface(threading.Thread):


    def __init__(self, initialStation):
        threading.Thread.__init__(self) 
        print("Test")
        self.instance = vlc.Instance('--input-repeat=-1', '--fullscreen')
        self.player= self.instance.media_player_new()
        self.player.set_mrl(initialStation)
        self.start()
        
    def run(self):
        while True:
            print("Play")
            self.player.play()
            time.sleep(2)
            while(self.player.is_playing()):
                time.sleep(3)
            time.sleep(2)

    def changeStation(self, station):
        self.player.stop()
        self.player.set_mrl(station)