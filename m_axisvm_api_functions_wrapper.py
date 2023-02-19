import comtypes.gen._0AA46C32_04EF_46E3_B0E4_D2DA28D0AB08_0_15_401 as ax

def linkElements_GetSelectedItemIds(axApp:ax.AxisVMApplication):
  """
  Returning the item ids of the selected link elements from the AxisVM model
  Manual: AxisVM COM 15.4, page 180
  long GetSelectedItemIds ([out] SAFEARRAY(long) * ItemIds)
          ItemIds Index list of selected link elements
      Returns the number of selected link elements

  :param axApp:
  :return: (tuple of nodes, number of nodes)
  """
  try:
    axModel = axApp.Models.Item(1)
    res = axModel.LinkElements.GetSelectedItemIds()
  except:
    res = (None, None)
  return res


def results_Forces_LinkElement(axApp: ax.AxisVMApplication,
                               nodeid:int,
                               loadcaseid:int = 1,
                               loadlevel:int = 0,
                               analysistype:ax.EAnalysisType = 0):
  """
  Manual: AxisVM COM 15.4, page 180
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
  :param axApp:
  :return:
  """
  try:
    axModel = axApp.Models.Item(1)
    forces = ax.RLinkElementForces()
    res = axModel.Results.Forces.GetLinkElementForcesByLoadCaseId(
      nodeid,
      loadcaseid,
      loadlevel,
      analysistype,
      forces
    )
  except:
    res = (None, None)
  return res