# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\ShowMembersDialog.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ShowMembersDialog(object):
    def setupUi(self, ShowMembersDialog):
        ShowMembersDialog.setObjectName("ShowMembersDialog")
        ShowMembersDialog.resize(851, 418)
        font = QtGui.QFont()
        font.setFamily("B Nazanin")
        font.setPointSize(12)
        ShowMembersDialog.setFont(font)
        ShowMembersDialog.setLayoutDirection(QtCore.Qt.RightToLeft)
        ShowMembersDialog.setLocale(QtCore.QLocale(QtCore.QLocale.Persian, QtCore.QLocale.Iran))
        self.verticalLayout = QtWidgets.QVBoxLayout(ShowMembersDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tbl_members = QtWidgets.QTableWidget(ShowMembersDialog)
        self.tbl_members.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tbl_members.setObjectName("tbl_members")
        self.tbl_members.setColumnCount(6)
        self.tbl_members.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("B Nazanin")
        font.setPointSize(12)
        item.setFont(font)
        self.tbl_members.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("B Nazanin")
        font.setPointSize(12)
        item.setFont(font)
        self.tbl_members.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("B Nazanin")
        font.setPointSize(12)
        item.setFont(font)
        self.tbl_members.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("B Nazanin")
        font.setPointSize(12)
        item.setFont(font)
        self.tbl_members.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("B Nazanin")
        font.setPointSize(12)
        item.setFont(font)
        self.tbl_members.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("B Nazanin")
        font.setPointSize(12)
        item.setFont(font)
        self.tbl_members.setHorizontalHeaderItem(5, item)
        self.verticalLayout.addWidget(self.tbl_members)
        self.hlay_buttons = QtWidgets.QHBoxLayout()
        self.hlay_buttons.setObjectName("hlay_buttons")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.hlay_buttons.addItem(spacerItem)
        self.btn_delete = QtWidgets.QPushButton(ShowMembersDialog)
        self.btn_delete.setObjectName("btn_delete")
        self.hlay_buttons.addWidget(self.btn_delete)
        self.btn_back = QtWidgets.QPushButton(ShowMembersDialog)
        self.btn_back.setObjectName("btn_back")
        self.hlay_buttons.addWidget(self.btn_back)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.hlay_buttons.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.hlay_buttons)

        self.retranslateUi(ShowMembersDialog)
        QtCore.QMetaObject.connectSlotsByName(ShowMembersDialog)

    def retranslateUi(self, ShowMembersDialog):
        _translate = QtCore.QCoreApplication.translate
        ShowMembersDialog.setWindowTitle(_translate("ShowMembersDialog", "لیست اعضای کتابخانه"))
        item = self.tbl_members.horizontalHeaderItem(0)
        item.setText(_translate("ShowMembersDialog", "کد عضو"))
        item = self.tbl_members.horizontalHeaderItem(1)
        item.setText(_translate("ShowMembersDialog", "نام"))
        item = self.tbl_members.horizontalHeaderItem(2)
        item.setText(_translate("ShowMembersDialog", "نام خانوادگی"))
        item = self.tbl_members.horizontalHeaderItem(3)
        item.setText(_translate("ShowMembersDialog", "تلفن"))
        item = self.tbl_members.horizontalHeaderItem(4)
        item.setText(_translate("ShowMembersDialog", "تاریخ عضویت"))
        item = self.tbl_members.horizontalHeaderItem(5)
        item.setText(_translate("ShowMembersDialog", "آدرس"))
        self.btn_delete.setText(_translate("ShowMembersDialog", "حذف اعضای انتخاب‌شده"))
        self.btn_back.setText(_translate("ShowMembersDialog", "بازگشت"))
