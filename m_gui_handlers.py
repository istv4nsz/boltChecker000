import sys
import m_axisvm_connect as ac
import m_bolt_checker as bc
from m_globs import Globs
import dataclasses
import json
import webbrowser
import m_axisvm_api_functions_wrapper as axw
from tkinter import messagebox


def exitAxisVM(globs: Globs):
    """
    Exiting AxisVM
    :param globs:
    :return:
    """
    if globs.axApp is not None:
        ac.ExitAxisVM(globs.axApp)
    globs.axApp = None


def startAxisVMButton_Click(globs: Globs):
    """
    Starting new AxisVM program instance and placing the COM pointer of AxisVMApplication in globs.axApp
    :param globs:
    :return:
    """
    print('startAxisVMButton_Click')
    globs.axApp = ac.StartAxisVM()
    if globs.axApp is None:
        print('...Connection error')
        messagebox.showwarning(title="Warning",
                               message="Connection error: could not start AxisVM")
    else:
        print('...Connected to AxisVM')
    print('...function end')


def genForSelectedButton_Click(bcid: bc.BoltCheckInputData, globs: Globs):
    """
    Generating control json file for the link elements that are currently selected in AxisVM
    :param bcid:
    :param globs:
    :return:
    """
    print('genForSelectedButton_Click')
    # --- getting selected link elements
    tupl_of_nodes, nof_nodes = axw.linkElements_GetSelectedItemIds(globs.axApp)
    # --- writting to json file if successful
    if (nof_nodes is not None) and (nof_nodes != 0):
        jsonDict = {}
        for n in tupl_of_nodes:
            jsonDict[int(n)] = dataclasses.asdict(bcid)
        json_object = json.dumps(jsonDict, indent=4)
        try:
            with open("control.json", "w") as outfile:
                outfile.write(json_object)
        except:
            messagebox.showwarning(title="Warning",
                                   message="File error: control.json could not be written")
    else:
        messagebox.showwarning(title="Warning",
                               message="Could not retrieve selected links from AxisVM")
    print('...function end')


def showControlFileButton_Click():
    """
    Opening the control.json file in the OS default program
    :return:
    """
    print('showControlFileButton_Click')
    webbrowser.open('control.json')
    print('...function end')


def performChecksButton_Click(globs):
    """
    1) Calculating the resistance force values for each bolt/link element read from the
    control.json file
    2) Reading the corresponding forces from AxisVM
    3) Making comparisons between resistances and acting forces
    :param globs:
    :return:
    """
    print('performChecksButton_Click')
    # 1 --- loading json
    print('...open control json')
    try:
        with open("control.json", "r") as infile:
            json_object = json.load(infile)
    except:
        messagebox.showwarning(title="Warning",
                               message="File error: control.json could not be read")
        return None
    linkelementresults = {}
    for n in json_object:
        # 2 --- calculating resistance forces for bolts in the control file
        print('...reading data and calc resistance forces if id: {}'.format(n))
        x = bc.BoltCheckInputData(**json_object[n])
        bolt = bc.Bolt(dia_mm=x.bolt_dia_mm, fyb_MPa=x.bolt_fyb_MPa, fub_MPa=x.bolt_fub_MPa)
        basemat = bc.BaseMat(fy_MPa=x.basemat_fy_MPa, fu_MPa=x.basemat_fu_MPa, t_mm=x.basemat_t_mm)
        geom = bc.GeomDef(e1_mm=x.geom_e1_mm,
                          e2_mm=x.geom_e2_mm,
                          p1_mm=x.geom_p1_mm,
                          p2_mm=x.geom_p2_mm,
                          no_shearplane=x.geom_no_shearplane,
                          no_bolt=x.geom_no_bolt)
        bcheck = bc.BoltCheck(gM2=x.boltcheck_gM2,
                              bShearAtThread=x.boltcheck_bShearAtThread,
                              bBoltDistCheckStrict=x.boltcheck_bBoltDistCheckStrict)
        result = {}
        result['F_bv_Rd_N'] = bcheck.F_bv_Rd_N(bolt)
        result['F_bb_Rd_edge_N'] = bcheck.F_bb_Rd_edge_N(bolt, basemat, geom)
        result['F_bb_Rd_inner_N'] = bcheck.F_bb_Rd_inner_N(bolt, basemat, geom)
        result['F_bt_Rd_N'] = bcheck.F_bt_Rd_N(bolt)
        result['B_bt_Rd_N'] = bcheck.B_bp_Rd_N(bolt, basemat, geom)
        result['Vmin_N'] = min(result['F_bv_Rd_N'][0],
                               result['F_bb_Rd_edge_N'][0],
                               result['F_bb_Rd_inner_N'][0])
        result['Tmin_N'] = min(result['F_bt_Rd_N'][0],
                               result['B_bt_Rd_N'][0])

        # 2 --- taking forces from AxisVM
        print('...getting AxisVM forces for id {}'.format(n))
        flocX_kN, flocY_kN, flocZ_kN, mlocX_kNm, mlocY_kNm, mlocZ_kNm, lcname, id = \
            axw.results_Forces_LinkElement_kNm(globs.axApp, elementid=int(n))
        if (id < 0) or (id is None):
            messagebox.showwarning(title="Warning",
                                   message="Could not retrieve forces from AxisVM for link {}".format(n))
            result['F_t_Ed_N'] = 'AxisVM error'
            result['F_v_Ed_N'] = 'AxisVM error'
            result['uf_t'] = 'AxisVM error'
            result['uf_v'] = 'AxisVM error'
            result['result'] = 'AxisVM error'

        else:
            # 3 --- making comparisons between resistance and acting forces
            F_t_Ed_N = 1000.0 * flocZ_kN
            F_v_Ed_N = 1000.0 * (flocX_kN ** 2 + flocY_kN ** 2) ** 0.5
            result['F_t_Ed_N'] = F_t_Ed_N
            result['F_v_Ed_N'] = F_v_Ed_N

            uf_t = F_t_Ed_N / result['Tmin_N']
            uf_v = F_v_Ed_N / result['Vmin_N']
            result['uf_t'] = uf_t
            result['uf_v'] = uf_v

            if uf_t <= 1.0 and uf_v <= 1.0:
                result['result'] = 'OK'
            else:
                result['result'] = 'not OK'

        linkelementresults[n] = result

    json_object = json.dumps(linkelementresults, indent=4)
    try:
        with open("results.json", "w") as outfile:
            outfile.write(json_object)
    except:
        messagebox.showwarning(title="Warning",
                               message="File error: results.json could not be written")

    print('...function end')


def showResultFileButton_Click(globs):
    """
    Opening the results.json file in the OS default application
    :param globs:
    :return:
    """
    print('showResultFileButton_Click')
    webbrowser.open('results.json')
    print('...function end')
