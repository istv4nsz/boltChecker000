import sys
import m_axisvm_connect as ac
from m_bolt_checker import BoltCheckInputData
from m_globs import Globs
import dataclasses
import json

def exitgui(globs:Globs):
  if globs.axApp is not None:
    ac.ExitAxisVM(globs.axApp)
  globs.axApp = None
  globs.axModel = None

def startAxisVMButton_Click(globs:Globs):
  globs.axApp = ac.StartAxisVM()
  if globs.axApp is None:
    print('Connection error')
    sys.exit()
  else:
    print('Connected to AxisVM')


def genForSelectedButton_Click(bcid:BoltCheckInputData, globs:Globs):
  globs.axModel = globs.axApp.Models.Item(1)
  tupl_of_nodes, nof_nodes = globs.axModel.LinkElements.GetSelectedItemIds()
  jsonDict={}
  for n in tupl_of_nodes:
    jsonDict[n]=dataclasses.asdict(bcid)
  json_object = json.dumps(jsonDict, indent=4)
  with open("sample.json", "w") as outfile:
    outfile.write(json_object)

def showControlFileButton_Click(globs):
  pass

def performChecksButton_Click(globs):
  pass

def showResultFileButton_Click(globs):
  pass

#
# ac.ExitAxisVM(axApp)
#