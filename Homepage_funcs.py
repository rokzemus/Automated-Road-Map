import sys
import Main
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QApplication, QDialog, QMainWindow
from PyQt5.uic import loadUi




class HomePage(QMainWindow):
    def __init__(self):
        super(HomePage, self).__init__()
        loadUi('untitled.ui', self)
        self.pushButton.clicked.connect(Main.updateTable)
        tables_list = Main.table_List
        for i in range(len(tables_list)):
            self.listWidget_2.addItem(str(tables_list[i]))
        self.pushButton_2.clicked.connect(self.refreshEmp)

    def refreshEmp(self):
        employees_List = Main.employee_List
        for i in range(len(employees_List)):
            self.listWidget.addItem(str(employees_List[i]))





app = QApplication(sys.argv)
widget = HomePage()
widget.show()
sys.exit(app.exec_())