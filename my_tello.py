from djitellopy import Tello

_RETRY_COUNT = 3  # number of retries after a failed command
_TELLO_IP = '192.168.10.1'  # Tello IP address

class MyTello(Tello):

    def __init__(self, host=_TELLO_IP, retry_count=_RETRY_COUNT):
        super().__init__(self, host, retry_count)


