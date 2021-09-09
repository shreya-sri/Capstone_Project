import sys
import re
import json
from PyQt5 import QtCore, QtGui, QtWidgets, sip
from Create_Widgets import CreateWidgets
import Get_Question 

states_and_cities = json.loads(open('../backend/states_and_cities.json').read())

class Window(QtWidgets.QWidget):
    
    def __init__(self):
        super().__init__()
    
        self.setWindowTitle("MainWindow")
        self.setGeometry(100, 100, 600, 600)
        #self.showFullScreen()
        self.setStyleSheet("background: #04284d;")
        self.layout
        self.response_dict = dict()
        self.val = 16
        self.questions_page()
        
        
    def wait_page(self):
        
        self.layout = QtWidgets.QGridLayout()
        self.setLayout(self.layout)
    
        self.text = CreateWidgets.create_Label()
        self.text.setAlignment(QtCore.Qt.AlignCenter)
        self.text.setText("Detecting")
        self.text.setFont(QtGui.QFont("Ubuntu mono", 70))
        
        self.time_val = 10
        self.timer = QtCore.QTimer()       
        self.timer.timeout.connect(self.countdown)
        self.timer.start(1000)
        
        self.button = CreateWidgets.create_Button()
        self.button.setText("Continue")
        self.button.clicked.connect(self.main_page)
        self.button.hide()
        
        self.layout.addWidget(self.text, 1, 0, 1, 5)  
        self.layout.addWidget(self.button, 3, 2, 1, 1)
        self.layout.setRowStretch(0, 1)
        self.layout.setRowStretch(2, 1)
        self.layout.setRowStretch(4, 1)
            

    def main_page(self):
        
        if self.layout is not None:
            self.deleteLayout(self.layout)
        
        self.layout = QtWidgets.QGridLayout()
        self.setLayout(self.layout)
        
        self.text1 = CreateWidgets.create_Label()
        self.text1.setText("Welcome!")
        self.text1.setAlignment(QtCore.Qt.AlignCenter)
        self.text1.setFont(QtGui.QFont("Ubuntu mono", 60))
        
        self.tex2 = CreateWidgets.create_Label()
        self.tex2.setText("Would you like to use our voice assistant?")
        self.tex2.setAlignment(QtCore.Qt.AlignCenter)
        self.tex2.setFont(QtGui.QFont("Ubuntu mono", 50))
        
        self.yes_button = CreateWidgets.create_Button()
        self.yes_button.setText("yes")
        self.yes_button.clicked.connect(self.load_page)
        
        self.no_button = CreateWidgets.create_Button()
        self.no_button.setText("no")
        self.no_button.clicked.connect(self.load_page)
        
        self.layout.addWidget(self.text1, 1, 0, 1, 5)
        self.layout.addWidget(self.tex2, 2, 0, 1, 5)
        self.layout.addWidget(self.yes_button, 4, 1)
        self.layout.addWidget(self.no_button, 4, 3)
        self.layout.setColumnMinimumWidth(0, 200)
        self.layout.setColumnMinimumWidth(4, 200)
        self.layout.setRowMinimumHeight(3, 100)
        self.layout.setRowStretch(0, 1)
        self.layout.setRowStretch(5, 1)
    
    
    def load_page(self):
        
        if self.layout is not None:
            self.deleteLayout(self.layout)
            
        self.layout = QtWidgets.QGridLayout()
        self.setLayout(self.layout)
        
        self.text = CreateWidgets.create_Label()
        self.text.setText("Please wait while the page loads...")
        self.text.setAlignment(QtCore.Qt.AlignCenter)
        self.text.setFont(QtGui.QFont("Ubuntu mono", 30))
        
        self.pbar = CreateWidgets.create_Progressbar()
        self.timer = QtCore.QTimer()       
        self.timer.timeout.connect(self.handleTimer)
        self.timer.start(100)
        
        self.button = CreateWidgets.create_Button()
        self.button.setText("begin")
        self.button.hide()
        self.button.clicked.connect(self.questions_page)
        
        self.layout.addWidget(self.text, 1, 0, 1, 5)  
        self.layout.addWidget(self.pbar, 3, 0, 1, 5)
        self.layout.addWidget(self.button, 5, 2, 1, 1)
        self.layout.setRowMinimumHeight(5, 200)
        self.layout.setRowStretch(0, 1)
        self.layout.setRowStretch(2, 1)
        self.layout.setRowStretch(6, 1)
        
        
    def questions_page(self):
        
        #if self.layout is not None:
        #    self.deleteLayout(self.layout)
           
        self.layout = QtWidgets.QGridLayout()
        self.setLayout(self.layout)
         
        self.question, self.response = Get_Question.Get_Question_and_Widget(self.val)
        self.question.setFont(QtGui.QFont("Ubuntu mono", 30))
    
        self.req = CreateWidgets.create_Label()
        self.req.setFont(QtGui.QFont("Ubuntu mono", 15))    
    
        self.next = CreateWidgets.create_Button()
        self.next.setText("next")
        self.next.clicked.connect(self.check_response)
        self.next.clicked.connect(self.gotonext)
        
        self.prev = CreateWidgets.create_Button()
        self.prev.setText("previous")
        self.prev.clicked.connect(self.gotoprev)
            
        self.layout.addWidget(self.question,1, 0, 1, 5)
            
        if len(self.response) == 1:
            if isinstance(self.response[0], QtWidgets.QPushButton):
                
                self.file = CreateWidgets.create_Label()
                self.file_display = CreateWidgets.create_Label()
                self.file.setFont(QtGui.QFont("Ubuntu mono", 15))
                
                self.response[0].clicked.connect(self.getfile)
                
                self.layout.addWidget(self.response[0], 2, 2, 1, 1)
                self.layout.addWidget(self.file_display, 3, 2, 1, 1)
                self.layout.addWidget(self.file, 4, 2, 1, 1)
                
                self.layout.setRowMinimumHeight(0, 200)
                self.layout.setRowMinimumHeight(1, 100)
                self.layout.setRowMinimumHeight(2, 100)
                self.layout.setRowMinimumHeight(3, 100)
                self.layout.setRowMinimumHeight(4, 50)
                
                self.layout.addWidget(self.prev, 6, 1, 1, 1)
                self.layout.addWidget(self.next, 6, 3, 1, 1)
                self.layout.setRowMinimumHeight(6, 200)
                
            elif isinstance(self.response[0], QtWidgets.QTextEdit):
                
                self.layout.addWidget(self.response[0], 2, 1, 1, 3)
                self.layout.addWidget(self.req, 3, 1, 1, 3)
                
                self.layout.setRowMinimumHeight(0, 200)
                self.layout.setRowMinimumHeight(1, 100)
                self.layout.setRowMinimumHeight(2, 100)
                self.layout.setRowMinimumHeight(3, 100)
            
                self.layout.addWidget(self.prev, 4, 1, 1, 1)
                self.layout.addWidget(self.next, 4, 3, 1, 1)
                self.layout.setRowMinimumHeight(4, 200)
                
            else:    
                self.layout.addWidget(self.response[0], 2, 1, 1, 3)
                if isinstance(self.response[0], QtWidgets.QComboBox):
                    if "state" in self.question.text().lower():
                        states = list(states_and_cities.keys())
                        self.response[0].addItems(states)
                    elif "city" in self.question.text().lower():
                        cities = states_and_cities[list(self.response_dict.values())[-1]]
                        self.response[0].addItems(cities)
                if isinstance(self.response[0], QtWidgets.QLineEdit):
                    if "required" in self.question.text():
                        self.response[0].setPlaceholderText("**Required")
                        self.response[0].setFocus()
                        
                self.layout.setRowMinimumHeight(0, 200)
                self.layout.setRowMinimumHeight(1, 100)
                self.layout.setRowMinimumHeight(2, 100)
                self.layout.setRowMinimumHeight(3, 200)
                
                self.layout.addWidget(self.prev, 4, 1, 1, 1)
                self.layout.addWidget(self.next, 4, 3, 1, 1)
                self.layout.setRowMinimumHeight(4, 200)
                
        elif len(self.response) == 2:
            self.layout.addWidget(self.response[0], 2, 1)
            self.layout.addWidget(self.response[1], 2, 3)
            self.layout.setRowMinimumHeight(0, 200)
            self.layout.setRowMinimumHeight(1, 100)
            self.layout.setRowMinimumHeight(2, 100)
            self.layout.setRowMinimumHeight(3, 200)
             
            self.layout.addWidget(self.prev, 4, 1, 1, 1)
            self.layout.addWidget(self.next, 4, 3, 1, 1)
            self.layout.setRowMinimumHeight(4, 200)

            
        elif len(self.response) > 2:
            for i in range(len(self.response)):
                self.layout.addWidget(self.response[i], i//3 + 2, i%3+1, 1, 2)
                self.layout.setRowMinimumHeight(0, 50)
                self.layout.setRowMinimumHeight(1, 100)
                self.layout.setRowMinimumHeight(i//3+2, 50)
                self.layout.setColumnMinimumWidth(i%3+1, 300)
                self.layout.setColumnMinimumWidth(2, 300)
                self.layout.setColumnMinimumWidth(0, 150)
                self.layout.setColumnMinimumWidth(4, 150)
            
            self.layout.addWidget(self.prev, len(self.response)//3 +3, 1, 1, 1)
            self.layout.addWidget(self.next, len(self.response)//3 +3, 3, 1, 1)
            self.layout.setRowMinimumHeight(len(self.response)//3 +3, 200)
            
        
    def end_page(self):
        #print(self.response_dict)
        #r_dict = {'Please enter your First name. This field is required.': 'shreya', 
        #'Please enter your Middle name.': '', 
        #'Please enter your Last name.': '', "Please enter your Father's name.": '', 
        #"Please enter your Mother's name.": '', 
        #'Please enter your Date of birth. This field is required.': '22-12-2000', 
        #'Please enter your Age. This field is required.': '20', 'Please select your Gender.': 'Female', 
        #'Please enter your Mobile No.. This field is required.': '9481407203', 
        #'Please enter your Email ID. This field is required.': 'shreyaram22@gmail.com', 
        #'Please enter your Marks of Identification.': '', 'Please select your Category.': 'General', 
        #'Please select your Relation with PwD.': 'self', 
        #'Please Upload your Photo. This field is required.': 'C:/Users/shrey/Downloads/s1.jpg', 
        #'Please Upload your Signature. This field is required.': 'C:/Users/shrey/Downloads/s1.jpg', 
        #'Please Enter your Address.': '', 'Please select your State.': 'Karnataka', 
        #'Please select your City.': 'Bengaluru', 'Please Enter your Village (if applicable).': '', 
        #'Please Enter your Pincode. This field is required.': '560071', 
        #'Please select your Choice of Address Proof.': 'Drivers License', 
        #'Please Upload your Address Proof. This field is required.': 'C:/Users/shrey/Downloads/s1.jpg', 
        #'Please select your Disability certificate. Select one of the following.': 'No', 
        #'Please select your Disability type. You can select more than option.': 'Low-Vision, Mental Illness', 
        #'Please select your Disability since when. Select one of the following.': 'Disability\nsince', 
        #'Please enter your Disability Since (if not at birth).': '', 
        #'Please enter your Hospital Treating Disability (if any).': '', 
        #'Please Enter your Pension Card Number (if applicable).': '', 
        #'Please select your Disability Due to.': 'Accident', 
        #'Please select your Employment Status.': 'Employed', 
        #'Please select your Occupation.': 'Agriculture', 'Please select your Poverty Status.': 'Above Poverty Line', 
        #'Please select your Annual Income.': 'less than two lakh', 
        #'Please select your Choice of ID Proof.': 'Drivers License', 
        #'Please Upload your ID Proof. This field is required.': 'C:/Users/shrey/Downloads/s1.jpg', 
        #'Please Enter your ID Proof Number. This field is required.': '560071'}

        if self.layout is not None:
           self.deleteLayout(self.layout)
       
        self.layout = QtWidgets.QHBoxLayout(self)
        self.scrollArea = QtWidgets.QScrollArea(self)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.gridLayout = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.layout.addWidget(self.scrollArea)
        self.heading = CreateWidgets.create_Label()
        self.heading.setText("Applicant Details")
        self.heading.setFont(QtGui.QFont("Ubuntu mono", 60))
        self.gridLayout.setColumnMinimumWidth(0, 25)
        self.gridLayout.setColumnMinimumWidth(1, 775)
        self.gridLayout.setColumnMinimumWidth(2, 150)
        self.gridLayout.setRowMinimumHeight(0, 200)
        self.gridLayout.addWidget(self.heading, 0, 0, 1, 4)
        
        keys = list(self.response_dict.keys())
        for i in range(len(self.response_dict)):
            
            self.question_string = CreateWidgets.create_Label()
            self.question_string.setAlignment(QtCore.Qt.AlignLeft)
            self.question_string.setText(keys[i])
            self.question_string.setFont(QtGui.QFont("Ubuntu mono", 20))
            
            self.response_string = CreateWidgets.create_Label()
            self.response_string.setAlignment(QtCore.Qt.AlignLeft)
            self.response_string.setText(self.response_dict[keys[i]])
            self.response_string.setFont(QtGui.QFont("Ubuntu mono", 20))
            
            self.gridLayout.setRowMinimumHeight(i+1, 45)
            self.gridLayout.addWidget(self.question_string, i+1, 1)
            self.gridLayout.addWidget(self.response_string, i+1, 3)
        
        self.msgbox = QtWidgets.QMessageBox()
        self.msgbox.setWindowTitle("Confirm")
        self.msgbox.setText("Confirm Submission?")
        self. msgbox.setIcon(QtWidgets.QMessageBox.Question)
        go_back = self.msgbox.addButton('Go back to form', self.msgbox.RejectRole)
        confirm = self.msgbox.addButton('Confirm', self.msgbox.ActionRole)
        self.submit = CreateWidgets.create_Button()
        self.submit.setText("Confirm Application")
        self.submit.setSizePolicy(200, 50)
        self.submit.clicked.connect(self.popup_box)
        go_back.clicked.connect(self.gotoquestions)
        confirm.clicked.connect(self.thank_you_page)
        self.gridLayout.setRowMinimumHeight(i+2, 150)
        self.gridLayout.addWidget(self.submit, i+2, 0, 1, 4, alignment=QtCore.Qt.AlignCenter)
        
        
    def thank_you_page(self):
        if self.layout is not None:
           self.deleteLayout(self.layout)
           
        self.layout = QtWidgets.QGridLayout()
        self.setLayout(self.layout)
         
        self.text = CreateWidgets.create_Label()
        self.text.setFont(QtGui.QFont("Ubuntu mono", 60))
        self.text.setText("Thank you!")
        self.layout.addWidget(self.text, 0, 0)
        
        self.timer = QtCore.QTimer()
        self.timer.start(5000)
        self.timer.timeout.connect(self.gotobeginning)
        
        
    def check_response(self):
        if len(self.response) == 1:
            if isinstance(self.response[0], QtWidgets.QLineEdit):
                if "required" in self.question.text():
                    if "Email" in self.question.text():
                        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
                        if not (re.fullmatch(regex, self.response[0].text())):
                            self.val -= 1  
                    elif self.response[0].text() == "":
                        self.val -= 1  
                        self.req.setText("**Required")
                self.response_dict[self.question.text()] = self.response[0].text()
                
            if isinstance(self.response[0], QtWidgets.QTextEdit):
                self.response_dict[self.question.text()] = self.response[0].toPlainText()
                
            if isinstance(self.response[0], QtWidgets.QComboBox):
                if self.response[0].currentText() == "Select":
                    self.val -= 1
                self.response_dict[self.question.text()] = self.response[0].currentText()
                
            if isinstance(self.response[0], QtWidgets.QPushButton):
                if self.file.text() == "" or self.file.text() == "required!":
                    self.val -=1
                self.response_dict[self.question.text()] = self.file.text()
              
        if len(self.response) == 2:
            if isinstance(self.response[0], QtWidgets.QRadioButton):
                if self.response[0].isChecked() == False and self.response[1].isChecked() == False:
                    self.val -= 1
                    
                elif self.response[0].isChecked() == False:
                    self.response_dict[self.question.text()] = self.response[1].text()
                    
                elif self.response[1].isChecked() == False:
                    self.response_dict[self.question.text()] = self.response[0].text()
                
        elif len(self.response) > 2:
            if isinstance(self.response[0], QtWidgets.QCheckBox):
                check = 0
                checked_list = []
                for i in range(len(self.response)):
                    if self.response[i].isChecked() == False:
                        check +=1
                    else: 
                        checked_list.append(self.response[i].text())
                if check == len(self.response):
                    self.val -=1   
                self.response_dict[self.question.text()] = ", ".join(checked_list)
      
                
    def countdown(self):
       if self.time_val > 0:
            if self.time_val%3 == 0:
                self.text.setText("Detecting..")
            elif self.time_val%3 == 1:
                self.text.setText("Detecting.")
            elif self.time_val%3 == 2:
                self.text.setText("Detecting")
            self.time_val -= 1
       else:
            self.timer.stop()
            self.text.setText("Detected!")
            self.button.show()           
        
        
    def getfile(self):
      fname = QtWidgets.QFileDialog.getOpenFileName(self, 'Open file', 'c:\\',"Image files (*.jpg  *.png *.gif)")
      image = QtGui.QPixmap(fname[0])
      self.file_display.resize(90,90)
      self.file_display.setPixmap(image.scaled(self.file.size(), QtCore.Qt.KeepAspectRatio))
      self.file.setText(fname[0])
      
    
    def gotonext(self):
        self.val += 1
        self.deleteLayout(self.layout)
        if self.val == len(Get_Question.data['root']):
            self.end_page()
        else:
            self.questions_page()
            
            
    def gotoprev(self):
        self.val -= 1
        self.deleteLayout(self.layout)
        if self.val == -1:
            self.main_page()
        else:
            self.questions_page()
            
            
    def gotoquestions(self):
        self.val = 0
        self.questions_page()
        
        
    def gotobeginning(self):
        self.val = 0
        self.deleteLayout(self.layout)
        self.wait_page()
    
    
    def handleTimer(self):
        value = self.pbar.value()
        if value < 100:
            value = value + 1
            self.pbar.setValue(value)
        else:
            self.timer.stop()
            self.button.show()
        
        
    def popup_box(self):
        self.msgbox.show()
        
        
    def deleteLayout(self, cur_lay):
        if cur_lay is not None:
            while cur_lay.count():
                item = cur_lay.takeAt(0)
                widget = item.widget()
                if widget is not None:
                    widget.deleteLater()
                else:
                    self.deleteLayout(item.layout())
        sip.delete(cur_lay)
              
    
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())
