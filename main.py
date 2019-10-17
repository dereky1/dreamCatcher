from PyQt5.QtWidgets import (QApplication, QHeaderView, QAbstractItemView, QTabWidget,QListWidget, QWidget, QTableWidget, QPushButton, QRadioButton, QGridLayout, QHBoxLayout, QVBoxLayout, QLabel, QLineEdit, QMainWindow, QFrame, QPlainTextEdit)
from PyQt5.QtGui import (QIcon)
import sys

"""

TODO: Past Tab needs more efficient widget to show dreams

        Change date entry into dropdown dates

        Reading from existing savefile

        Current Tab

"""

class dreamObject:
    def __init__(self, newTitle, newSubject, newDate, newNightmare, newDescription):
        self.title = newTitle
        self.subject = newSubject
        self.date = newDate
        self.nightmare = newNightmare
        self.description = newDescription

class Home(QWidget):
    def __init__(self):
        super().__init__()
        self.title = "dream Catcher"
        self.width = 900
        self.height = 600
        self.dreamCabinet = []
        self.layout = QHBoxLayout()
        self.initUI()
        self.show()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.resize(self.width,self.height)
        self.setWindowIcon(QIcon('icon.png'))
        tabWidget = QTabWidget()

        tab1 = QWidget()
        tab1Lay = QGridLayout()
        tab1Lay.addLayout(self.createTextHeader(),0,0,1,3)
        tab1Lay.addLayout(self.createTextBox(),1,0,3,4)
        tab1Lay.addLayout(self.createNotification(),4,1,1,2)
        tab1Lay.addLayout(self.createSubmit(),4,3,1,1)
        tab1.setLayout(tab1Lay)

        tab3 = QWidget()
        tab3Lay = QVBoxLayout()
        tab3Lay.addLayout(self.createPastTable())
        tab3.setLayout(tab3Lay)

        #Cuurrent Dream
        tab2 = QWidget()
        tab2Lay = QVBoxLayout()
        tab2Lay.addLayout(self.createCurrent())
        tab2.setLayout(tab2Lay)

        ####Settings
        tab4 = QWidget()
        tab4Lay = QVBoxLayout()
        tab4Lay.addLayout(self.createSettings())
        tab4.setLayout(tab4Lay)

        tabWidget.addTab(tab1, "Home")
        tabWidget.addTab(tab2, "Current")
        tabWidget.addTab(tab3, "Past")
        tabWidget.addTab(tab4, "Settings")

        self.layout.addWidget(tabWidget)
        self.setLayout(self.layout)

    def createTextHeader(self):
        headerLayout = QHBoxLayout()
        titleLabel = QLabel("Title")
        self.titleBox = QLineEdit()
        subjectLabel = QLabel("Subject")
        self.subjectBox = QLineEdit()
        dateLabel = QLabel("Date")
        self.dateBox = QLineEdit()
        self.nightmareCheck = QRadioButton("Nightmare")
        headerLayout.addWidget(titleLabel)
        headerLayout.addWidget(self.titleBox)
        headerLayout.addWidget(subjectLabel)
        headerLayout.addWidget(self.subjectBox)
        headerLayout.addWidget(dateLabel)
        headerLayout.addWidget(self.dateBox)
        headerLayout.addWidget(self.nightmareCheck)
        return headerLayout

    def createTextBox(self):
        textLayout = QVBoxLayout()
        textLabel = QLabel("Your Dream Starts Here: ")
        self.textBox = QPlainTextEdit()
        textLayout.addWidget(textLabel)
        textLayout.addWidget(self.textBox)
        return textLayout

    def createSubmit(self):
        submitLayout = QHBoxLayout()
        submitButton = QPushButton("Add to Dreams")
        submitButton.clicked.connect(self.dreamCreation)
        submitLayout.addWidget(submitButton)
        return submitLayout

    def createNotification(self):
        notificationLayout = QHBoxLayout()
        self.notification = QLabel()
        notificationLayout.addWidget(self.notification)
        return notificationLayout

    #### Create Layout for past tab
    def createPastTable(self):
        pastHeaderLayout = QGridLayout()
        """table = QTableWidget(10,3)
        table.setHorizontalHeaderLabels(["Date","Subject","Title"])
        table.setShowGrid(False)
        header = table.horizontalHeader()
        header.setSectionResizeMode(0, QHeaderView.Stretch)
        header.setSectionResizeMode(1, QHeaderView.Stretch)
        header.setSectionResizeMode(2, QHeaderView.Stretch)
        table.setSelectionBehavior(QAbstractItemView.SelectRows)
        pastHeaderLayout.addWidget(table)"""

        self.past = QListWidget()
        self.past.addItem("#   Date\t\tTitle\t\tSubject")
        pastHeaderLayout.addWidget(self.past)

        return pastHeaderLayout


    #####SETTINGs Tab
    def createSettings(self):
        settingsLayout = QVBoxLayout()
        exportButton = QPushButton("Save Dream")
        self.notification4 = QLabel()
        exportButton.clicked.connect(self.saveDreams)
        settingsLayout.addWidget(exportButton)
        settingsLayout.addWidget(self.notification4)
        return settingsLayout

    ####### Current tab
    def createCurrent(self):
        currentLayout = QVBoxLayout()
        currentView = QListWidget()
        currentLayout.addWidget(currentView)
        return currentLayout

    ###### Dreams functions
    def clearDream(self):
        self.titleBox.setText("")
        self.subjectBox.setText("")
        self.dateBox.setText("")
        self.nightmareCheck.setChecked(False)
        self.textBox.setPlainText("")
        self.notification.setText("")

    #def saveDream(self, dream):
    #    newDream =

    ###### Button onclick methods
    def dreamCreation(self):
        dreamTitle = self.titleBox.text()
        newDream = dreamObject(dreamTitle, self.subjectBox.text(), self.dateBox.text(), self.nightmareCheck.isChecked(), self.textBox.toPlainText())
        self.dreamCabinet.append(newDream)
        self.clearDream()
        self.notification.setText('Dream " {title}" has been recorded'.format(title=dreamTitle))
        #self.printDreams()

    ###### i/o
    def saveDreams(self):
        try:
            self.saveFile = open("record.dreams", "w+")
            for i in range(0,len(self.dreamCabinet)):
                self.saveFile.write("{index};{title};{subject};{date};{nightmare};{desc}\n".format(index=i+1, title=self.dreamCabinet[i].title, subject=self.dreamCabinet[i].subject, date=self.dreamCabinet[i].date, nightmare=self.dreamCabinet[i].nightmare, desc=self.dreamCabinet[i].description))
            self.notification4.setText('Dreams have been saved to "record.dreams"')
            self.saveFile.close()
        except:
            self.notification4.setText("There was a problem saving dreams")


    ##### debug functions
    def printDreams(self):
        for i in range(len(self.dreamCabinet)):
            print("Dream #{index}:\nTitle: {title}\nSubject: {subject}\nDate: {date}\nNightmare: {nightmare}\nDescription: {desc}".format(index=i+1, title=self.dreamCabinet[i].title, subject=self.dreamCabinet[i].subject, date=self.dreamCabinet[i].date, nightmare=self.dreamCabinet[i].nightmare, desc=self.dreamCabinet[i].description))


def main():
    app = QApplication([])
    home = Home()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
