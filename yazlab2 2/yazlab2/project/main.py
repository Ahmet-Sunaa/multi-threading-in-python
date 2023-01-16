import sys
import time
from PyQt6 import QtCore, QtGui, QtWidgets, uic
from modules.inputCheck import isfloatAble, isintegerAble
from modules.threadOperations import createThreads, createThreadsForSpecific, createThreadsForQuery
from modules.similartyCheck import similarityCheck
from modules.bigDataOperations import dataOperations
import multiprocessing


class resultWindow(QtWidgets.QMainWindow):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        uic.loadUi("resultwindow.ui", self)
        self.setWindowTitle("Sonuç Ekranı")
        self.ozelliklabel.setText("Sonuçlarınız:")
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.setColumnWidth(0, 200)
        self.tableWidget.setColumnWidth(1, 200)
        self.tableWidget.setColumnWidth(2, 50)
        self.tableWidget.setColumnWidth(3, 100)


class MainWindow(QtWidgets.QMainWindow):

    def __init__(self, *args, **kwargs):
        self.similarityRate = 0
        self.threadNumber = 0
        self.column1 = ""
        self.column2 = ""
        self.column3 = ""
        self.column4 = ""
        self.queryValue = 0

        super().__init__(*args, **kwargs)
        uic.loadUi("mainwindow.ui", self)
        self.setWindowTitle("Özellik Seçim Ekranı")
        self.Startprogram.clicked.connect(self.resultwindow)
        self.pushButton.clicked.connect(self.resultOfQuery)
        self.pushButton_2.clicked.connect(self.resultOfSql)

    def resultwindow(self):
        if self.plainTextEdit.toPlainText().replace("%", "") != '' and isfloatAble(self.plainTextEdit.toPlainText().replace("%", "")) and isintegerAble(self.threadcombobox.currentText()):
            self.similarityRate = float(
                self.plainTextEdit.toPlainText().replace("%", ""))
            self.threadNumber = int(self.threadcombobox.currentText())
            self.column1 = self.comboBox.currentText()
            results ,job_time = createThreads(function=similarityCheck, threadNumber=self.threadNumber,
                                    column1=self.column1, similarityRate=self.similarityRate)
            tableRow = 0
            self.window = resultWindow()
            self.window.tableWidget.setRowCount(len(results))
            print(job_time)
            self.window.ozelliklabel.setText(
                "İşleminiz "+"{:.3f}".format(job_time)+" saniyede tamamlandı")
            for result in results:
                self.window.tableWidget.setItem(
                    tableRow, 0, QtWidgets.QTableWidgetItem(result[1]))
                self.window.tableWidget.setItem(
                    tableRow, 1, QtWidgets.QTableWidgetItem(result[2]))
                self.window.tableWidget.setItem(
                    tableRow, 2, QtWidgets.QTableWidgetItem(str(result[0]*100)))
                tableRow += 1
            self.window.show()
        else:
            print("Hatalı değer ")

    def resultOfQuery(self):
        self.column2 = self.comboBox_3.currentText()
        self.column3 = self.comboBox_4.currentText()
        self.queryValue = int(self.plainTextEdit_2.toPlainText())
        self.similarityRate = float(
            self.plainTextEdit.toPlainText().replace("%", ""))
        self.threadNumber = int(self.threadcombobox.currentText())
        results,job_time = createThreadsForSpecific(function=similarityCheck, threadNumber=self.threadNumber, variable=self.queryValue,
                                           column1=self.column2, column2=self.column3, similarityRate=self.similarityRate)
        tableRow = 0
        self.window = resultWindow()
        self.window.ozelliklabel.setText(
            "İşleminiz "+"{:.3f}".format(job_time)+" saniyede tamamlandı")
        self.window.tableWidget.setRowCount(len(results))
        for result in results:
            self.window.tableWidget.setItem(
                tableRow, 0, QtWidgets.QTableWidgetItem(result[1]))
            self.window.tableWidget.setItem(
                tableRow, 1, QtWidgets.QTableWidgetItem(result[2]))
            self.window.tableWidget.setItem(
                tableRow, 2, QtWidgets.QTableWidgetItem(str(result[0]*100)))
            tableRow += 1
        self.window.show()

    def resultOfSql(self):
        self.column2 = self.comboBox_2.currentText()
        self.column3 = self.comboBox_6.currentText()
        self.column4 = self.comboBox_5.currentText()
        self.similarityRate = float(
            self.plainTextEdit.toPlainText().replace("%", ""))
        self.threadNumber = int(self.threadcombobox.currentText())
        df = dataOperations()
        results,job_time = createThreadsForQuery(df=df,function=similarityCheck, threadNumber=self.threadNumber, column1=self.column2,
                                        column2=self.column3, column3=self.column4, similarityRate=self.similarityRate)
        tableRow = 0
        self.window = resultWindow()
        self.window.ozelliklabel.setText(
            "İşleminiz "+"{:.3f}".format(job_time)+" saniyede tamamlandı")
        self.window.tableWidget.setRowCount(len(results[0][3]))
        for result in results:
            print(result)
            self.window.tableWidget.setItem(
                tableRow, 0, QtWidgets.QTableWidgetItem(result[1]))
            self.window.tableWidget.setItem(
                tableRow, 1, QtWidgets.QTableWidgetItem(result[2]))
            self.window.tableWidget.setItem(
                tableRow, 2, QtWidgets.QTableWidgetItem(str(result[0]*100)))
            for res in result[3]:
                self.window.tableWidget.setItem(
                    tableRow, 3, QtWidgets.QTableWidgetItem(res))
                tableRow += 1
        self.window.show()


if __name__ == "__main__":
    multiprocessing.freeze_support()
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()
