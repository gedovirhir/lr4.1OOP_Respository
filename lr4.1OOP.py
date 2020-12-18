import clr
import random
import time
from math import ceil

clr.AddReference('System')
clr.AddReference('System.IO')
clr.AddReference('System.Drawing')
clr.AddReference('System.Reflection')
clr.AddReference('System.Threading')
clr.AddReference('System.Windows.Forms')

from System import EventHandler

import System.IO
import System.Drawing as Dr
import System.Reflection
import System.Windows.Forms as WinForm
from System.Threading import ApartmentState, Thread, ThreadStart

class form1(System.Windows.Forms.Form):
    def __init__(self):        
        self.Text = "form"
        self.BackColor = Dr.Color.FromArgb(238,238,238)
        self.ClientSize = Dr.Size(900,900)
        caption_height = WinForm.SystemInformation.CaptionHeight
        self.MinimumSize =Dr.Size(392,(117 + caption_height))
        self.model = MyModel()
        
        self.InitiliazeComponent()
        
        
    
    def run(self):
        WinForm.Application.Run(self)
    
    def InitiliazeComponent(self):
        self.components = System.ComponentModel.Container()
        self.Number1Tb = WinForm.TextBox()
        self.Number2Tb = WinForm.TextBox()
        self.Number1Lab = WinForm.Label()
        self.Number2Lab = WinForm.Label()
        self.sum11Lab = WinForm.Label()
        self.sum11Tb = WinForm.TextBox()
        self.sum12Lab = WinForm.Label()
        self.sum12Tb = WinForm.TextBox()
        
        self.model.observer = EventHandler(self.UpdateFromModel)
        

        self.sum21Lab = WinForm.Label()
        self.sum21Tb = WinForm.TextBox()
        self.sum22Lab = WinForm.Label()
        self.sum22Tb = WinForm.TextBox()

        self.Number1Lab.Location = Dr.Point(10,10)
        self.Number1Lab.Size = Dr.Size(50,20)
        self.Number1Lab.Text = "Num 1: "

        self.Number2Lab.Location = Dr.Point(10,50)
        self.Number2Lab.Size = Dr.Size(50,20)
        self.Number2Lab.Text = "Num 2: "


        self.Number1Tb.Location = Dr.Point(70,10)
        self.Number1Tb.Size = Dr.Size(70,20)
        #self.Number1Tb.Text = "100"
        self.Number1Tb.Text = str(self.model.getNum1())
        self.Number1Tb.TextChanged += self.Number1Tb_TextChanged

        self.Number2Tb.Location = Dr.Point(70,50)
        self.Number2Tb.Size = Dr.Size(70,20)
        #self.Number2Tb.Text = "200"
        self.Number2Tb.Text = str(self.model.getNum2())
        self.Number2Tb.TextChanged += self.Number2Tb_TextChanged
        
        self.sum11Lab.Location = Dr.Point(150,10)
        self.sum11Lab.Size = Dr.Size(70,20)
        self.sum11Lab.Text = "Num1 +1: "

        self.sum11Tb.Location = Dr.Point(210,10)
        self.sum11Tb.Size = Dr.Size(70,20)
        #self.sum11Tb.Text = str(int(self.Number1Tb.Text)+1)
        self.sum11Tb.Text = str(self.model.getNum1Pls())
        self.sum11Tb.TextChanged += self.sum11Tb_TextChanged

        self.sum12Lab.Location = Dr.Point(290,10)
        self.sum12Lab.Size = Dr.Size(70,30)
        self.sum12Lab.Text = "Num1 +Num2: "

        self.sum12Tb.Location = Dr.Point(360,10)
        self.sum12Tb.Size = Dr.Size(70,20)
        #self.sum12Tb.Text = str(int(self.Number1Tb.Text)+int(self.Number2Tb.Text))
        self.sum12Tb.Text = str(self.model.getSum())
        self.sum12Tb.TextChanged += self.sum12Tb_TextChanged

        #2
        self.sum21Lab.Location = Dr.Point(150,50)
        self.sum21Lab.Size = Dr.Size(70,20)
        self.sum21Lab.Text = "Num1 -1: "

        self.sum21Tb.Location = Dr.Point(210,50)
        self.sum21Tb.Size = Dr.Size(70,22)
        #self.sum21Tb.Text = str(int(self.Number2Tb.Text)-1)
        self.sum21Tb.Text = str(self.model.getNum2Mns())
        self.sum21Tb.TextChanged += self.sum21Tb_TextChanged

        
        self.sum22Lab.Location = Dr.Point(290,50)
        self.sum22Lab.Size = Dr.Size(70,30)
        self.sum22Lab.Text = "Num2 +Num1: "

        self.sum22Tb.Location = Dr.Point(360,50)
        self.sum22Tb.Size = Dr.Size(70,20)
        #self.sum22Tb.Text = str(int(self.Number2Tb.Text)+int(self.Number1Tb.Text))
        self.sum22Tb.Text = str(self.model.getSum())
        self.sum22Tb.TextChanged += self.sum22Tb_TextChanged

        

        self.Controls.Add(self.Number1Lab)
        self.Controls.Add(self.Number2Lab)
        self.Controls.Add(self.Number1Tb)
        self.Controls.Add(self.Number2Tb)
        self.Controls.Add(self.sum11Tb)
        self.Controls.Add(self.sum11Lab)
        self.Controls.Add(self.sum12Tb)
        self.Controls.Add(self.sum12Lab)

        self.Controls.Add(self.sum21Tb)
        self.Controls.Add(self.sum21Lab)
        self.Controls.Add(self.sum22Tb)
        self.Controls.Add(self.sum22Lab)
        
    def dispose(self):
        self.components.Dispose()
        WinForm.Form.Dispose(self)

    
    """
    def Number1Tb_TextChanged(self, sender, args):
        try:
            self.sum11Tb.Text = str(int(self.Number1Tb.Text)+1)
            self.sum12Tb.Text = str(int(self.Number1Tb.Text)+int(self.Number2Tb.Text))
            self.sum22Tb.Text = str(int(self.Number1Tb.Text)+int(self.Number2Tb.Text))
        except ValueError:
            self.sum11Tb.Text = str(1)
            self.sum12Tb.Text = str(int(self.Number2Tb.Text))
            self.sum22Tb.Text = str(int(self.Number2Tb.Text))
    def Number2Tb_TextChanged(self, sender, args):
        try:
            self.sum21Tb.Text = str(int(self.Number2Tb.Text)-1)
            self.sum12Tb.Text = str(int(self.Number1Tb.Text)+int(self.Number2Tb.Text))
            self.sum22Tb.Text = str(int(self.Number1Tb.Text)+int(self.Number2Tb.Text))
        except ValueError:
            self.sum21Tb.Text = str(3)
            self.sum12Tb.Text = str(int(self.Number1Tb.Text))
            self.sum22Tb.Text = str(int(self.Number2Tb.Text))
    def sum11Tb_TextChanged(self, sender, args):
        try:
            self.Number1Tb.Text = str(int(self.sum11Tb.Text)-1)
        except ValueError:
            self.Number1Tb.Text = str(-1)
    def sum12Tb_TextChanged(self, sender, artgs):
        try:
            self.Number1Tb.Text = str(int(self.sum12Tb.Text)-int(self.Number2Tb.Text))
        except ValueError:
            self.Number1Tb.Text = str(-int(self.Number2Tb.Text))
    def sum21Tb_TextChanged(self, sender, args):
        try:
            self.Number2Tb.Text = str(int(self.sum21Tb.Text)+1)
        except ValueError:
            self.Number2Tb.Text = str(1)
    def sum22Tb_TextChanged(self, sender, artgs):
        try:
            self.Number2Tb.Text = str(int(self.sum22Tb.Text)-int(self.Number1Tb.Text))
        except ValueError:
            self.Number2Tb.Text = str(-int(self.Number1Tb.Text))
    """
    def Number1Tb_TextChanged(self, sender, args):
        try:
            self.model.setNum1(int(self.Number1Tb.Text))
        except ValueError:
            self.model.setNum1(0)
    def Number2Tb_TextChanged(self, sender, args):
        try:
            self.model.setNum2(int(self.Number2Tb.Text))
        except ValueError:
            self.model.setNum2(0)
    def sum11Tb_TextChanged(self, sender, args):
        try:
            self.model.setNum1(int(self.sum11Tb.Text) - 1)
        except ValueError:
            self.model.setNum1(-1)
    def sum12Tb_TextChanged(self, sender, args):
        try:
            self.model.setNum1(int(self.sum12Tb.Text) - self.model.getNum2())
        except ValueError:
            self.model.setNum1(-self.model.getNum2())
    def sum21Tb_TextChanged(self, sender, args):
        try:
            self.model.setNum2(int(self.sum21Tb.Text) + 1)
        except ValueError:
            self.model.setNum1(1)
    def sum22Tb_TextChanged(self, sender, args):
        try:
            self.model.setNum2(int(self.sum22Tb.Text) - self.model.getNum1())
        except ValueError:
            self.model.setNum2(-self.model.getNum1())

    def UpdateFromModel(self, sender, args):
        self.Number1Tb.Text = str(self.model.getNum1())
        self.Number2Tb.Text = str(self.model.getNum2())

        self.sum11Tb.Text = str(self.model.getNum1Pls())
        self.sum21Tb.Text = str(self.model.getNum2Mns())

        self.sum12Tb.Text = str(self.model.getSum())
        self.sum22Tb.Text = str(self.model.getSum())


class MyModel(object):
    def __init__(self, num1 = 100, num2 = 200):
        self.num1 = num1
        self.num2 = num2

        self.observer = System.EventHandler
    
    def setNum1(self, num):
        self.num1 = num

        self.observer.Invoke(self, None)
    def setNum2(self, num):
        self.num2 = num

        self.observer.Invoke(self, None)
    def getNum1(self):
        return self.num1
    def getNum2(self):
        return self.num2
    def getNum1Pls(self):
        return self.num1 + 1
    def getNum2Mns(self):
        return self.num2 - 1
    def getSum(self):
        return self.num2 + self.num1
             
        

def form_thr():
    form = form1()

    WinForm.Application.Run(form)
    form.dispose()


if __name__ == '__main__':
    form_thr()  