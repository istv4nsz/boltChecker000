import comtypes.gen._0AA46C32_04EF_46E3_B0E4_D2DA28D0AB08_0_15_401 as ax

def linkElements_GetSelectedItemIds(axApp:ax.AxisVMApplication) -> (int, int):
  """
  Returning the item ids of the selected link elements from the AxisVM model
  Manual: AxisVM COM 15.4, page 180
  long GetSelectedItemIds ([out] SAFEARRAY(long) * ItemIds)
          ItemIds Index list of selected link elements
      Returns the number of selected link elements

  Experience:
    returns tuple( , )
      tuple of ints - element ids
      int - number if elements returned
  :param axApp:
  :return: (tuple of nodes, number of nodes)
  """
  try:
    axModel = axApp.Models.Item(1)
    res = axModel.LinkElements.GetSelectedItemIds()
  except:
    res = (None, None)
  return res


def results_Forces_LinkElement_kNm(axApp: ax.AxisVMApplication,
                               elementid:int,
                               loadcaseid:int = 1,
                               loadlevel:int = 0,
                               analysistype:ax.EAnalysisType = 0) -> \
      (float, float, float, float, float, float, str, int) :
  """
  Manual: AxisVM COM 15.4, page xxx
  long GetLinkElementForcesByLoadCaseId ([in] long LinkElementId,
                                        [in] long LoadCaseId,
                                        [in] long LoadLevel,
                                        [in] EAnalysisType AnalysisType,
                                        [i/o] RLinkElementForces* Forces,
                                        [out] BSTR* Combination)
            LinkElementId link element index
                          (0 < LinkElementId<=AxisVMLinkElements.Count)
            LoadCaseId load case index (0 < LoadCaseId <= AxisVMLoadCases.Count)
            LoadLevel load level or time step (increment) index
            AnalysisType type of analysis
            Forces forces in edge connection
            Combination name of the load case
      If successful returns edge connection index, otherwise returns an error code
      (errDatabaseNotReady, feInvalidCombinationOfLoadCaseAndLoadLevel, feInvalidAnalysisType,
      feLinkElementIndexOutOfBounds).

  Experience:
    returns tuple( , , ):
      <comtypes.gen._0AA46C32_04EF_46E3_B0E4_D2DA28D0AB08_0_15_401.RLinkElementForces object at 0x000001F08BC9A350>
      loadcase name - None if error
      linkElementID - error code if error

  :param axApp:
  :return:
  """
  try:
    # ensuring correct parameter types
    elementid = int(elementid)
    loadcaseid = int(loadcaseid)
    loadlevel = int(loadlevel)
    # return object
    # forces = ax.RLinkElementForces() # turns out not needed
    # communicating with AxisVM
    axModel = axApp.Models.Item(1)
    forces, lcname, id = axModel.Results.Forces.GetLinkElementForcesByLoadCaseId(
      elementid,
      loadcaseid,
      loadlevel,
      analysistype,
      )
    res = ( forces.lefSection1.lefvNx,
            forces.lefSection1.lefvVy,
            forces.lefSection1.lefvVz,
            forces.lefSection1.lefvTx,
            forces.lefSection1.lefvMy,
            forces.lefSection1.lefvMz,
            lcname,
            id )
  except:
    res = (None,) * 8
  return res