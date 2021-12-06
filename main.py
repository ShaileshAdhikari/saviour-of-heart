# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Main_page.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from risk_score import Ui_Risk_window


class Ui_Dialog(object):
    def open_risk_window(self):
        self.window = QtWidgets.QDialog()
        self.Age = int(self.age.toPlainText())
        self.Sbp = int(self.SBP.toPlainText())
        self.Hdl = int(self.HDL.toPlainText())
        self.Tcl = int(self.TCL.toPlainText())
        if self.GMale.isChecked():
            self.Gender = 0
            self.dGender = "Male"
        else:
            self.Gender = 1
            self.dGender = "Female"

        if self.SYes.isChecked():
            self.Smoke = 1
            self.dSmoke = "Yes" 
        else:
            self.Smoke = 0
            self.dSmoke = "No"

        if self.HYes.isChecked():
            self.Toh = 1
            self.dToh = "Yes"
        else:
            self.Toh = 0
            self.dToh = "No"
        if self.DYes.isChecked():
            self.Diabetes = 1
            self.dDiabetes = "Yes"
        else:
            self.Diabetes = 0
            self.dDiabetes = "No"
    
        self.ui = Ui_Risk_window(self.Age, self.Sbp, self.Hdl, self.Tcl, self.Gender, self.Smoke, self.Toh,
                                 self.Diabetes,self.dGender, self.dSmoke, self.dToh,self.dDiabetes)
        self.ui.setupUi(self.window)
        self.window.show()
    
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1343, 583)
        font = QtGui.QFont()
        font.setPointSize(18)
        Dialog.setFont(font)
        Dialog.setStyleSheet("background-image: url(:/newPrefix/heart.jpg);\n""")
        Dialog.setSizeGripEnabled(False)
        Dialog.setModal(True)
        self.age = QtWidgets.QTextEdit(Dialog)
        self.age.setGeometry(QtCore.QRect(390, 130, 191, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.age.setFont(font)
        self.age.setPlaceholderText("")
        self.age.setObjectName("age")
        self.SBP = QtWidgets.QTextEdit(Dialog)
        self.SBP.setGeometry(QtCore.QRect(390, 220, 191, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.SBP.setFont(font)
        self.SBP.setObjectName("SBP")
        self.HDL = QtWidgets.QTextEdit(Dialog)
        self.HDL.setGeometry(QtCore.QRect(390, 310, 191, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.HDL.setFont(font)
        self.HDL.setObjectName("HDL")
        self.TCL = QtWidgets.QTextEdit(Dialog)
        self.TCL.setGeometry(QtCore.QRect(390, 400, 191, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.TCL.setFont(font)
        self.TCL.setObjectName("TCL")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(50, 120, 311, 81))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.label.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(50, 210, 311, 81))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(16)
        self.label_2.setFont(font)
        self.label_2.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.label_2.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(50, 300, 311, 81))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(16)
        self.label_3.setFont(font)
        self.label_3.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.label_3.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(60, 390, 311, 81))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(16)
        self.label_4.setFont(font)
        self.label_4.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.label_4.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(500, 10, 401, 41))
        font = QtGui.QFont()
        font.setFamily("Lucida Bright")
        font.setPointSize(26)
        self.label_5.setFont(font)
        self.label_5.setAutoFillBackground(False)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(270, 60, 861, 41))
        font = QtGui.QFont()
        font.setFamily("MS Reference Sans Serif")
        font.setPointSize(16)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.GMale = QtWidgets.QRadioButton(Dialog)
        self.GMale.setGeometry(QtCore.QRect(630, 150, 71, 41))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(14)
        self.GMale.setFont(font)
        self.GMale.setCheckable(True)
        self.GMale.setObjectName("GMale")
        self.buttonGroup_2 = QtWidgets.QButtonGroup(Dialog)
        self.buttonGroup_2.setObjectName("buttonGroup_2")
        self.buttonGroup_2.addButton(self.GMale)
        self.SYes = QtWidgets.QRadioButton(Dialog)
        self.SYes.setGeometry(QtCore.QRect(630, 240, 51, 41))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(14)
        self.SYes.setFont(font)
        self.SYes.setCheckable(True)
        self.SYes.setObjectName("SYes")
        self.buttonGroup = QtWidgets.QButtonGroup(Dialog)
        self.buttonGroup.setObjectName("buttonGroup")
        self.buttonGroup.addButton(self.SYes)
        self.SNo = QtWidgets.QRadioButton(Dialog)
        self.SNo.setGeometry(QtCore.QRect(760, 240, 51, 41))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(14)
        self.SNo.setFont(font)
        self.SNo.setCheckable(True)
        self.SNo.setObjectName("SNo")
        self.buttonGroup.addButton(self.SNo)
        self.HNo = QtWidgets.QRadioButton(Dialog)
        self.HNo.setGeometry(QtCore.QRect(760, 330, 51, 41))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(14)
        self.HNo.setFont(font)
        self.HNo.setCheckable(True)
        self.HNo.setObjectName("HNo")
        self.buttonGroup_3 = QtWidgets.QButtonGroup(Dialog)
        self.buttonGroup_3.setObjectName("buttonGroup_3")
        self.buttonGroup_3.addButton(self.HNo)
        self.DNo = QtWidgets.QRadioButton(Dialog)
        self.DNo.setGeometry(QtCore.QRect(760, 420, 51, 41))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(14)
        self.DNo.setFont(font)
        self.DNo.setCheckable(True)
        self.DNo.setObjectName("DNo")
        self.buttonGroup_4 = QtWidgets.QButtonGroup(Dialog)
        self.buttonGroup_4.setObjectName("buttonGroup_4")
        self.buttonGroup_4.addButton(self.DNo)
        self.HYes = QtWidgets.QRadioButton(Dialog)
        self.HYes.setGeometry(QtCore.QRect(630, 330, 51, 41))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(14)
        self.HYes.setFont(font)
        self.HYes.setCheckable(True)
        self.HYes.setObjectName("HYes")
        self.buttonGroup_3.addButton(self.HYes)
        self.DYes = QtWidgets.QRadioButton(Dialog)
        self.DYes.setGeometry(QtCore.QRect(630, 420, 51, 41))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(14)
        self.DYes.setFont(font)
        self.DYes.setCheckable(True)
        self.DYes.setObjectName("DYes")
        self.buttonGroup_4.addButton(self.DYes)
        self.Female = QtWidgets.QRadioButton(Dialog)
        self.Female.setGeometry(QtCore.QRect(760, 150, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(14)
        self.Female.setFont(font)
        self.Female.setCheckable(True)
        self.Female.setObjectName("Female")
        self.buttonGroup_2.addButton(self.Female)
        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setGeometry(QtCore.QRect(630, 130, 91, 21))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(16)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(Dialog)
        self.label_8.setGeometry(QtCore.QRect(630, 220, 141, 21))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(Dialog)
        self.label_9.setGeometry(QtCore.QRect(630, 300, 261, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(Dialog)
        self.label_10.setGeometry(QtCore.QRect(630, 390, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.line = QtWidgets.QFrame(Dialog)
        self.line.setGeometry(QtCore.QRect(590, 130, 41, 321))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.line.setFont(font)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(Dialog)
        self.line_2.setGeometry(QtCore.QRect(900, 130, 20, 321))
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.label_11 = QtWidgets.QLabel(Dialog)
        self.label_11.setGeometry(QtCore.QRect(930, 140, 401, 71))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(13)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(Dialog)
        self.label_12.setGeometry(QtCore.QRect(930, 360, 401, 31))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(13)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.line_3 = QtWidgets.QFrame(Dialog)
        self.line_3.setGeometry(QtCore.QRect(930, 240, 401, 16))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.line_4 = QtWidgets.QFrame(Dialog)
        self.line_4.setGeometry(QtCore.QRect(930, 350, 401, 16))
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.label_13 = QtWidgets.QLabel(Dialog)
        self.label_13.setGeometry(QtCore.QRect(930, 260, 401, 81))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(13)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(610, 490, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("calculate")
        #to show risk window when clicked
        self.pushButton.clicked.connect(self.open_risk_window)
        
        # self.pushButton_2 = QtWidgets.QPushButton(Dialog)
       # self.pushButton_2.setGeometry(QtCore.QRect(0, 0, 75, 23))
       # self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(Dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(790, 490, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.age.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:16pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8.25pt;\"><br /></p></body></html>"))
        self.SBP.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:16pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8.25pt;\"><br /></p></body></html>"))
        self.HDL.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:16pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8.25pt;\"><br /></p></body></html>"))
        self.TCL.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:16pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8.25pt;\"><br /></p></body></html>"))
        self.label.setText(_translate("Dialog", "What is your age?\n"
"(Applicable for age range: 30-74)"))
        self.label_2.setText(_translate("Dialog", "Systolic Blood Pressure (SBP)\n"
"(in mmHg, Normal range: 100-140)"))
        self.label_3.setText(_translate("Dialog", "HDL Cholesterol Level\n"
"(in mg/dl, Normal range: 35-60)"))
        self.label_4.setText(_translate("Dialog", "TCL Cholesterol Level\n"
"(in mg/dl, Normal range: 200-240)"))
        self.label_5.setText(_translate("Dialog", "SAVIOR OF THE HEART"))
        self.label_6.setText(_translate("Dialog", "Machine Learning approach for determining the risk of having ASCVD in 10 years"))
        self.GMale.setText(_translate("Dialog", "Male"))
        self.SYes.setText(_translate("Dialog", "Yes"))
        self.SNo.setText(_translate("Dialog", "No"))
        self.HNo.setText(_translate("Dialog", "No"))
        self.DNo.setText(_translate("Dialog", "No"))
        self.HYes.setText(_translate("Dialog", "Yes"))
        self.DYes.setText(_translate("Dialog", "Yes"))
        self.Female.setText(_translate("Dialog", "Female"))
        self.label_7.setText(_translate("Dialog", "Gender"))
        self.label_8.setText(_translate("Dialog", "Do you smoke?"))
        self.label_9.setText(_translate("Dialog", "Treatment of Hypertension?"))
        self.label_10.setText(_translate("Dialog", "Do you have Diabetes?"))
        self.label_11.setText(_translate("Dialog", "This calculator is based on Framingham Heart Study\n"
" Find out more on:\n"
" https://www.framinghamheartstudy.org/"))
        self.label_12.setText(_translate("Dialog", "Know how individual parameter affects the risk score"))
        self.label_13.setText(_translate("Dialog", "Validation of Framingham Heart Study for\n"
" Asian Population\n"
"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2465638/"))
        self.pushButton.setText(_translate("Dialog", "Calculate"))
        # self.pushButton_2.setText(_translate("Dialog", "Calculate"))
        self.pushButton_3.setText(_translate("Dialog", "Cancel"))
#import heart_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
