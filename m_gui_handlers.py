import sys
import m_axisvm_connect as ac
from m_bolt_checker import BoltCheckInputData
import comtypes.gen._0AA46C32_04EF_46E3_B0E4_D2DA28D0AB08_0_15_401 as ax
from m_globs import Globs

def startAxisVMButton_Click(globs:Globs):
  globs.axApp = ac.StartAxisVM()
  if globs.axApp is None:
    print('Connection error')
    sys.exit()
  else:
    print('Connected to AxisVM')
    globs.axModel = globs.axApp.Models.Item(1)

def genForSelectedButton_Click(bcid:BoltCheckInputData, globs:Globs):
  x=globs.axApp

def showControlFileButton_Click(globs):
  pass

def performChecksButton_Click(globs):
  pass

def showResultFileButton_Click(globs):
  pass

#
# ac.ExitAxisVM(axApp)
#