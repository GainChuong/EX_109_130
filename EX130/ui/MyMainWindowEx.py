from PyQt6.QtWidgets import QMessageBox

from BTQT.EX130.ui.MyMainWindow import Ui_MainWindow
from BTQT.EX109.EX109 import dep_calc
class MyMainWindowEx(Ui_MainWindow):
    def __init__(self):
        pass
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow=MainWindow
        self.setupSignalAndSlot()
    def setupSignalAndSlot(self):
        self.pushButtonCalc.clicked.connect(self.process_dep)
        self.pushButtonDetail.clicked.connect(self.view_detail)

    def get_data(self):
        return dep_calc(
            float(self.LineEditNew.text()),
            float(self.LineEditTrans.text()),
            float(self.LineEditSetup.text()),
            int(self.LineEditYear.text())
        )
    def view_detail(self):
        try:
            *_, result_list = self.get_data()
            self.listWidget.clear()
            self.listWidget.addItems(result_list)
        except Exception as error:
            msgBox = QMessageBox()
            msgBox.setWindowTitle("Lỗi")
            msgBox.setText("Bạn có thể đang gặp lỗi")
            msgBox.setIcon(QMessageBox.Icon.Warning)
            buttons = QMessageBox.StandardButton.Yes
            msgBox.setStandardButtons(buttons)
            ret = msgBox.exec()
            if ret == QMessageBox.StandardButton.Yes:
                self.clear()
    def process_dep(self):
        try:
            org, year, month, _ = self.get_data()
            self.LineEditOrg.setText(str(round(org, 0)))
            self.LineEditYearDep.setText(str(round(year, 0)))
            self.LineEditMonthDep.setText(str(round(month, 0)))
        except Exception as error:
            msgBox = QMessageBox()
            msgBox.setWindowTitle("Lỗi")
            msgBox.setText("Bạn có thể đang gặp lỗi")
            msgBox.setIcon(QMessageBox.Icon.Warning)
            buttons = QMessageBox.StandardButton.Yes
            msgBox.setStandardButtons(buttons)
            ret = msgBox.exec()
            if ret == QMessageBox.StandardButton.Yes:
                self.clear()
    def clear(self):
        self.LineEditYear.setText("")
        self.LineEditTrans.setText("0")
        self.LineEditSetup.setText("0")
        self.LineEditNew.setText("")
        self.LineEditOrg.setText("")
        self.LineEditMonthDep.setText("")
        self.LineEditYearDep.setText("")
        self.LineEditNew.setFocus()
    def show_window(self):
        self.MainWindow.show()
