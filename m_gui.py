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


  def exitProgram(self):
    gh.exitgui(self.globs)
    self.root.quit()

  def run(self):
    self.root = tk.Tk()
    self.root.protocol('WM_DELETE_WINDOW', self.exitProgram)
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
    self.txt1.insert('1.0', "Text comes here...")
    self.txt1.grid(row=0, column=0, sticky='we')
    self.frm1.columnconfigure(0, weight=1)

    self.startAxisVMButton = tk.Button(self.frm1, text="Start AxisVM", command=lambda : gh.startAxisVMButton_Click(self.globs))
    self.startAxisVMButton.grid(row=1, column=0, sticky= "we")

    self.genForSelectedButton = tk.Button(self.frm1, text="Generate contol file for selected links",
                                          command=lambda : gh.genForSelectedButton_Click(self.bcid, self.globs))
    self.genForSelectedButton.grid(row=2, column=0, sticky="we")

    # ---------------------------------------------------------------- frm2 ---
    self.frm2 = tk.Frame(self.root)
    self.frm2.grid(row=1, sticky='we')

    # ***************
    self.lbl1 = tk.Label(self.frm2, bg='grey95', font="{Lucida Console} 8", text='Bolt diameter [mm]:')
    self.lbl1.grid(row=0, column=0, sticky='w')

    self.entry1 = tk.Entry(self.frm2, font="{Lucida Console} 8")
    self.entry1.insert(0, str(self.bcid.bolt_dia_mm))
    self.entry1.grid(row=0, column=1, sticky='we')

    # ***************
    self.lbl2 = tk.Label(self.frm2, bg='grey95', font="{Lucida Console} 8", text='Bolt fyb [MPa]:')
    self.lbl2.grid(row=1, column=0, sticky='w')

    self.entry2 = tk.Entry(self.frm2, font="{Lucida Console} 8")
    self.entry2.insert(0, str(self.bcid.bolt_fyb_MPa))
    self.entry2.grid(row=1, column=1, sticky='we')

    # ***************
    self.lbl3 = tk.Label(self.frm2, bg='grey95', font="{Lucida Console} 8", text='Bolt fub [MPa]:')
    self.lbl3.grid(row=2, column=0, sticky='w')

    self.entry3 = tk.Entry(self.frm2, font="{Lucida Console} 8")
    self.entry3.insert(0, str(self.bcid.bolt_fub_MPa))
    self.entry3.grid(row=2, column=1, sticky='we')

    # ***************
    self.lbl4 = tk.Label(self.frm2, bg='grey95', font="{Lucida Console} 8", text='Base mat. thick. [mm]:')
    self.lbl4.grid(row=3, column=0, sticky='w')

    self.entry4 = tk.Entry(self.frm2, font="{Lucida Console} 8")
    self.entry4.insert(0, str(self.bcid.basemat_t_mm))
    self.entry4.grid(row=3, column=1, sticky='we')

    # ***************
    self.lbl5 = tk.Label(self.frm2, bg='grey95', font="{Lucida Console} 8", text='Base mat. fy [MPa]:')
    self.lbl5.grid(row=4, column=0, sticky='w')

    self.entry5 = tk.Entry(self.frm2, font="{Lucida Console} 8")
    self.entry5.insert(0, str(self.bcid.basemat_fy_MPa))
    self.entry5.grid(row=4, column=1, sticky='we')

    # ***************
    self.lbl6 = tk.Label(self.frm2, bg='grey95', font="{Lucida Console} 8", text='Base mat. fu [MPa]:')
    self.lbl6.grid(row=5, column=0, sticky='w')

    self.entry6 = tk.Entry(self.frm2, font="{Lucida Console} 8")
    self.entry6.insert(0, str(self.bcid.basemat_fu_MPa))
    self.entry6.grid(row=5, column=1, sticky='we')

    # ***************
    self.lbl7 = tk.Label(self.frm2, bg='grey95', font="{Lucida Console} 8", text='Geometry e1 [mm]:')
    self.lbl7.grid(row=6, column=0, sticky='w')

    self.entry7 = tk.Entry(self.frm2, font="{Lucida Console} 8")
    self.entry7.insert(0, str(self.bcid.geom_e1_mm))
    self.entry7.grid(row=6, column=1, sticky='we')

    # ***************
    self.lbl8 = tk.Label(self.frm2, bg='grey95', font="{Lucida Console} 8", text='Geometry e2 [mm]:')
    self.lbl8.grid(row=7, column=0, sticky='w')

    self.entry8 = tk.Entry(self.frm2, font="{Lucida Console} 8")
    self.entry8.insert(0, str(self.bcid.geom_e2_mm))
    self.entry8.grid(row=7, column=1, sticky='we')

    # ***************
    self.lbl9 = tk.Label(self.frm2, bg='grey95', font="{Lucida Console} 8", text='Geometry p1 [mm]:')
    self.lbl9.grid(row=8, column=0, sticky='w')

    self.entry9 = tk.Entry(self.frm2, font="{Lucida Console} 8")
    self.entry9.insert(0, str(self.bcid.geom_p1_mm))
    self.entry9.grid(row=8, column=1, sticky='we')

    # ***************
    self.lbl10 = tk.Label(self.frm2, bg='grey95', font="{Lucida Console} 8", text='Geometry p2 [mm]:')
    self.lbl10.grid(row=9, column=0, sticky='w')

    self.entry10 = tk.Entry(self.frm2, font="{Lucida Console} 8")
    self.entry10.insert(0, str(self.bcid.geom_p2_mm))
    self.entry10.grid(row=9, column=1, sticky='we')

    # ***************
    self.lbl11 = tk.Label(self.frm2, bg='grey95', font="{Lucida Console} 8", text='Number of shearplanes:')
    self.lbl11.grid(row=10, column=0, sticky='w')

    self.entry11 = tk.Entry(self.frm2, font="{Lucida Console} 8")
    self.entry11.insert(0, str(self.bcid.geom_no_shearplane))
    self.entry11.grid(row=10, column=1, sticky='we')

    # ***************
    self.lbl12 = tk.Label(self.frm2, bg='grey95', font="{Lucida Console} 8", text='Number of bolts:')
    self.lbl12.grid(row=11, column=0, sticky='w')

    self.entry12 = tk.Entry(self.frm2, font="{Lucida Console} 8")
    self.entry12.insert(0, str(self.bcid.geom_no_bolt))
    self.entry12.grid(row=11, column=1, sticky='we')

    # ***************
    self.lbl13 = tk.Label(self.frm2, bg='grey95', font="{Lucida Console} 8", text='Gamma_M2:')
    self.lbl13.grid(row=11, column=0, sticky='w')

    self.entry13 = tk.Entry(self.frm2, font="{Lucida Console} 8")
    self.entry13.insert(0, str(self.bcid.boltcheck_gM2))
    self.entry13.grid(row=11, column=1, sticky='we')

    # ***************
    self.lbl14 = tk.Label(self.frm2, bg='grey95', font="{Lucida Console} 8", text='Shear at thread:')
    self.lbl14.grid(row=12, column=0, sticky='w')

    xbShearAtThread = tk.BooleanVar(value=self.bcid.boltcheck_bShearAtThread)

    self.entry14 = tk.Entry(self.frm2, font="{Lucida Console} 8")
    self.entry14 = tk.Checkbutton(self.frm2,
                                  variable=xbShearAtThread,
                                  onvalue=True,
                                  offvalue=False)
    self.entry14.grid(row=12, column=1, sticky='w')

    # ***************
    self.lbl15 = tk.Label(self.frm2, bg='grey95', font="{Lucida Console} 8", text='Strict check of bolt distances:')
    self.lbl15.grid(row=13, column=0, sticky='w')

    xbBoltDistCheckStrict = tk.BooleanVar(value=self.bcid.boltcheck_bBoltDistCheckStrict)

    self.entry15 = tk.Entry(self.frm2, font="{Lucida Console} 8")
    self.entry15 = tk.Checkbutton(self.frm2,
                                  variable=xbBoltDistCheckStrict,
                                  onvalue=True,
                                  offvalue=False)
    self.entry15.grid(row=13, column=1, sticky='w')

    self.frm2.columnconfigure(0, weight=1)
    self.frm2.columnconfigure(1, weight=20)

    # ---------------------------------------------------------------- frm2 ---
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
                                command=self.exitProgram)
    self.exitButton.grid(row=4, column=0, sticky= "we")

    self.frm3.columnconfigure(0, weight=1)

    # ----------------------------------------------------------- main loop ---
    self.root.mainloop()
