from PyQt5 import QtCore, QtGui, QtWidgets, uic
import pickle

def random_forest(sex, age, SBP, TOH, smoke , diabetes, HDL, TDL):

    # load the model from disk
    filename = "./ML/finalized_model.sav"
    loaded_model = pickle.load(open(filename, 'rb'))

    y_pred = loaded_model.predict([[sex, TOH, smoke, diabetes, age, SBP, HDL, TDL]])
    
    if __name__ == "__main__":
        import sys
        app = QtWidgets.QApplication(sys.argv)
        RiskWindow = QtWidgets.QDialog()
        # ui = Ui_RiskWindow()
        # ui.setupUi(RiskWindow)
        RiskWindow.show()
        sys.exit(app.exec_())
    
    return(y_pred)