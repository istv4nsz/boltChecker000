import sys
import m_axisvm_connect as ac
from m_bolt_checker import BoltCheckInputData

def startAxisVMButton_Click(globs):
  globs.axApp = ac.StartAxisVM()
  if globs.axApp is None:
    print('Connection error')
    sys.exit()
  else:
    print('Connected to AxisVM')

def genForSelectedButton_Click(bcid:BoltCheckInputData, globs):
  pass

def showControlFileButton_Click(globs):
  pass

def performChecksButton_Click(globs):
  pass

def showResultFileButton_Click(globs):
  pass

#
# ac.ExitAxisVM(axApp)
#