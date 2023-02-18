import os
import m_gui
import m_axisvm_connect as ac

class Globs:
  pass

globs=Globs()
globs.axApp = None
globs.pwd = os.getcwd()
globs.contolFileName = 'check_control.json'

ms = m_gui.MainScreen(globs)

if globs.axApp is not None:
  ac.ExitAxisVM(globs.axApp)

globs=None
