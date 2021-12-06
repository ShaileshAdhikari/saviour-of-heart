# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'risk_score.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from random_forest import random_forest
from preventive_measures import Ui_Dialog_preventive
from more_risk_score import Ui_More_risk
# from Main_page1 import Ui_Dialog

class Ui_Risk_window(object):
    def __init__(self, Age,SBP,HDL,TCL,Gender,Smoke,TOH,Diabetes,dGender,dSmoke,dTOH,dDiabetes):
        self.Age = Age
        self.SBP = SBP
        self.HDL = HDL
        self.TCL = TCL
        
        self.Gender = Gender
        self.Smoke = Smoke
        self.TOH = TOH
        self.Diabetes = Diabetes
        
        self.dGender = dGender
        self.dSmoke = dSmoke
        self.dTOH = dTOH
        self.dDiabetes = dDiabetes
        print(dGender); print(dSmoke);
        
        Risk_Score = random_forest(self.Gender, self.Age, self.SBP, self.TOH,self.Smoke, self.Diabetes,self.HDL, self.TCL)
        self.final_risk = round(float(Risk_Score),2)
        self.dfinal_risk = str(self.final_risk) +"%"
        
        
    def open_preventive_measures(self):
        self.window = QtWidgets.QDialog()
        self.ui = Ui_Dialog_preventive(self.Age, self.SBP, self.HDL, self.TCL, self.dGender, self.dSmoke, self.dTOH, self.dDiabetes, self.final_risk)
        self.ui.setupUi(self.window)
        self.window.show()
    
    def open_more_risk(self):
        self.window = QtWidgets.QDialog()
        self.ui = Ui_More_risk(self.Age, self.SBP, self.HDL, self.TCL, self.dGender, self.dSmoke, self.dTOH, self.dDiabetes, self.final_risk)
        self.ui.setupUi(self.window)
        self.window.show()
        
    ''' def open_home(self):
        self.window = QtWidgets.QDialog()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self.window)
        self.window.show()
    '''      
    def setupUi(self, Risk_window):
        Risk_window.setObjectName("Risk_window")
        Risk_window.resize(1343, 593)
        font = QtGui.QFont()
        font.setPointSize(20)
        Risk_window.setFont(font)
        Risk_window.setStyleSheet("background-image: url(:/newPrefix/heart.jpg);")
        self.label_5 = QtWidgets.QLabel(Risk_window)
        self.label_5.setGeometry(QtCore.QRect(500, 10, 401, 41))
        font = QtGui.QFont()
        font.setFamily("Lucida Bright")
        font.setPointSize(26)
        self.label_5.setFont(font)
        self.label_5.setAutoFillBackground(False)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Risk_window)
        self.label_6.setGeometry(QtCore.QRect(270, 60, 861, 41))
        font = QtGui.QFont()
        font.setFamily("MS Reference Sans Serif")
        font.setPointSize(16)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.line_4 = QtWidgets.QFrame(Risk_window)
        self.line_4.setGeometry(QtCore.QRect(920, 380, 401, 16))
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.line_2 = QtWidgets.QFrame(Risk_window)
        self.line_2.setGeometry(QtCore.QRect(880, 120, 20, 361))
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.label_12 = QtWidgets.QLabel(Risk_window)
        self.label_12.setGeometry(QtCore.QRect(920, 390, 401, 31))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(13)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(Risk_window)
        self.label_13.setGeometry(QtCore.QRect(920, 290, 401, 81))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(13)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.line_3 = QtWidgets.QFrame(Risk_window)
        self.line_3.setGeometry(QtCore.QRect(920, 270, 401, 16))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.label_11 = QtWidgets.QLabel(Risk_window)
        self.label_11.setGeometry(QtCore.QRect(920, 170, 401, 71))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(13)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.line = QtWidgets.QFrame(Risk_window)
        self.line.setGeometry(QtCore.QRect(460, 120, 20, 361))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.label = QtWidgets.QLabel(Risk_window)
        self.label.setGeometry(QtCore.QRect(560, 140, 221, 41))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.risk_score = QtWidgets.QLabel(Risk_window)
        self.risk_score.setGeometry(QtCore.QRect(590, 200, 161, 91))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(36)
        self.risk_score.setFont(font)
        self.risk_score.setText("")
        self.risk_score.setObjectName("risk_score")
        self.preventive = QtWidgets.QPushButton(Risk_window)
        self.preventive.setGeometry(QtCore.QRect(550, 320, 261, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.preventive.setFont(font)
        self.preventive.setObjectName("preventive")
        
         #to show preventive measures
        self.preventive.clicked.connect(self.open_preventive_measures)
       
        self.more_risk = QtWidgets.QPushButton(Risk_window)
        self.more_risk.setGeometry(QtCore.QRect(540, 410, 281, 61))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.more_risk.setFont(font)
        self.more_risk.setObjectName("more_risk")
        
        #to show more risk
        self.more_risk.clicked.connect(self.open_more_risk)
        
        self.label_3 = QtWidgets.QLabel(Risk_window)
        self.label_3.setGeometry(QtCore.QRect(40, 140, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Risk_window)
        self.label_4.setGeometry(QtCore.QRect(40, 180, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_7 = QtWidgets.QLabel(Risk_window)
        self.label_7.setGeometry(QtCore.QRect(40, 220, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(Risk_window)
        self.label_8.setGeometry(QtCore.QRect(40, 260, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(Risk_window)
        self.label_9.setGeometry(QtCore.QRect(40, 300, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(Risk_window)
        self.label_10.setGeometry(QtCore.QRect(40, 340, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.label_14 = QtWidgets.QLabel(Risk_window)
        self.label_14.setGeometry(QtCore.QRect(40, 380, 271, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(Risk_window)
        self.label_15.setGeometry(QtCore.QRect(40, 420, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.label_16 = QtWidgets.QLabel(Risk_window)
        self.label_16.setGeometry(QtCore.QRect(140, 140, 61, 31))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(18)
        self.label_16.setFont(font)
        self.label_16.setObjectName("label_16")
        self.label_17 = QtWidgets.QLabel(Risk_window)
        self.label_17.setGeometry(QtCore.QRect(150, 180, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(18)
        self.label_17.setFont(font)
        self.label_17.setObjectName("label_17")
        self.label_18 = QtWidgets.QLabel(Risk_window)
        self.label_18.setGeometry(QtCore.QRect(300, 220, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(18)
        self.label_18.setFont(font)
        self.label_18.setObjectName("label_18")
        self.label_19 = QtWidgets.QLabel(Risk_window)
        self.label_19.setGeometry(QtCore.QRect(270, 260, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(18)
        self.label_19.setFont(font)
        self.label_19.setObjectName("label_19")
        self.label_20 = QtWidgets.QLabel(Risk_window)
        self.label_20.setGeometry(QtCore.QRect(270, 300, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(18)
        self.label_20.setFont(font)
        self.label_20.setObjectName("label_20")
        self.label_21 = QtWidgets.QLabel(Risk_window)
        self.label_21.setGeometry(QtCore.QRect(220, 340, 47, 21))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(18)
        self.label_21.setFont(font)
        self.label_21.setObjectName("label_21")
        self.label_22 = QtWidgets.QLabel(Risk_window)
        self.label_22.setGeometry(QtCore.QRect(330, 380, 47, 21))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(18)
        self.label_22.setFont(font)
        self.label_22.setObjectName("label_22")
        self.label_23 = QtWidgets.QLabel(Risk_window)
        self.label_23.setGeometry(QtCore.QRect(220, 420, 47, 21))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(18)
        self.label_23.setFont(font)
        self.label_23.setObjectName("label_23")
        
        self.form_back = QtWidgets.QPushButton(Risk_window)
        self.form_back.setGeometry(QtCore.QRect(120, 480, 191, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.form_back.setFont(font)
        self.form_back.setObjectName("form_back")
        
        #to go back home
        # self.form_back.clicked.connect(self.open_home)
        
        self.retranslateUi(Risk_window)
        QtCore.QMetaObject.connectSlotsByName(Risk_window)

    def retranslateUi(self, Risk_window):
        _translate = QtCore.QCoreApplication.translate
        Risk_window.setWindowTitle(_translate("Risk_window", "Dialog"))
        self.label_5.setText(_translate("Risk_window", "SAVIOR OF THE HEART"))
        self.label_6.setText(_translate("Risk_window", "Machine Learning approach for determining the risk of having ASCVD in 10 years"))
        self.label_12.setText(_translate("Risk_window", "Know how individual parameter affects the risk score"))
        self.label_13.setText(_translate("Risk_window", "Validation of Framingham Heart Study for\n"
" Asian Population\n"
"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2465638/"))
        self.label_11.setText(_translate("Risk_window", "This calculator is based on Framingham Heart Study\n"
" Find out more on:\n"
" https://www.framinghamheartstudy.org/"))
        self.label.setText(_translate("Risk_window", "Your risk score is:"))
        self.risk_score.setText(_translate("Risk_window", self.dfinal_risk))
        self.preventive.setText(_translate("Risk_window", "Preventive Measures"))
        self.more_risk.setText(_translate("Risk_window", "More about Risk Score"))
        self.label_3.setText(_translate("Risk_window", "Age :"))
        self.label_4.setText(_translate("Risk_window", "Gender :"))
        self.label_7.setText(_translate("Risk_window", "Systolic Blood Pressure :"))
        self.label_8.setText(_translate("Risk_window", "HDL Cholesterol Level :"))
        self.label_9.setText(_translate("Risk_window", "TCL Cholesterol Level :"))
        self.label_10.setText(_translate("Risk_window", "Smoking Status :"))
        self.label_14.setText(_translate("Risk_window", "Treatment of Hypertension :"))
        self.label_15.setText(_translate("Risk_window", "Diabetes Status :"))
        self.label_16.setText(_translate("Risk_window", str(self.Age)))
        self.label_17.setText(_translate("Risk_window", str(self.dGender)))
        self.label_18.setText(_translate("Risk_window", str(self.SBP)))
        self.label_19.setText(_translate("Risk_window", str(self.HDL)))
        self.label_20.setText(_translate("Risk_window", str(self.TCL)))
        self.label_21.setText(_translate("Risk_window", str(self.dSmoke)))
        self.label_22.setText(_translate("Risk_window", str(self.dTOH)))
        self.label_23.setText(_translate("Risk_window", str(self.dDiabetes)))
        self.form_back.setText(_translate("Risk_window", "Back to form"))
#import heart_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Risk_window = QtWidgets.QDialog()
    ui = Ui_Risk_window()
    ui.setupUi(Risk_window)
    Risk_window.show()
    sys.exit(app.exec_())
