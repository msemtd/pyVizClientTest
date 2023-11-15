import sys
import time
import socket
from appJar import gui

default_port = 49333
app = gui()
app.addLabel("title", "Welcome to pyVizClientTest")
app.setLabelBg("title", "red")
app.addLabelEntry("port")
app.setEntryDefault("port", default_port)
app.setEntry("port", default_port)

class VizServerComms():
    """
    Python equivalent of comms for VizServer.
    use select or a thread and a queue for reading
    """
    port = 0
    running = False
    client = None
    lsock = None
    def start(self, port):
        assert (not self.running), "already running"
        assert (isinstance(port, int)), "port int"
        assert (0 < port <= 65535), "port range"
        assert (self.lsock == None), "already listening"
        self.port = port
        self.lsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.lsock.setblocking(0)
        server_address = ('localhost', port)
        self.lsock.bind(server_address)
        self.lsock.listen(5)


vcs = VizServerComms()

def listenOnPort(port):
    vcs.start(port)

def press(button):
    if button == "Listen":
        port = app.getEntry("port")
        print("listen on port:", port)
        try:
            listenOnPort(int(port))
        except AssertionError as error:
            print("An exception occurred", error)

app.addButtons(["Listen"], press)

app.go()
