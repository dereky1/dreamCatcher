from PyQt5.QtWidgets import (QApplication, QHeaderView, QAbstractItemView, QTabWidget,QListWidget, QWidget, QTableWidget, QPushButton, QRadioButton, QGridLayout, QHBoxLayout, QVBoxLayout, QLabel, QLineEdit, QMainWindow, QFrame, QPlainTextEdit)
import sys

class Home(QWidget):
    def __init__(self):
        super().__init__()
        self.title = "dream Catcher"
        self.width = 900
        self.height = 600
        self.layout = QHBoxLayout()
        self.initUI()
        self.show()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.resize(self.width,self.height)
        tabWidget = QTabWidget()

        tab1 = QWidget()
        tab1Lay = QGridLayout()
        tab1Lay.addLayout(self.createTextHeader(),0,0,1,3)
        tab1Lay.addLayout(self.createTextBox(),1,0,3,4)
        tab1Lay.addLayout(self.createSubmit(),4,3,1,1)
        tab1.setLayout(tab1Lay)

        tab2 = QWidget()
        tab2Lay = QVBoxLayout()
        tab2Lay.addLayout(self.createPastTable())
        tab2.setLayout(tab2Lay)

        #Cuurrent Dream
        tab3 = QWidget()

        ####Settings
        tab4 = QWidget()

        tabWidget.addTab(tab1, "Home")
        tabWidget.addTab(tab2, "Past")
        tabWidget.addTab(tab3, "Current")
        tabWidget.addTab(tab4, "Settings")


        self.layout.addWidget(tabWidget)
        self.setLayout(self.layout)


    def createTextHeader(self):
        headerLayout = QHBoxLayout()
        titleLabel = QLabel("Title")
        titleBox = QLineEdit()
        subjectLabel = QLabel("Subject")
        subjectBox = QLineEdit()
        dateLabel = QLabel("Date")
        dateBox = QLineEdit()
        nightmareCheck = QRadioButton("Nightmare")
        headerLayout.addWidget(titleLabel)
        headerLayout.addWidget(titleBox)
        headerLayout.addWidget(subjectLabel)
        headerLayout.addWidget(subjectBox)
        headerLayout.addWidget(dateLabel)
        headerLayout.addWidget(dateBox)
        headerLayout.addWidget(nightmareCheck)
        return headerLayout

    def createTextBox(self):
        textLayout = QVBoxLayout()
        textLabel = QLabel("Your Dream Starts Here: ")
        textBox = QPlainTextEdit()
        textLayout.addWidget(textLabel)
        textLayout.addWidget(textBox)
        return textLayout

    def createSubmit(self):
        submitLayout = QHBoxLayout()
        submitButton = QPushButton("Add to Dreams")
        submitLayout.addWidget(submitButton)
        return submitLayout

    #### Create Layout for past tab
    def createPastTable(self):
        pastHeaderLayout = QGridLayout()
        table = QTableWidget(10,3)
        table.setHorizontalHeaderLabels(["Date","Subject","Title"])
        table.setShowGrid(False)
        header = table.horizontalHeader()
        header.setSectionResizeMode(0, QHeaderView.Stretch)
        header.setSectionResizeMode(1, QHeaderView.Stretch)
        header.setSectionResizeMode(2, QHeaderView.Stretch)
        table.setSelectionBehavior(QAbstractItemView.SelectRows)
        pastHeaderLayout.addWidget(table)
        return pastHeaderLayout

    ###### Button onclick methods


    ###### layout management


def main():
    app = QApplication([])
    home = Home()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
