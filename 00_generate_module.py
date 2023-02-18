import comtypes
import comtypes.client as cc
import struct

# Generate interop module for AxisVM API

# IMPORTANT NOTE: 32 bit python can generate module for 32bit AxisVM and vice versa for 64 bit

# HOW TO DECIDE WHAT IS MAJOR AN MINOR VERSION
# ------------------------------------------------
# >>> import win32com.client as w32
# >>> axobj=w32.gencache.EnsureDispatch('AxisVM.AxisVMApplication')
# >>> axcon=w32.constants
# >>> axcon.acR
# >>> print(axobj.Loaded)
# 1
# >>> print(axobj.Visible)
# 0
# >>> print(axobj.FullExePath)
# C:\AxisVM_X5\AxisVM_x64.exe
# >>> print(axobj.LibraryMajorVersion)
# 15
# >>> print(axobj.LibraryMinorVersion)
# 401
# >>> print(axobj.Version)
# 15 r4k Hu 0

# AxisVM COM version
major_version = 15 # was 9
minor_version = 401 # was 3

# GUID of the AxisVM type library
AxVM_GUID = "{0AA46C32-04EF-46E3-B0E4-D2DA28D0AB08}"

python_platform = struct.calcsize("P") * 8
print ("Current Python interpreter is {} bit".format(python_platform))

 # generate python module for later import in main python file
tlb_id = comtypes.GUID(AxVM_GUID)
try:
    cc.GetModule((tlb_id, major_version, minor_version))
    print("AxisVM module file generated")
except:
    print("AxiVM module generation error !\n",
          "Likely reasons:\n",
          "  - AxisVM and Python are not on the same platform (32 vs 64 bit)\n",
          "  - Major and minor version is not correct")

# generated module will be placed in:
# C:\Users\-\.conda\envs\axisenv\lib\site-packages\comtypes\gen

# copy the name of the generated module
# Generating comtypes.gen._0AA46C32_04EF_46E3_B0E4_D2DA28D0AB08_0_9_3

# import the generated module: _0AA46C32_04EF_46E3_B0E4_D2DA28D0AB08_0_9_3 to main.py:
# e.g.
# import comtypes.gen._0AA46C32_04EF_46E3_B0E4_D2DA28D0AB08_0_9_3 as Axis
