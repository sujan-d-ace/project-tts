import sys
from PyQt5.QtWidgets import QApplication, QFileDialog,QTextEdit, QMainWindow, QPushButton, QLabel
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPalette, QColor, QBrush, QLinearGradient, QFont
import load

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.title = "Text2Speech"
        self.top = 10
        self.left = 10
        self.width = 1280
        self.height = 1080
        
        self.InitWindow()
        
    def InitWindow(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.top,self.left, self.width, self.height)
               
        #TTS System Status Bar
        self.fontstatus = QFont()
        self.fontstatus.setPointSize(12)
        self.fontstatus.setBold(True)
        
        self.statusBar().showMessage('-->Waiting for Input....')
        self.statusBar().setStyleSheet("background-color: rgba(150, 0, 0, 0.2);")
        self.statusBar().setFont(self.fontstatus)
        
        #TTS System Heading
        self.font = QFont()
        self.font.setPointSize(32)
        self.font.setBold(True)
        self.font.setWeight(63)
        self.font.setStretch(100)
        
        self.TTS_label = QLabel(self)
        self.TTS_label.setText("<font color=#00008b>TEXT TO SPEECH APPLICATION")
        self.TTS_label.setFont(self.font)
        self.TTS_label.move(0,60)
        self.TTS_label.resize(1280,60)
        self.TTS_label.setAlignment(Qt.AlignCenter)
        
        #TTS System Heading Description
        self.fontdes = QFont()
        self.fontdes.setPointSize(14)
        self.fontdes.setWeight(63)
        self.fontdes.setStretch(80)
        
        self.TTS_label = QLabel(self)
        self.TTS_label.setText("<font color=#7b68ee>[A tiny app that allows you to convert text input to voice output]")
        self.TTS_label.setFont(self.fontdes)
        self.TTS_label.move(0,102)
        self.TTS_label.resize(1280,40)
        self.TTS_label.setAlignment(Qt.AlignCenter)
        
        #TTS System speak now label
        self.font1 = QFont()
        self.font1.setPointSize(18)
        self.font1.setBold(True)
        self.font1.setWeight(50)
        
        self.Sub_label = QLabel(self)
        self.Sub_label.setText("<font color=#8a2be2>Text Input.")
        self.Sub_label.setFont(self.font1)
        self.Sub_label.move(0,125)
        self.Sub_label.resize(1280,150)
        self.Sub_label.setAlignment(Qt.AlignCenter)
            
        #Textedit Box to get Input 
        self.fontbox = QFont()
        self.fontbox.setPointSize(14)
        
        self.text_edit = QTextEdit('This is a Text to Speech System.',self)
        self.text_edit.setFont(self.fontbox)
        self.text_edit.move(45,218)
        self.text_edit.resize(1190,250)
        
        #Font attributes for buttons
        self.butfont = QFont()
        self.butfont.setPointSize(12)
        self.butfont.setBold(True)
        
        #SpeakButton to get Voice Ouput
        self.button=QPushButton(self)
        self.button.setText("Speak Now")
        self.button.move(540,492)
        self.button.setStyleSheet("background-color:#0000ff; color:#ffffe0;")
        self.button.setFont(self.butfont)
        self.button.clicked.connect(self.on_click)

        #OpenButton to get txt file
        self.Open_Button = QPushButton(self)
        self.Open_Button.setText("Open File")
        self.Open_Button.move(660,492)
        self.Open_Button.setStyleSheet("background-color:#dc143c; color:#faf0e6;")
        self.Open_Button.setFont(self.butfont)
        self.Open_Button.clicked.connect(self.on_opclick)
        
        self.showMaximized()
        
        #SpeakButton OnClick Action to get text to speech voice
    def on_click(self): 
        #TTS System Status Bar : Text to Speech Conversion
        self.statusBar().showMessage('-->Converting Text To Speech....')
        self.statusBar().setFont(self.fontstatus)
        
        data = self.text_edit.toPlainText() #returns the text from the text_edit box as plain text
        
        #To call and access the function of load module
        p = load.TextToSpeech()
        p.get_pronunciation(data)
        
        
        #OpenButton Onclick Action to display OpenFileDialog Box
    def on_opclick(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self,"Open a File", "","Text Files (*.txt);;Python Files (*.py)", options=options)
        if fileName:
            #TTS System Status Bar : Opening a File
            self.statusBar().showMessage('-->Opened a File : ' + fileName)
            self.statusBar().setFont(self.fontstatus)
            
            #To Open and Read the Content of a File
            file = fileName #store file path with file name in file variable
            f = open(file, 'r+') #Opens the file in read only mode
            text = f.read() #reads the content of file
            self.text_edit.clear() #clears the textedit box area
            self.text_edit.setText(text) #display the content of file in textedit box
            
if __name__ == '__main__':        
    App=QApplication(sys.argv)
    window = Window()
    
    #Gradient background for window
    p = QPalette()
    gradient = QLinearGradient(0, 0, 0, 400)
    gradient.setColorAt(0.0, QColor(240, 240, 240))
    gradient.setColorAt(1.0, QColor(220, 160, 160))
    p.setBrush(QPalette.Window, QBrush(gradient))
    window.setPalette(p)
    
    sys.exit(App.exec())