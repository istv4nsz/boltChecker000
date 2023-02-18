import m_axisvm_connect as ac
import m_gui_handlers as gh
from m_globs import Globs

globs=Globs()
gh.startAxisVMButton_Click(globs) # start AxisVM

pass

ac.ExitAxisVM(globs.axApp)
globs=None

# if globs.axApp is not None:
#   ac.ExitAxisVM(globs.axApp)
# globs=None