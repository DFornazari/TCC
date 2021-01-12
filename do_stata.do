import excel "G:\My Drive\TCC\Vers. Alt\custos total.xlsx", sheet("LN_TAM") firstrow clear
tsset T
regress CT ASK PRC_MED_TRA CST_COMB CST_CAP TAR_POR_DEC OUT_POR_RPK LOD_FAC ETA_MED T
constraint define 1 PRC_MED_TRA + CST_COMB + CST_CAP + TAR_POR_DEC + OUT_POR_RPK = 1
cnsreg CT ASK PRC_MED_TRA CST_COMB CST_CAP TAR_POR_DEC OUT_POR_RPK LOD_FAC ETA_MED T, constraints(1)
import excel "G:\My Drive\TCC\Vers. Alt\custos total.xlsx", sheet("LN_GLO") firstrow clear
tsset T
regress CT ASK PRC_MED_TRA CST_COMB CST_CAP TAR_POR_DEC OUT_POR_RPK LOD_FAC ETA_MED T
constraint define 1 PRC_MED_TRA + CST_COMB + CST_CAP + TAR_POR_DEC + OUT_POR_RPK = 1
cnsreg CT ASK PRC_MED_TRA CST_COMB CST_CAP TAR_POR_DEC OUT_POR_RPK LOD_FAC ETA_MED T, constraints(1)
import excel "G:\My Drive\TCC\Vers. Alt\custos total.xlsx", sheet("LN_AZU") firstrow clear
tsset T
regress CT ASK PRC_MED_TRA CST_COMB CST_CAP TAR_POR_DEC OUT_POR_RPK LOD_FAC ETA_MED T
constraint define 1 PRC_MED_TRA + CST_COMB + CST_CAP + TAR_POR_DEC + OUT_POR_RPK = 1
cnsreg CT ASK PRC_MED_TRA CST_COMB CST_CAP TAR_POR_DEC OUT_POR_RPK LOD_FAC ETA_MED T, constraints(1)
import excel "G:\My Drive\TCC\Vers. Alt\custos total.xlsx", sheet("LN_DADOS") firstrow clear
tsset K T
xtreg CT ASK PRC_MED_TRA CST_COMB CST_CAP TAR_POR_DEC OUT_POR_RPK LOD_FAC ETA_MED TAM AZU GLO T
