from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox
from MainWindowUI import Ui_CyberRefMain  
from InfoWindow import Ui_CyberRefInfo           #importing the 3 UIs for the 3 windows (Main, Info, Results)
from ResultWindow import Ui_CyberRefResults   
from ResponseGetter import urlChecker

class MainWindow(QMainWindow):
    def __init__(self):                 #setting up the main window
        super().__init__()
        self.ui = Ui_CyberRefMain()              
        self.ui.setupUi(self)
        self.ui.INFO_BUTTON.clicked.connect(self.OpenInfoWindow)
        self.ui.EXIT_BUTTON.clicked.connect(self.close)
        self.ui.START_BUTTON.clicked.connect(self.press_start)

    def OpenResultsWindow(self):        #opening the results window
        self.ResultsWindow = ResultsWindow()
        self.ResultsWindow.show()
        self.close()

    def OpenInfoWindow(self):            #opening the info window
        self.InfoWindow = InfoWindow()
        self.InfoWindow.show()
        self.close() 
    

           
    def UserInputCheck(self, url, ApiKey):            #checking the user input for errors

        if not url and not ApiKey:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setWindowTitle("Error")  
            msg.setText("Invalid URL and API Key")
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec()
            return 0
    
        if not url:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setWindowTitle("Error")
            msg.setText("Invalid URL")
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec()
            return 0
    
        if not ApiKey:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setWindowTitle("Error")
            msg.setText("Invalid API Key")
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec()
            return 0
        

        return 1
   

    def press_start(self):                              
        url = self.ui.URL_EDITBOX.toPlainText()
        ApiKey = self.ui.API_EDITBOX.toPlainText()    

        if self.UserInputCheck(url, ApiKey) == 0:        #if the input is invalid returns to main window
            return        
        
        stats, trackers, outgoing_links, votes = urlChecker(url, ApiKey)    #data collection
                   
        self.OpenResultsWindow()
        
        # scan results
        self.ResultsWindow.ui.MAINHARMLESS_LABEL.setText(f"Harmless : {stats.get('harmless', 0)}")
        self.ResultsWindow.ui.MAINMALICIOUS_LABEL.setText(f"Malicious : {stats.get('malicious', 0)}")
        self.ResultsWindow.ui.MAINSUSPICIOUS_LABEL.setText(f"Suspicious : {stats.get('suspicious', 0)}")
    
        # community votes
        self.ResultsWindow.ui.VOTEHARMLESS_LABEL.setText(f"Harmless : {votes.get('harmless', 0)}")
        self.ResultsWindow.ui.VOTEMALICIOUS_LABEL.setText(f"Malicious : {votes.get('malicious', 0)}")
    
        # outgoing links
        if outgoing_links:
            links_text = "\n".join(f"- {link}" for link in outgoing_links)
        else:
            links_text = "No outgoing links"
        self.ResultsWindow.ui.OUTGOINGLINKS_EDITXT.setPlainText(links_text)
    
        # web trackers
        if trackers:
            trackers_text = "\n".join(trackers.keys())  
        else:
            trackers_text = "No trackers"
        self.ResultsWindow.ui.TRACKERS_EDITXT.setPlainText(trackers_text)
    
        self.ResultsWindow.show()
        self.close()

class InfoWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_CyberRefInfo()
        self.ui.setupUi(self)
        self.ui.BACK_BUTTON.clicked.connect(self.goback)
        
    
    def goback(self):
        self.MainWindow = MainWindow()
        self.MainWindow.show()
        self.close()

class ResultsWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.ui = Ui_CyberRefResults()
        self.ui.setupUi(self)
        self.ui.EXIT_BUTTON.clicked.connect(self.close)
        self.ui.BACK_BUTTON.clicked.connect(self.goback)

    def goback(self):
        self.MainWindow = MainWindow()
        self.MainWindow.show()
        self.close()


if __name__ == "__main__":

    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()