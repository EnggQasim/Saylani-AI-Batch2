import sys

from PyQt5.QtWidgets import QDialog, QApplication

from AddTwoNumb import *

 

class MyForm(QDialog):

    def __init__(self):

        super().__init__()

        self.ui = Ui_Dialog()

        self.ui.setupUi(self)

        self.ui.pushButtonAdd.clicked.connect(self.dispSum)

        self.show()

 

    def dispSum(self):

        numb1=self.ui.lineEditFirstNumb.text()

        numb2=self.ui.lineEditSecondNumb.text()

        x=int(numb1)

        y=int(numb2)

        z=x+y

        self.ui.labelResponse.setText("Sum is "+str(z))

 

if __name__=="__main__":   

    app = QApplication(sys.argv)

    w = MyForm()

    w.show()

    sys.exit(app.exec_())
