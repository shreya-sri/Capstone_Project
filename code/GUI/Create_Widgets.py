from PyQt5 import QtCore, QtGui, QtWidgets

#Creating necessary widgets with style elements

class CreateWidgets():

    @staticmethod    
    def create_Label():
        label = QtWidgets.QLabel()
        label.setAlignment(QtCore.Qt.AlignCenter)
        label.setWordWrap(True)
        label.setStyleSheet(
            """
            font-family: Ubuntu mono;
            color: #ffffff;
            padding: 0px;
            margin: 0px;
            """
        )
        return label
    
    @staticmethod
    def create_Button():
        button = QtWidgets.QPushButton()
        button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        button.setStyleSheet(
            """
            *{
                background: '#60dcb5';
                border-radius: 25px;
                font-size: 25px;
                font-family: Ubuntu mono;
                color: #000000;
                padding: 15px 15px;
                
            }
            *:hover{
                background: '#084c91';
                color: #ffffff;
            }
            """
        )
        return button

    @staticmethod
    def create_Progressbar():
        pbar = QtWidgets.QProgressBar()
        pbar.setStyleSheet(
            """
            *{
                border: 2px solid black;
                border-radius: 5px;
                background: '#dddddd';
                height: 75px;
                text-align: center;
                font-size: 20px;
                margin-left: 200px;
                margin-right: 200px;
            }
            *:chunk {
                background: '#60dcb5';
                width: 10px;
                margin: 0.5px;
            }
            """
        )
        return pbar
        
    @staticmethod
    def create_TextBox():
        textbox =  QtWidgets.QLineEdit()
        textbox.setStyleSheet(
            """
                border: 2px solid black;
                background: '#ffffff';
                font-size: 20px;
                border-radius: 5px;
                height: 50px;
                
            """)
        return textbox
    
    @staticmethod
    def create_MultiTextBox():
        multi_textbox =  QtWidgets.QTextEdit()
        multi_textbox.setStyleSheet(
            """
                border: 2px solid black;
                background: '#ffffff';
                font-size: 20px;
                border-radius: 5px;
                height: 50px;
                
            """)
        return multi_textbox
    
    @staticmethod
    def create_Radio():
        radio = QtWidgets.QRadioButton()
        radio.setFont(QtGui.QFont("Ubuntu mono", 25))
        radio.setStyleSheet(
            """
                *{
                color: #ffffff;
                }
                *:indicator {
                    width: 30px;
                    height: 30px;
                    padding-left: 50px;
                }
                *:indicator::unchecked {
                    image: url(images/radio-button-unchecked.png);
                }
                *:indicator::checked {
                    image: url(images/radio-button-checked.png);
                }
            """    
        
        )
        return radio

    @staticmethod
    def create_DropDown():
        dropdown = QtWidgets.QComboBox()
        dropdown.view().setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        dropdown.setStyleSheet(
            """
               *{ 
                   background: '#ffffff';
                   min-width: 6em;
                   height: 50px;
                   border: 2px solid black;
                   border-radius: 5px;
                   font-size: 20px;
                   font-family: Ubuntu mono;
                }
               
               *:on { 
                    padding-top: 3px;
                    padding-left: 4px;
                }
               
               * QAbstractItemView {
                   border: 2px solid black;
                   border-radius: 5px;
                   selection-background-color: lightgray;
                 }
               
               
              *:drop-down {
                   border-left-width: 1px;
                   border-left-color:black;
                   border-left-style: solid;
                   border-top-right-radius: 5px;
                   border-bottom-right-radius: 5px;
            }
              *:down-arrow {
                  image: url(images/dropdown-arrow.png);
                  width: 15px;
                  height: 15px;
                
            }
               * QScrollBar:vertical {
                   width: 0px;
                   height: 0px;
            }
        """
        )
        return dropdown
    
    @staticmethod
    def create_CheckBox():
        check_box = QtWidgets.QCheckBox()
        check_box.setFont(QtGui.QFont("Ubuntu mono", 15))
        check_box.setStyleSheet(
            """
              *{
                color: #ffffff;
                }
            
              *:indicator {
                height: 30px;
                width: 30px;
                }
              *:indicator::unchecked {
                    image: url(images/checkbox-unchecked.png);
                }
                *:indicator::checked {
                    image: url(images/checkbox-checked.png);
                }
            """
        )
        return check_box