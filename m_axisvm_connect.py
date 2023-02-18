import sys
import errno
import comtypes
import comtypes.client as cc
from time import sleep
import comtypes.gen._0AA46C32_04EF_46E3_B0E4_D2DA28D0AB08_0_15_401 as ax

#Axis = main.Axis
AX_APP_PROGID = 'AxisVM.AxisVMApplication'


def WaitForAxisVM_loaded(aAxApp):
  # wait until AxisVM is loaded
  try:
    while aAxApp.Loaded == ax.lbFalse:
      sleep(0.1)  # wait 100 ms
    return True
  except:
    return False


def InitAxisVM(aAxApp):
  aAxApp.Visible = ax.lbTrue  # AxisVM starts hidden, so make it visible
  aAxApp.CloseOnLastReleased = ax.lbFalse  # Do not close AxisVM after this code
  aAxApp.AskCloseOnLastReleased = ax.lbTrue  # Ask whether close AxisVM after this code
  aAxApp.AskSaveOnLastReleased = ax.lbTrue
  aAxApp.ApplicationClose = ax.acEnableNoWarning


def StartAxisVM():
  axApp = None
  try:
    axApp = cc.CreateObject(AX_APP_PROGID, comtypes.CLSCTX_ALL, None, ax.IAxisVMApplication)
  except:
    sys.exit(errno.EACCES)
  if axApp is not None:
    if WaitForAxisVM_loaded(axApp):
      InitAxisVM(axApp)
      return axApp
  return None

# does not work :(
#
# def ConnectoAxisVM():
#   axApp = None
#   try:
#     axApp = cc.GetActiveObject(AX_APP_PROGID, ax.IAxisVMApplication)
#   except:
#     sys.exit(errno.EACCES)
#   if axApp is None:
#     return None
#   if WaitForAxisVM_loaded(axApp):
#     InitAxisVM(axApp)
#     return axApp
#   else:
#     return None


def ExitAxisVM(axApp):
  axApp.ApplicationClose = ax.acEnableNoWarning
  axApp.AskSaveOnLastReleased = ax.lbFalse
  axApp.Quit()
  axApp = None
