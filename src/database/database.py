import mysql.connector


class PlaylistDatabase():
    """Get station urls from a mysql database hosted on the pi. It's easier
    for a webbased configuration tool (php or whatever based) to change the
    stations.
    """

    def __init__(self,host,user,pw):
        #self._mydb_ = mysql.connector.connect(host=host,user=user,passwd=pw)
        self._getPlaylists_()
        
        
    def _getPlaylists_(self):
        #cursor = self._mydb_.cursor()
        #cursor.execute("SELECT url FROM FM_PLAYLIST")
        fmResult = ["http://streams.radiobob.de/bob-live/mp3-192/mediaplayer","http://streams.radiobob.de/bob-classicrock/mp3-192/mediaplayer","http://www.ndr.de/resources/metadaten/audio/m3u/n-joy.m3u","http://www.ndr.de/resources/metadaten/audio/m3u/n-joy.m3u","http://www.ndr.de/resources/metadaten/audio/m3u/n-joy.m3u","http://streams.radiobob.de/bob-live/mp3-192/mediaplayer","http://streams.radiobob.de/bob-classicrock/mp3-192/mediaplayer","https://www.ndr.de/resources/metadaten/audio_ssl/m3u/ndr2.m3u","https://www.ndr.de/resources/metadaten/audio_ssl/m3u/ndr2.m3u","https://www.ndr.de/resources/metadaten/audio_ssl/m3u/ndr2.m3u","https://www.ndr.de/resources/metadaten/audio_ssl/m3u/ndr2.m3u"]
        self._fmPlaylist_ = fmResult
        #cursor.execute("SELECT url FROM AM_PLAYLIST")
        #amResult = cursor.fetchall()
        amResult = fmResult
        self._amPlaylist_ = fmResult
        #cursor.execute("SELECT url FROM LW_PLAYLIST")
        self._lwPlaylist_  = fmResult



    def getStationURL(self, frequency, broadcastingTechnology):
        if broadcastingTechnology == "AM":
            return self._amPlaylist_[frequency]
        elif broadcastingTechnology == "FM":
            return self._fmPlaylist_[frequency]
        else:
            return self._lwPlaylist_[frequency]

    def updateDatabase(self):
        self._getPlaylists_()
