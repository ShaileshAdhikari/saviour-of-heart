from PyQt5 import QtCore, QtGui, QtWidgets
from random_forest import random_forest


class Ui_More_risk(object):
    def __init__(self, Age,SBP,HDL,TCL,Gender,Smoke,TOH,Diabetes, Risk):
        self.Age = Age
        self.SBP = SBP
        self.HDL = HDL
        self.TCL = TCL
        self.Gender = Gender
        self.Smoke = Smoke
        self.TOH = TOH
        self.Diabetes = Diabetes
        self.final_risk = Risk
    
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1343, 593)
        Dialog.setStyleSheet("background-image: url(:/newPrefix/heart.jpg);")
        self.label_22 = QtWidgets.QLabel(Dialog)
        self.label_22.setGeometry(QtCore.QRect(330, 380, 47, 21))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(18)
        self.label_22.setFont(font)
        self.label_22.setObjectName("label_22")
        self.label_11 = QtWidgets.QLabel(Dialog)
        self.label_11.setGeometry(QtCore.QRect(920, 170, 401, 71))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(13)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.label_20 = QtWidgets.QLabel(Dialog)
        self.label_20.setGeometry(QtCore.QRect(270, 300, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(18)
        self.label_20.setFont(font)
        self.label_20.setObjectName("label_20")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(270, 60, 861, 41))
        font = QtGui.QFont()
        font.setFamily("MS Reference Sans Serif")
        font.setPointSize(16)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_10 = QtWidgets.QLabel(Dialog)
        self.label_10.setGeometry(QtCore.QRect(40, 340, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.label_25 = QtWidgets.QLabel(Dialog)
        self.label_25.setGeometry(QtCore.QRect(480, 230, 371, 231))
        font = QtGui.QFont()
        font.setPointSize(72)
        self.label_25.setFont(font)
        self.label_25.setObjectName("label_25")
        self.label_8 = QtWidgets.QLabel(Dialog)
        self.label_8.setGeometry(QtCore.QRect(40, 260, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setGeometry(QtCore.QRect(40, 220, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_17 = QtWidgets.QLabel(Dialog)
        self.label_17.setGeometry(QtCore.QRect(150, 180, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(18)
        self.label_17.setFont(font)
        self.label_17.setObjectName("label_17")
        self.label_14 = QtWidgets.QLabel(Dialog)
        self.label_14.setGeometry(QtCore.QRect(40, 380, 271, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.line_4 = QtWidgets.QFrame(Dialog)
        self.line_4.setGeometry(QtCore.QRect(920, 380, 401, 16))
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.label_15 = QtWidgets.QLabel(Dialog)
        self.label_15.setGeometry(QtCore.QRect(40, 420, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.label_9 = QtWidgets.QLabel(Dialog)
        self.label_9.setGeometry(QtCore.QRect(40, 300, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.line_2 = QtWidgets.QFrame(Dialog)
        self.line_2.setGeometry(QtCore.QRect(880, 120, 20, 361))
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.label_21 = QtWidgets.QLabel(Dialog)
        self.label_21.setGeometry(QtCore.QRect(220, 340, 47, 21))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(18)
        self.label_21.setFont(font)
        self.label_21.setObjectName("label_21")
        self.label_13 = QtWidgets.QLabel(Dialog)
        self.label_13.setGeometry(QtCore.QRect(920, 290, 401, 81))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(13)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(480, 130, 221, 41))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_18 = QtWidgets.QLabel(Dialog)
        self.label_18.setGeometry(QtCore.QRect(300, 220, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(18)
        self.label_18.setFont(font)
        self.label_18.setObjectName("label_18")
        self.label_24 = QtWidgets.QLabel(Dialog)
        self.label_24.setGeometry(QtCore.QRect(480, 190, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_24.setFont(font)
        self.label_24.setObjectName("label_24")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(700, 100, 161, 91))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(36)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(500, 10, 401, 41))
        font = QtGui.QFont()
        font.setFamily("Lucida Bright")
        font.setPointSize(26)
        self.label_5.setFont(font)
        self.label_5.setAutoFillBackground(False)
        self.label_5.setObjectName("label_5")
        self.line = QtWidgets.QFrame(Dialog)
        self.line.setGeometry(QtCore.QRect(460, 120, 20, 361))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(40, 180, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(40, 140, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_16 = QtWidgets.QLabel(Dialog)
        self.label_16.setGeometry(QtCore.QRect(140, 140, 61, 31))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(18)
        self.label_16.setFont(font)
        self.label_16.setObjectName("label_16")
        self.label_12 = QtWidgets.QLabel(Dialog)
        self.label_12.setGeometry(QtCore.QRect(920, 390, 401, 31))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(13)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.label_19 = QtWidgets.QLabel(Dialog)
        self.label_19.setGeometry(QtCore.QRect(270, 260, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(18)
        self.label_19.setFont(font)
        self.label_19.setObjectName("label_19")
        self.label_23 = QtWidgets.QLabel(Dialog)
        self.label_23.setGeometry(QtCore.QRect(220, 420, 47, 21))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(18)
        self.label_23.setFont(font)
        self.label_23.setObjectName("label_23")
        self.line_3 = QtWidgets.QFrame(Dialog)
        self.line_3.setGeometry(QtCore.QRect(920, 270, 401, 16))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(550, 500, 281, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_3 = QtWidgets.QPushButton(Dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(130, 480, 181, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_22.setText(_translate("Dialog", "Yes"))
        self.label_11.setText(_translate("Dialog", "This calculator is based on Framingham Heart Study\n"
" Find out more on:\n"
" https://www.framinghamheartstudy.org/"))
        self.label_20.setText(_translate("Dialog", str(self.TCL)))
        self.label_6.setText(_translate("Dialog", "Machine Learning approach for determining the risk of having ASCVD in 10 years"))
        self.label_10.setText(_translate("Dialog", "Smoking Status :"))
        self.label_25.setText(_translate("Dialog", "XYZ"))
        self.label_8.setText(_translate("Dialog", "HDL Cholesterol Level :"))
        self.label_7.setText(_translate("Dialog", "Systolic Blood Pressure :"))
        self.label_17.setText(_translate("Dialog", "Female"))
        self.label_14.setText(_translate("Dialog", "Treatment of Hypertension :"))
        self.label_15.setText(_translate("Dialog", "Diabetes Status :"))
        self.label_9.setText(_translate("Dialog", "TCL Cholesterol Level :"))
        self.label_21.setText(_translate("Dialog", str(self.Smoke)))
        self.label_13.setText(_translate("Dialog", "Validation of Framingham Heart Study for\n"
" Asian Population\n"
"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2465638/"))
        self.label.setText(_translate("Dialog", "Your risk score is:"))
        self.label_18.setText(_translate("Dialog", str(self.SBP)))
        self.label_24.setText(_translate("Dialog", "More about Risk Score"))
        self.label_2.setText(_translate("Dialog", str(self.final_risk)))
        self.label_5.setText(_translate("Dialog", "SAVIOR OF THE HEART"))
        self.label_4.setText(_translate("Dialog", "Gender :"))
        self.label_3.setText(_translate("Dialog", "Age :"))
        self.label_16.setText(_translate("Dialog", str(self.Age)))
        self.label_12.setText(_translate("Dialog", "Know how individual parameter affects the risk score"))
        self.label_19.setText(_translate("Dialog", str(self.HDL)))
        self.label_23.setText(_translate("Dialog", str(self.Diabetes)))
        self.pushButton.setText(_translate("Dialog", "Preventive Measures"))
        self.pushButton_3.setText(_translate("Dialog", "Back to form"))
#import heart_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_More_risk()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())