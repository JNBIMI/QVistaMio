from moduls.QvVisorHTML import QvVisorHTML
from moduls.QvPushButton import QvPushButton
from moduls.QvMemoria import QvMemoria
from qgis.PyQt.QtWidgets import QCheckBox
import os
import random

class QvSabiesQue(QvVisorHTML):
    def __init__(self,parent=None):
        if not QvMemoria().getVolHints():
            return
        directori=os.path.abspath('Hints/')+'/'
        self.arxius=[directori+x for x in next(os.walk('./Hints'))[2] if x.endswith(('.htm','.html'))]
        #afegir una ordenació aleatòria
        self.ultimArxiu=directori+'Ja esta.html'
        self.arxius.remove(self.ultimArxiu)
        random.shuffle(self.arxius)
        super().__init__(self.arxius[0],'Sabíeu que...',logo=True,parent=parent)
        self.segBoto=QvPushButton('Següent',destacat=True)
        self.segBoto.clicked.connect(self.seg)
        self.layoutBoto.addWidget(self.segBoto)
        self.cbVolMes=QCheckBox('No tornar a mostrar')
        self.layoutBoto.insertWidget(0,self.cbVolMes)
        self.show()
    def seg(self):
        self.arxius.pop(0)
        if len(self.arxius)!=0:
            self.carrega(self.arxius[0])
        else:
            self.carrega(self.ultimArxiu)
            self.segBoto.setEnabled(False)
    def close(self):
        super().close()
        QvMemoria().setVolHints(not self.cbVolMes.isChecked())