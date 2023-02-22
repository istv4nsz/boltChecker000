from dataclasses import dataclass


@dataclass
class BoltCheckInputData:
    bolt_dia_mm: int = 20
    bolt_fyb_MPa: float = 600
    bolt_fub_MPa: float = 800
    basemat_fy_MPa: float = 235
    basemat_fu_MPa: float = 360
    basemat_t_mm: float = 10
    geom_e1_mm: float = 30
    geom_e2_mm: float = 30
    geom_p1_mm: float = 60
    geom_p2_mm: float = 60
    geom_no_shearplane: int = 1
    geom_no_bolt: int = 1
    boltcheck_gM2: float = 1.25
    boltcheck_bShearAtThread: bool = True
    boltcheck_bBoltDistCheckStrict: bool = True


class Bolt:

    def __init__(self, dia_mm=20, fyb_MPa=600, fub_MPa=800):
        self.dia_mm = int(dia_mm)
        self.fyb_MPa = float(fyb_MPa)
        self.fub_MPa = float(fub_MPa)
        self.holeDia_mm = self.getHoleDia_mm(dia_mm)
        self.shearArea_mm2 = self.getShearArea_mm2(dia_mm)
        self.diaBM_mm = self.getDiaBM_mm(dia_mm)
        self.area_mm2 = 1.0 * (self.dia_mm ** 2) * 3.14 / 4

    @staticmethod
    def getHoleDia_mm(dia_mm):
        return {6: 7,
                8: 9,
                10: 12,
                12: 13,
                14: 15,
                16: 18,
                18: 20,
                20: 22,
                22: 24,
                24: 26,
                27: 30,
                30: 33}[dia_mm]

    @staticmethod
    def getShearArea_mm2(dia_mm):
        return {6: 20.1,
                8: 36.6,
                10: 58.0,
                12: 84.3,
                14: 115.0,
                16: 157.0,
                18: 192.0,
                20: 245.0,
                22: 303.0,
                24: 353.0,
                27: 459.0,
                30: 561.0}[dia_mm]

    @staticmethod
    def getDiaBM_mm(dia_mm):
        return {6: 9.9,
                8: 13.2,
                10: 17.0,
                12: 20.5,
                14: 23.7,
                16: 24.6,
                18: 29.1,
                20: 32.4,
                22: 34.5,
                24: 38.8,
                27: 44.2,
                30: 49.6}[dia_mm]


class BaseMat:

    def __init__(self, fy_MPa=235, fu_MPa=360, t_mm=10):
        self.fy_MPa = float(fy_MPa)
        self.fu_MPa = float(fu_MPa)
        self.t_mm = float(t_mm)


class GeomDef:

    def __init__(self, e1_mm=30, e2_mm=30, p1_mm=60, p2_mm=60, no_shearplane=1, no_bolt=1):
        self.e1_mm = float(e1_mm)
        self.e2_mm = float(e2_mm)
        self.p1_mm = float(p1_mm)
        self.p2_mm = float(p2_mm)
        self.no_shearplane = int(no_shearplane)
        self.no_bolt = int(no_bolt)

    @staticmethod  # -- EN 1993-1-8:2005 minimum values, Table 3.3
    def get_e1_EC_min_dist_mm(db0):
        return 1.2 * db0

    @staticmethod
    def get_e2_EC_min_dist_mm(db0):
        return 1.2 * db0

    @staticmethod
    def get_p1_EC_min_dist_mm(db0):
        return 2.2 * db0

    @staticmethod
    def get_p2_EC_min_dist_mm(db0):
        return 2.4 * db0

    @staticmethod  # -- From Kisokos
    def get_e1_recommended_min_dist_mm(db0):
        return 2.0 * db0

    @staticmethod
    def get_e2_recommended_min_dist_mm(db0):
        return 1.5 * db0

    @staticmethod
    def get_p1_recommended_min_dist_mm(db0):
        return 3.0 * db0

    @staticmethod
    def get_p2_recommended_min_dist_mm(db0):
        return 3.0 * db0


class BoltCheck:

    def __init__(self, gM2=1.25, bShearAtThread=True, bBoltDistCheckStrict=True):
        self.gM2 = float(gM2)
        self.bShearAtThread = bool(bShearAtThread)
        self.bBoltDistCheckStrict = bool(bBoltDistCheckStrict)

    def F_bv_Rd_N(self, bolt: Bolt):
        if self.bShearAtThread:
            AA = bolt.shearArea_mm2
        else:
            AA = bolt.area_mm2
        resVal = bolt.fub_MPa * AA / self.gM2 / (3 ** 0.5)  # N/mm2 * mm2 / c / c -> return N
        return (resVal,
                'd:{}, A:{}, fub:{}, gM2:{}'.format(bolt.dia_mm, AA, bolt.fub_MPa, self.gM2)
                )

    def F_bb_Rd_edge_N(self, bolt: Bolt, basemat: BaseMat, geom: GeomDef):
        if self.bBoltDistCheckStrict:
            if GeomDef.get_e1_EC_min_dist_mm(bolt.holeDia_mm) > geom.e1_mm:
                return (0.0, 'Zero from bolt e1 distance check')
            if GeomDef.get_e2_EC_min_dist_mm(bolt.holeDia_mm) > geom.e2_mm:
                return (0.0, 'Zero from bolt e2 distance check')
        k1 = max(0.0, min(2.8 * geom.e2_mm / bolt.holeDia_mm - 1.7, 2.5))
        a_b = min(geom.e1_mm / 3 / bolt.holeDia_mm, 1, bolt.fub_MPa / basemat.fu_MPa)
        resVal = k1 * a_b * basemat.fu_MPa * bolt.dia_mm * basemat.t_mm / self.gM2
        resVal = resVal * int(geom.e1_mm >= bolt.holeDia_mm / 2)
        resVal = resVal * int(geom.e2_mm >= bolt.holeDia_mm / 2)
        return (resVal,
                'd:{}, d0:{}, f.ub:{}, f.u:{}, t:{}, e1:{}>{:.2f}, e2:{}>{:.2f}, k1:{:.2f}, a_b:{:.2f}, gM2:{}'.format(
                    bolt.dia_mm,
                    bolt.holeDia_mm,
                    bolt.fub_MPa,
                    basemat.fu_MPa,
                    basemat.t_mm,
                    geom.e1_mm,
                    GeomDef.get_e1_EC_min_dist_mm(bolt.holeDia_mm),
                    geom.e2_mm,
                    GeomDef.get_e2_EC_min_dist_mm(bolt.holeDia_mm),
                    k1,
                    a_b,
                    self.gM2)
                )

    def F_bb_Rd_inner_N(self, bolt: Bolt, basemat: BaseMat, geom: GeomDef):
        if self.bBoltDistCheckStrict:
            if GeomDef.get_p1_EC_min_dist_mm(bolt.holeDia_mm) > geom.p1_mm:
                return (0.0, 'Zero from bolt p1 distance check')
            if GeomDef.get_p2_EC_min_dist_mm(bolt.holeDia_mm) > geom.p2_mm:
                return (0.0, 'Zero from bolt p2 distance check')
        k1 = max(0.0, min(1.4 * geom.p2_mm / bolt.holeDia_mm - 1.7, 2.5))
        a_b = max(0.0, min(geom.p1_mm / 3 / bolt.holeDia_mm - 1 / 4, bolt.fub_MPa / basemat.fu_MPa, 1))
        resVal = k1 * a_b * basemat.fu_MPa * bolt.dia_mm * basemat.t_mm / self.gM2
        resVal = resVal * int(geom.p1_mm >= bolt.holeDia_mm)
        resVal = resVal * int(geom.p2_mm >= bolt.holeDia_mm)
        return (resVal,
                'd:{}, d0:{}, f.ub:{}, f.u:{}, t:{}, p1:{}>{:.2f}, p2:{}>{:.2f}, k1:{:.2f}, a_b:{:.2f}, gM2:{}'.format(
                    bolt.dia_mm,
                    bolt.holeDia_mm,
                    bolt.fub_MPa,
                    basemat.fu_MPa,
                    basemat.t_mm,
                    geom.p1_mm,
                    GeomDef.get_p1_EC_min_dist_mm(bolt.holeDia_mm),
                    geom.p2_mm,
                    GeomDef.get_p2_EC_min_dist_mm(bolt.holeDia_mm),
                    k1,
                    a_b,
                    self.gM2)
                )

    def F_bt_Rd_N(self, bolt: Bolt):
        return (0.9 * bolt.fub_MPa * bolt.shearArea_mm2 / self.gM2,
                'd:{}, fub:{}, A:{}, gM2:{}'.format(
                    bolt.dia_mm,
                    bolt.fub_MPa,
                    bolt.shearArea_mm2,
                    self.gM2)
                )

    def B_bp_Rd_N(self, bolt: Bolt, basemat: BaseMat, geom: GeomDef):
        if self.bBoltDistCheckStrict:
            if GeomDef.get_e1_EC_min_dist_mm(bolt.holeDia_mm) > geom.e1_mm:
                return (0.0, 'Zero from bolt e1 distance check')
            if GeomDef.get_e2_EC_min_dist_mm(bolt.holeDia_mm) > geom.e2_mm:
                return (0.0, 'Zero from bolt e2 distance check')
            if GeomDef.get_p1_EC_min_dist_mm(bolt.holeDia_mm) > geom.p1_mm:
                return (0.0, 'Zero from bolt p1 distance check')
            if GeomDef.get_p2_EC_min_dist_mm(bolt.holeDia_mm) > geom.p2_mm:
                return (0.0, 'Zero from bolt p2 distance check')
        resVal = 0.6 * 3.14 * bolt.diaBM_mm * basemat.t_mm * basemat.fu_MPa / self.gM2
        delta = min(1,
                    (geom.e1_mm / GeomDef.get_e1_EC_min_dist_mm(bolt.holeDia_mm)) ** 2,
                    (geom.e2_mm / GeomDef.get_e2_EC_min_dist_mm(bolt.holeDia_mm)) ** 2,
                    (geom.p1_mm / GeomDef.get_p1_EC_min_dist_mm(bolt.holeDia_mm)) ** 2,
                    (geom.p2_mm / GeomDef.get_p2_EC_min_dist_mm(bolt.holeDia_mm)) ** 2
                    )
        return (resVal * delta,
                'd:{}, d0:{}, dbm:{}, f.ub:{}, f.u:{}, t:{}, e1:{}>{:.2f}, e2:{}>{:.2f}, p1:{}>{:.2f}, p2:{}>{:.2f}, res:{:.2f}, delta:{:.2f}, gM2:{}'.format(
                    bolt.dia_mm,
                    bolt.holeDia_mm,
                    bolt.diaBM_mm,
                    bolt.fub_MPa,
                    basemat.fu_MPa,
                    basemat.t_mm,
                    geom.e1_mm,
                    GeomDef.get_e1_EC_min_dist_mm(bolt.holeDia_mm),
                    geom.e2_mm,
                    GeomDef.get_e2_EC_min_dist_mm(bolt.holeDia_mm),
                    geom.p1_mm,
                    GeomDef.get_p1_EC_min_dist_mm(bolt.holeDia_mm),
                    geom.p2_mm,
                    GeomDef.get_p2_EC_min_dist_mm(bolt.holeDia_mm),
                    resVal,
                    delta,
                    self.gM2)
                )
