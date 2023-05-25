# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\UserSearchDialog.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_UserSearchDialog(object):
    def setupUi(self, UserSearchDialog):
        UserSearchDialog.setObjectName("UserSearchDialog")
        UserSearchDialog.resize(308, 148)
        font = QtGui.QFont()
        font.setFamily("B Nazanin")
        font.setPointSize(12)
        UserSearchDialog.setFont(font)
        UserSearchDialog.setLayoutDirection(QtCore.Qt.RightToLeft)
        UserSearchDialog.setLocale(QtCore.QLocale(QtCore.QLocale.Persian, QtCore.QLocale.Iran))
        self.verticalLayout = QtWidgets.QVBoxLayout(UserSearchDialog)
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.verticalLayout.setObjectName("verticalLayout")
        self.flay_inputs = QtWidgets.QFormLayout()
        self.flay_inputs.setSizeConstraint(QtWidgets.QLayout.SetMinAndMaxSize)
        self.flay_inputs.setObjectName("flay_inputs")
        self.lbl_title = QtWidgets.QLabel(UserSearchDialog)
        self.lbl_title.setObjectName("lbl_title")
        self.flay_inputs.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.lbl_title)
        self.txt_title = QtWidgets.QLineEdit(UserSearchDialog)
        self.txt_title.setClearButtonEnabled(True)
        self.txt_title.setObjectName("txt_title")
        self.flay_inputs.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.txt_title)
        self.lbl_author = QtWidgets.QLabel(UserSearchDialog)
        self.lbl_author.setObjectName("lbl_author")
        self.flay_inputs.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.lbl_author)
        self.txt_author = QtWidgets.QLineEdit(UserSearchDialog)
        self.txt_author.setClearButtonEnabled(True)
        self.txt_author.setObjectName("txt_author")
        self.flay_inputs.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.txt_author)
        self.verticalLayout.addLayout(self.flay_inputs)
        self.hlay_buttons = QtWidgets.QHBoxLayout()
        self.hlay_buttons.setObjectName("hlay_buttons")
        self.btn_search = QtWidgets.QPushButton(UserSearchDialog)
        self.btn_search.setObjectName("btn_search")
        self.hlay_buttons.addWidget(self.btn_search)
        self.btn_back = QtWidgets.QPushButton(UserSearchDialog)
        self.btn_back.setObjectName("btn_back")
        self.hlay_buttons.addWidget(self.btn_back)
        self.verticalLayout.addLayout(self.hlay_buttons)

        self.retranslateUi(UserSearchDialog)
        QtCore.QMetaObject.connectSlotsByName(UserSearchDialog)

    def retranslateUi(self, UserSearchDialog):
        _translate = QtCore.QCoreApplication.translate
        UserSearchDialog.setWindowTitle(_translate("UserSearchDialog", "جست‌وجوی کتاب"))
        self.lbl_title.setText(_translate("UserSearchDialog", "عنوان کتاب"))
        self.lbl_author.setText(_translate("UserSearchDialog", "نویسنده"))
        self.btn_search.setText(_translate("UserSearchDialog", "جست‌وجو"))
        self.btn_back.setText(_translate("UserSearchDialog", "بازگشت"))
