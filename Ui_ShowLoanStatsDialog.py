# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\ShowLoanStatsDialog.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ShowLoanStatsDialog(object):
    def setupUi(self, ShowLoanStatsDialog):
        ShowLoanStatsDialog.setObjectName("ShowLoanStatsDialog")
        ShowLoanStatsDialog.resize(400, 400)
        ShowLoanStatsDialog.setMinimumSize(QtCore.QSize(400, 400))
        font = QtGui.QFont()
        font.setFamily("B Nazanin")
        font.setPointSize(12)
        ShowLoanStatsDialog.setFont(font)
        ShowLoanStatsDialog.setLayoutDirection(QtCore.Qt.RightToLeft)
        ShowLoanStatsDialog.setLocale(QtCore.QLocale(QtCore.QLocale.Persian, QtCore.QLocale.Iran))
        self.verticalLayout = QtWidgets.QVBoxLayout(ShowLoanStatsDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tbl_sections = QtWidgets.QTableWidget(ShowLoanStatsDialog)
        self.tbl_sections.setObjectName("tbl_sections")
        self.tbl_sections.setColumnCount(3)
        self.tbl_sections.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("B Nazanin")
        font.setPointSize(12)
        item.setFont(font)
        self.tbl_sections.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("B Nazanin")
        font.setPointSize(12)
        item.setFont(font)
        self.tbl_sections.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("B Nazanin")
        font.setPointSize(12)
        item.setFont(font)
        self.tbl_sections.setHorizontalHeaderItem(2, item)
        self.verticalLayout.addWidget(self.tbl_sections)
        self.hlay_buttons = QtWidgets.QHBoxLayout()
        self.hlay_buttons.setObjectName("hlay_buttons")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.hlay_buttons.addItem(spacerItem)
        self.btn_back = QtWidgets.QPushButton(ShowLoanStatsDialog)
        self.btn_back.setObjectName("btn_back")
        self.hlay_buttons.addWidget(self.btn_back)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.hlay_buttons.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.hlay_buttons)

        self.retranslateUi(ShowLoanStatsDialog)
        QtCore.QMetaObject.connectSlotsByName(ShowLoanStatsDialog)

    def retranslateUi(self, ShowLoanStatsDialog):
        _translate = QtCore.QCoreApplication.translate
        ShowLoanStatsDialog.setWindowTitle(_translate("ShowLoanStatsDialog", "آمار امانت کتاب از بخش‌ها"))
        item = self.tbl_sections.horizontalHeaderItem(0)
        item.setText(_translate("ShowLoanStatsDialog", "کد بخش"))
        item = self.tbl_sections.horizontalHeaderItem(1)
        item.setText(_translate("ShowLoanStatsDialog", "نام بخش"))
        item = self.tbl_sections.horizontalHeaderItem(2)
        item.setText(_translate("ShowLoanStatsDialog", "تعداد امانت"))
        self.btn_back.setText(_translate("ShowLoanStatsDialog", "بازگشت"))
