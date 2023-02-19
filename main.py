import os
import m_gui
import m_axisvm_connect as ac
from m_globs import Globs

globs=Globs()

ms = m_gui.MainScreen(globs)

print('Exiting...')
if globs.axApp is not None:
  ac.ExitAxisVM(globs.axApp)

globs=None
