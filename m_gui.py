import tkinter as tk
import m_gui_handlers as gh
from m_bolt_checker import BoltCheckInputData
from m_globs import Globs

class MainScreen():

  def __init__(self, globs:Globs):
    self.bcid = BoltCheckInputData()
    # bolt_dia_mm = '16'                     #1
    # bolt_fyb_MPa = '640'                   #2
    # bolt_fub_MPa = '800'                   #3
    # basemat_t_mm = '12'                    #4
    # basemat_fy_MPa = '235'                 #5
    # basemat_fu_MPa = '360'                 #6
    # geom_e1_mm = '25'                      #7
    # geom_e2_mm = '25'                      #8
    # geom_p1_mm = '40'                      #9
    # geom_p2_mm = '40'                      #10
    # geom_no_shearplane = '1'               #11
    # geom_no_bolt = '1'                     #12
    # boltcheck_gM2 = '1.25'                 #13
    # boltcheck_bShearAtThread = True        #14
    # boltcheck_bBoltDistCheckStrict = True  #15
    self.globs = globs

    self.run()


  def fExitProgram(self):
    gh.exitAxisVM(self.globs)
    self.root.quit()


  def fGenForSelectedButton(self):
    self.bcid.bolt_dia_mm = int(self.i01entry.get())
    self.bcid.bolt_fyb_MPa = float(self.i02entry.get())
    self.bcid.bolt_fub_MPa = float(self.i03entry.get())
    self.bcid.basemat_t_mm = float(self.i04entry.get())
    self.bcid.basemat_fy_MPa = float(self.i05entry.get())
    self.bcid.basemat_fu_MPa = float(self.i06entry.get())
    self.bcid.geom_e1_mm = float(self.i07entry.get())
    self.bcid.geom_e2_mm = float(self.i08entry.get())
    self.bcid.geom_p1_mm = float(self.i09entry.get())
    self.bcid.geom_p2_mm = float(self.i10entry.get())
    self.bcid.geom_no_shearplane = int(self.i11entry.get())
    self.bcid.geom_no_bolt = int(self.i12entry.get())
    self.bcid.boltcheck_gM2 = float(self.i13entry.get())
    self.bcid.boltcheck_bShearAtThread = bool(self.i14var.get())
    self.bcid.boltcheck_bBoltDistCheckStrict = bool(self.i15var.get())
    gh.genForSelectedButton_Click(self.bcid, self.globs)


  def run(self):
    self.root = tk.Tk()
    self.root.protocol('WM_DELETE_WINDOW', self.fExitProgram)
    self.root.wm_title('Checking metric bolts')
    self.root.columnconfigure(0, weight=1)

    # ---------------------------------------------------------------- frm1 ---
    self.frm1 = tk.Frame(self.root)
    self.frm1.grid(row=0, column=0, sticky='we')
    self.txt1 = tk.Text(self.frm1,
                        bg='grey95',
                        font="{Lucida Console} 8",
                        width=100, height=5,
                        relief=tk.FLAT)
    self.txt1.insert('1.0', "Help text comes here...")
    self.txt1.grid(row=0, column=0, sticky='we')
    self.frm1.columnconfigure(0, weight=1)

    self.startAxisVMButton = tk.Button(self.frm1, text="Start AxisVM", command=lambda : gh.startAxisVMButton_Click(self.globs))
    self.startAxisVMButton.grid(row=1, column=0, sticky= "we")

    self.genForSelectedButton = tk.Button(self.frm1, text="Generate contol file for selected links",
                                          command=self.fGenForSelectedButton)
    self.genForSelectedButton.grid(row=2, column=0, sticky="we")

    # ---------------------------------------------------------------- frm2 ---
    self.frm2 = tk.Frame(self.root)
    self.frm2.grid(row=1, sticky='we')

    # ***************
    self.i01label = tk.Label(self.frm2, bg='grey95', font="{Lucida Console} 8", text='Bolt diameter [mm]:')
    self.i01label.grid(row=0, column=0, sticky='w')

    self.i01entry = tk.Entry(self.frm2, font="{Lucida Console} 8")
    self.i01entry.insert(0, str(self.bcid.bolt_dia_mm))
    self.i01entry.grid(row=0, column=1, sticky='we')

    # ***************
    self.i02label = tk.Label(self.frm2, bg='grey95', font="{Lucida Console} 8", text='Bolt fyb [MPa]:')
    self.i02label.grid(row=1, column=0, sticky='w')

    self.i02entry = tk.Entry(self.frm2, font="{Lucida Console} 8")
    self.i02entry.insert(0, str(self.bcid.bolt_fyb_MPa))
    self.i02entry.grid(row=1, column=1, sticky='we')

    # ***************
    self.i03label = tk.Label(self.frm2, bg='grey95', font="{Lucida Console} 8", text='Bolt fub [MPa]:')
    self.i03label.grid(row=2, column=0, sticky='w')

    self.i03entry = tk.Entry(self.frm2, font="{Lucida Console} 8")
    self.i03entry.insert(0, str(self.bcid.bolt_fub_MPa))
    self.i03entry.grid(row=2, column=1, sticky='we')

    # ***************
    self.i04label = tk.Label(self.frm2, bg='grey95', font="{Lucida Console} 8", text='Base mat. thick. [mm]:')
    self.i04label.grid(row=3, column=0, sticky='w')

    self.i04entry = tk.Entry(self.frm2, font="{Lucida Console} 8")
    self.i04entry.insert(0, str(self.bcid.basemat_t_mm))
    self.i04entry.grid(row=3, column=1, sticky='we')

    # ***************
    self.i05label = tk.Label(self.frm2, bg='grey95', font="{Lucida Console} 8", text='Base mat. fy [MPa]:')
    self.i05label.grid(row=4, column=0, sticky='w')

    self.i05entry = tk.Entry(self.frm2, font="{Lucida Console} 8")
    self.i05entry.insert(0, str(self.bcid.basemat_fy_MPa))
    self.i05entry.grid(row=4, column=1, sticky='we')

    # ***************
    self.i06label = tk.Label(self.frm2, bg='grey95', font="{Lucida Console} 8", text='Base mat. fu [MPa]:')
    self.i06label.grid(row=5, column=0, sticky='w')

    self.i06entry = tk.Entry(self.frm2, font="{Lucida Console} 8")
    self.i06entry.insert(0, str(self.bcid.basemat_fu_MPa))
    self.i06entry.grid(row=5, column=1, sticky='we')

    # ***************
    self.i07label = tk.Label(self.frm2, bg='grey95', font="{Lucida Console} 8", text='Geometry e1 [mm]:')
    self.i07label.grid(row=6, column=0, sticky='w')

    self.i07entry = tk.Entry(self.frm2, font="{Lucida Console} 8")
    self.i07entry.insert(0, str(self.bcid.geom_e1_mm))
    self.i07entry.grid(row=6, column=1, sticky='we')

    # ***************
    self.i08label = tk.Label(self.frm2, bg='grey95', font="{Lucida Console} 8", text='Geometry e2 [mm]:')
    self.i08label.grid(row=7, column=0, sticky='w')

    self.i08entry = tk.Entry(self.frm2, font="{Lucida Console} 8")
    self.i08entry.insert(0, str(self.bcid.geom_e2_mm))
    self.i08entry.grid(row=7, column=1, sticky='we')

    # ***************
    self.i09label = tk.Label(self.frm2, bg='grey95', font="{Lucida Console} 8", text='Geometry p1 [mm]:')
    self.i09label.grid(row=8, column=0, sticky='w')

    self.i09entry = tk.Entry(self.frm2, font="{Lucida Console} 8")
    self.i09entry.insert(0, str(self.bcid.geom_p1_mm))
    self.i09entry.grid(row=8, column=1, sticky='we')

    # ***************
    self.i10label = tk.Label(self.frm2, bg='grey95', font="{Lucida Console} 8", text='Geometry p2 [mm]:')
    self.i10label.grid(row=9, column=0, sticky='w')

    self.i10entry = tk.Entry(self.frm2, font="{Lucida Console} 8")
    self.i10entry.insert(0, str(self.bcid.geom_p2_mm))
    self.i10entry.grid(row=9, column=1, sticky='we')

    # ***************
    self.i11label = tk.Label(self.frm2, bg='grey95', font="{Lucida Console} 8", text='Number of shearplanes:')
    self.i11label.grid(row=10, column=0, sticky='w')

    self.i11entry = tk.Entry(self.frm2, font="{Lucida Console} 8")
    self.i11entry.insert(0, str(self.bcid.geom_no_shearplane))
    self.i11entry.grid(row=10, column=1, sticky='we')

    # ***************
    self.i12label = tk.Label(self.frm2, bg='grey95', font="{Lucida Console} 8", text='Number of bolts:')
    self.i12label.grid(row=11, column=0, sticky='w')

    self.i12entry = tk.Entry(self.frm2, font="{Lucida Console} 8")
    self.i12entry.insert(0, str(self.bcid.geom_no_bolt))
    self.i12entry.grid(row=11, column=1, sticky='we')

    # ***************
    self.i13label = tk.Label(self.frm2, bg='grey95', font="{Lucida Console} 8", text='Gamma_M2:')
    self.i13label.grid(row=11, column=0, sticky='w')

    self.i13entry = tk.Entry(self.frm2, font="{Lucida Console} 8")
    self.i13entry.insert(0, str(self.bcid.boltcheck_gM2))
    self.i13entry.grid(row=11, column=1, sticky='we')

    # ***************
    self.i14label = tk.Label(self.frm2, bg='grey95', font="{Lucida Console} 8", text='Shear at thread:')
    self.i14label.grid(row=12, column=0, sticky='w')

    self.i14var = tk.BooleanVar(value=self.bcid.boltcheck_bShearAtThread)

    self.i14chkb = tk.Checkbutton(self.frm2,
                                  variable=self.i14var,
                                  onvalue=True,
                                  offvalue=False)
    self.i14chkb.grid(row=12, column=1, sticky='w')

    # ***************
    self.i15label = tk.Label(self.frm2, bg='grey95', font="{Lucida Console} 8", text='Strict check of bolt distances:')
    self.i15label.grid(row=13, column=0, sticky='w')

    self.i15var = tk.BooleanVar(value=self.bcid.boltcheck_bBoltDistCheckStrict)

    self.i15entry = tk.Checkbutton(self.frm2,
                                   variable=self.i15var,
                                   onvalue=True,
                                   offvalue=False)
    self.i15entry.grid(row=13, column=1, sticky='w')

    self.frm2.columnconfigure(0, weight=1)
    self.frm2.columnconfigure(1, weight=20)

    # ---------------------------------------------------------------- frm3 ---
    self.frm3 = tk.Frame(self.root)
    self.frm3.grid(row=2, column=0, sticky='we')

    # ***************
    self.showControlFileButton = tk.Button(self.frm3, text="Show control file",
                                           command=lambda : gh.showControlFileButton_Click())
    self.showControlFileButton.grid(row=1, column=0, sticky= "we")

    self.performChecksButton = tk.Button(self.frm3, text="Perform checks",
                                         command=lambda : gh.performChecksButton_Click(self.globs))
    self.performChecksButton.grid(row=2, column=0, sticky= "we")

    self.showResultFileButton = tk.Button(self.frm3, text="Show result file",
                                          command=lambda : gh.showResultFileButton_Click(self.globs))
    self.showResultFileButton.grid(row=3, column=0, sticky= "we")

    self.exitButton = tk.Button(self.frm3, text="Exit program",
                                command=self.fExitProgram)
    self.exitButton.grid(row=4, column=0, sticky= "we")

    self.frm3.columnconfigure(0, weight=1)

    # ----------------------------------------------------------- main loop ---
    self.root.mainloop()
