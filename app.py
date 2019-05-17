import sys
import time
from appJar import gui

app = gui()
app.addLabel("title", "Welcome to pyVizClientTest")
app.setLabelBg("title", "red")
app.go()
