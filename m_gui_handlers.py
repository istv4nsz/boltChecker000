import sys
import m_axisvm_connect as ac
import m_bolt_checker as bc
from m_globs import Globs
import dataclasses
import json
import webbrowser
import m_axisvm_api_functions_wrapper as axw
from tkinter import messagebox


def exitgui(globs:Globs):
  if globs.axApp is not None:
    ac.ExitAxisVM(globs.axApp)
  globs.axApp = None


def startAxisVMButton_Click(globs:Globs):
  globs.axApp = ac.StartAxisVM()
  if globs.axApp is None:
    print('Connection error')
    sys.exit()
  else:
    print('Connected to AxisVM')


def genForSelectedButton_Click(bcid:bc.BoltCheckInputData, globs:Globs):
  tupl_of_nodes, nof_nodes = axw.linkElements_GetSelectedItemIds(globs.axApp)
  if (nof_nodes is not None) and (nof_nodes != 0):
    jsonDict={}
    for n in tupl_of_nodes:
      jsonDict[int(n)]=dataclasses.asdict(bcid)
    json_object = json.dumps(jsonDict, indent=4)
    try:
      with open("contol.json", "w") as outfile:
        outfile.write(json_object)
    except:
      messagebox.showwarning(title="Warning",
                             message="File error: control.json could not be written")
  else:
    messagebox.showwarning(title="Warning",
                           message="Could not retrieve selected links from AxisVM")


def showControlFileButton_Click():
  webbrowser.open('control.json')


def performChecksButton_Click(globs):
  #1 --- loading json and calculating resistance forces for bolts in the control file
  try:
    with open("control.json", "r") as infile:
      json_object = json.load(infile)
  except:
    messagebox.showwarning(title="Warning",
                           message="File error: control.json could not be read")
    return None
  linkelements={}
  for n in json_object:
    x=bc.BoltCheckInputData(**json_object[n])
    bolt=bc.Bolt(dia_mm=x.bolt_dia_mm, fyb_MPa=x.bolt_fyb_MPa, fub_MPa=x.bolt_fub_MPa)
    basemat=bc.BaseMat(fy_MPa=x.basemat_fy_MPa, fu_MPa=x.basemat_fu_MPa, t_mm=x.basemat_t_mm)
    geom=bc.GeomDef(e1_mm=x.geom_e1_mm,
                    e2_mm=x.geom_e2_mm,
                    p1_mm=x.geom_p1_mm,
                    p2_mm=x.geom_p2_mm,
                    no_shearplane=x.geom_no_shearplane,
                    no_bolt=x.geom_no_bolt)
    bcheck=bc.BoltCheck(gM2=x.boltcheck_gM2,
                        bShearAtThread=x.boltcheck_bShearAtThread,
                        bBoltDistCheckStrict=x.boltcheck_bBoltDistCheckStrict)
    result={}
    result['F_bv_Rd_N']=bcheck.F_bt_Rd_N(bolt)
    result['F_bb_Rd_edge_N']=bcheck.F_bb_Rd_edge_N(bolt, basemat, geom)
    result['F_bb_Rd_inner_N']=bcheck.F_bb_Rd_inner_N(bolt, basemat, geom)
    result['F_bt_Rd_N']=bcheck.F_bt_Rd_N(bolt)
    result['B_bt_Rd_N']=bcheck.B_bp_Rd_N(bolt, basemat, geom)
    result['Vmin_N']=min(result['F_bv_Rd_N'][0],
                         result['F_bb_Rd_edge_N'][0],
                         result['F_bb_Rd_inner_N'][0])
    result['Tmin_N']=min(result['F_bt_Rd_N'][0],
                         result['B_bt_Rd_N'][0])
    linkelements[int(n)]=result
  #2 --- taking forces from AxisVM
    axModel = globs.axApp.Models.Item(1)
    axResults = axModel.Results


def showResultFileButton_Click(globs):
  pass

