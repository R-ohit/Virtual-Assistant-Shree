from PyQt5 import QtGui
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtCore import Qt, QTimer, QTime, QDate
from ShreeUi import Ui_MainWindow
import sys
import Main

class MainThread(QThread):

    def __init__(self):
        
         super(MainThread,self).__init__()
    
    def run(self):
         self.Task_Gui()

    def Task_Gui(self):
        Main.TaskExecution()

startFunctions = MainThread()


class Gui_Start(QMainWindow):

    def __init__(self):
        
        super().__init__()

        self.Project_ui = Ui_MainWindow()
        
        self.Project_ui.setupUi(self)

        self.Project_ui.pushButton.clicked.connect(self.startFunc)

        self.Project_ui.pushButton_2.clicked.connect(self.close)

    def startFunc(self):
        self.Project_ui.movies = QtGui.QMovie("SHREE(1).gif") 

        self.Project_ui.Gif.setMovie(self.Project_ui.movies)
        
        self.Project_ui.movies.start()
    
        timer = QTimer(self)
    
        timer.timeout.connect(self.showtime)

        timer.start(1000)

        startFunctions.start()

    def showtime(self):

        current_time = QTime.currentTime()

        label_time = current_time.toString("hh:mm:ss")

        labbel = "Time is now :" + label_time
    
        self.Project_ui.textBrowser.setText(labbel)
    
Gui_App = QApplication(sys.argv)
    
Gui_Project_Ui = Gui_Start()

Gui_Project_Ui.show()

exit(Gui_App.exec_())