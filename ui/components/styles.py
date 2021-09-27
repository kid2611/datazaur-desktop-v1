from PyQt5.QtGui import QFont, QPalette


GLOBAL_PALETTE = QPalette()


GLOBAL_STYLE = """
                QMainWindow {   
                color: #FFFFFF;
                background-color: #061636;
                }
                QGroupBox {  
                color: #FFFFFF;
                background-color: #061226;
                font: 63 11pt "FixedsysTTF";
                }
                QPushButton {
                color: #FFFFFF;
                background-color: #063236;
                border-color: #FF0000;
                font: 63 11pt "FixedsysTTF";
                }
                QLineEdit {
                background-color: #005282;
                color: #FFFFFF;
                border-color: #FF0000;
                gridline-color: #FF0000;
                font: 63 11pt "FixedsysTTF";
                }
                QLabel {
                color: #FFFFFF;
                border-color: #FF0000;
                gridline-color: #FF0000;
                font: 63 11pt "FixedsysTTF";
                }
                QComboBox {
                background-color: #103864;
                alternate-background-color: #106438;
                selection-background-color: #641038;
                color: #FFFFFF;
                selection-color: #FFAFBF;
                border-color: #FF0000;
                gridline-color: #FF0000;
                font: 63 11pt "FixedsysTTF";

                QTableView {
                color: #FFFFFF;
                background-color: #062242;
                alternate-background-color: #106438;
                selection-background-color: #641038;
                }
                QListWidget {
                color: #FFFFFF;
                background-color: #062242;
                alternate-background-color: #106438;
                selection-background-color: #641038;
                }
                QTabWidget {
                color: #FFFFFF;
                font: 63 11pt "FixedsysTTF";
                background-color: #081824;
                alternate-background-color: #106438;
                selection-background-color: #641038;
                }
                QRadioButton {
                color: #FFFFFF;
                font: 63 10pt "FixedsysTTF";
                background-color: #061532;
                }
                
                """

STYLE2 = """QCheckBox::indicator"
                   "{"
                   "border : 2px solid rgb(0, 31, 36);"
                   "}"
                   "QCheckBox::indicator:checked"
                   "{"
                   "background-color : rgb(150, 220, 220);"
                   "color : rgb(0, 0, 255);"
                   "selection-color : rgb(255, 255, 255);"
                   "}"
                   "QCheckBox::indicator:unchecked"
                   "{"
                   "background-color : rgb(12, 46, 86);"
                   "color : rgb(0, 0, 255);"
                   "selection-color : rgb(255, 255, 255);"
                   "}"""
