import pandas as pd

dir = "G:\\My Drive\\TCC\\Database\\Anuario\\Dados\\Dados Estatísticos-20-10-2020.csv"

df = pd.read_csv(dir, sep=";", encoding='ISO-8859-1', decimal=",")

list_empresas = ["TAM", "GLO", "AZU", "VRG", "VRN", "VLO"]
#list_empresas = ["TAM"]


df_brasileira = df[df["EMPRESA (NACIONALIDADE)"] == "BRASILEIRA"]

df_brasileira = df_brasileira[df_brasileira["ANO"]>=2009]


list_anos = list(range(2009, 2020))
list_meses = list(range(1,13))

dict_data = {}

# for ano in list_anos:
#
#     dict_ano = {}
#
#     for mes in list_meses:
#
#         dict_mes = {}
#
#         for empresa in list_empresas:
#
#             dict_empresa = {}
#
#             ask_dom = df_brasileira[((df_brasileira["ANO"]==ano) & (df_brasileira["MÊS"]==mes) & (df_brasileira["EMPRESA (SIGLA)"]==empresa) & (df_brasileira["NATUREZA"]=="DOMÉSTICA"))]["ASK"].sum()
#             ask_int = df_brasileira[((df_brasileira["ANO"]==ano) & (df_brasileira["MÊS"]==mes) & (df_brasileira["EMPRESA (SIGLA)"]==empresa) & (df_brasileira["NATUREZA"]=="INTERNACIONAL"))]["ASK"].sum()
#             rpk_dom = df_brasileira[((df_brasileira["ANO"]==ano) & (df_brasileira["MÊS"]==mes) & (df_brasileira["EMPRESA (SIGLA)"]==empresa) & (df_brasileira["NATUREZA"]=="DOMÉSTICA"))]["RPK"].sum()
#             rpk_int = df_brasileira[((df_brasileira["ANO"]==ano) & (df_brasileira["MÊS"]==mes) & (df_brasileira["EMPRESA (SIGLA)"]==empresa) & (df_brasileira["NATUREZA"]=="INTERNACIONAL"))]["RPK"].sum()
#             atk_dom = df_brasileira[((df_brasileira["ANO"]==ano) & (df_brasileira["MÊS"]==mes) & (df_brasileira["EMPRESA (SIGLA)"]==empresa) & (df_brasileira["NATUREZA"]=="DOMÉSTICA"))]["ATK"].sum()
#             atk_int = df_brasileira[((df_brasileira["ANO"]==ano) & (df_brasileira["MÊS"]==mes) & (df_brasileira["EMPRESA (SIGLA)"]==empresa) & (df_brasileira["NATUREZA"]=="INTERNACIONAL"))]["ATK"].sum()
#             rtk_dom = df_brasileira[((df_brasileira["ANO"]==ano) & (df_brasileira["MÊS"]==mes) & (df_brasileira["EMPRESA (SIGLA)"]==empresa) & (df_brasileira["NATUREZA"]=="DOMÉSTICA"))]["RTK"].sum()
#             rtk_int = df_brasileira[((df_brasileira["ANO"]==ano) & (df_brasileira["MÊS"]==mes) & (df_brasileira["EMPRESA (SIGLA)"]==empresa) & (df_brasileira["NATUREZA"]=="INTERNACIONAL"))]["RTK"].sum()
#             comb_dom = df_brasileira[((df_brasileira["ANO"]==ano) & (df_brasileira["MÊS"]==mes) & (df_brasileira["EMPRESA (SIGLA)"]==empresa) & (df_brasileira["NATUREZA"]=="DOMÉSTICA"))]["COMBUSTÍVEL (LITROS)"].sum()
#             comb_int = df_brasileira[((df_brasileira["ANO"]==ano) & (df_brasileira["MÊS"]==mes) & (df_brasileira["EMPRESA (SIGLA)"]==empresa) & (df_brasileira["NATUREZA"]=="INTERNACIONAL"))]["COMBUSTÍVEL (LITROS)"].sum()
#             decolagens_dom = df_brasileira[((df_brasileira["ANO"]==ano) & (df_brasileira["MÊS"]==mes) & (df_brasileira["EMPRESA (SIGLA)"]==empresa) &  (df_brasileira["NATUREZA"]=="DOMÉSTICA"))]["DECOLAGENS"].sum()
#             decolagens_int = df_brasileira[((df_brasileira["ANO"]==ano) & (df_brasileira["MÊS"]==mes) & (df_brasileira["EMPRESA (SIGLA)"]==empresa) & (df_brasileira["NATUREZA"]=="INTERNACIONAL"))]["DECOLAGENS"].sum()
#             hrvoo_dom = df_brasileira[((df_brasileira["ANO"]==ano) & (df_brasileira["MÊS"]==mes) & (df_brasileira["EMPRESA (SIGLA)"]==empresa) & (df_brasileira["NATUREZA"]=="DOMÉSTICA"))]["HORAS VOADAS"].sum()
#             hrvoo_int = df_brasileira[((df_brasileira["ANO"]==ano) & (df_brasileira["MÊS"]==mes) & (df_brasileira["EMPRESA (SIGLA)"]==empresa) & (df_brasileira["NATUREZA"]=="INTERNACIONAL"))]["HORAS VOADAS"].sum()
#
#             dict_empresa = {"ASK_DOM":ask_dom,
#                             "ASK_INT":ask_int,
#                             "RPK_DOM":rpk_dom,
#                             "RPK_INT":rpk_int,
#                             "ATK_DOM":atk_dom,
#                             "ATK_INT":atk_int,
#                             "RTK_DOM":rtk_dom,
#                             "RTK_INT":rtk_int,
#                             "COMB_DOM":comb_dom,
#                             "COMB_INT":comb_int,
#                             "DEC_DOM":decolagens_dom,
#                             "DEC_INT":decolagens_int,
#                             "HRVOO_DOM":hrvoo_dom,
#                             "HRVOO_INT":hrvoo_int}
#
#             dict_mes[empresa] = dict_empresa
#
#         dict_ano[mes] = dict_mes
#
#     dict_data[ano] = dict_ano
#
#


df_consolidada = pd.DataFrame(columns=["ANO","MÊS","EMPRESA", "ASK_DOM", "ASK_INT", "RPK_DOM","RPK_INT","ATK_DOM","ATK_INT","RTK_DOM","RTK_INT","COMB_DOM","COMB_INT","DEC_DOM","DEC_INT","HRVOO_DOM","HRVOO_INT","DIST_DOM","DIST_INT", "PASSPG_DOM", "PASSPG_INT", "PASSGRA_DOM", "PASSGRA_INT"])

for ano in list_anos:
    for mes in list_meses:
        for empresa in list_empresas:

            ask_dom = df_brasileira[((df_brasileira["ANO"]==ano) & (df_brasileira["MÊS"]==mes) & (df_brasileira["EMPRESA (SIGLA)"]==empresa) & (df_brasileira["NATUREZA"]=="DOMÉSTICA"))]["ASK"].sum()
            ask_int = df_brasileira[((df_brasileira["ANO"]==ano) & (df_brasileira["MÊS"]==mes) & (df_brasileira["EMPRESA (SIGLA)"]==empresa) & (df_brasileira["NATUREZA"]=="INTERNACIONAL"))]["ASK"].sum()
            rpk_dom = df_brasileira[((df_brasileira["ANO"]==ano) & (df_brasileira["MÊS"]==mes) & (df_brasileira["EMPRESA (SIGLA)"]==empresa) & (df_brasileira["NATUREZA"]=="DOMÉSTICA"))]["RPK"].sum()
            rpk_int = df_brasileira[((df_brasileira["ANO"]==ano) & (df_brasileira["MÊS"]==mes) & (df_brasileira["EMPRESA (SIGLA)"]==empresa) & (df_brasileira["NATUREZA"]=="INTERNACIONAL"))]["RPK"].sum()
            atk_dom = df_brasileira[((df_brasileira["ANO"]==ano) & (df_brasileira["MÊS"]==mes) & (df_brasileira["EMPRESA (SIGLA)"]==empresa) & (df_brasileira["NATUREZA"]=="DOMÉSTICA"))]["ATK"].sum()
            atk_int = df_brasileira[((df_brasileira["ANO"]==ano) & (df_brasileira["MÊS"]==mes) & (df_brasileira["EMPRESA (SIGLA)"]==empresa) & (df_brasileira["NATUREZA"]=="INTERNACIONAL"))]["ATK"].sum()
            rtk_dom = df_brasileira[((df_brasileira["ANO"]==ano) & (df_brasileira["MÊS"]==mes) & (df_brasileira["EMPRESA (SIGLA)"]==empresa) & (df_brasileira["NATUREZA"]=="DOMÉSTICA"))]["RTK"].sum()
            rtk_int = df_brasileira[((df_brasileira["ANO"]==ano) & (df_brasileira["MÊS"]==mes) & (df_brasileira["EMPRESA (SIGLA)"]==empresa) & (df_brasileira["NATUREZA"]=="INTERNACIONAL"))]["RTK"].sum()
            comb_dom = df_brasileira[((df_brasileira["ANO"]==ano) & (df_brasileira["MÊS"]==mes) & (df_brasileira["EMPRESA (SIGLA)"]==empresa) & (df_brasileira["NATUREZA"]=="DOMÉSTICA"))]["COMBUSTÍVEL (LITROS)"].sum()
            comb_int = df_brasileira[((df_brasileira["ANO"]==ano) & (df_brasileira["MÊS"]==mes) & (df_brasileira["EMPRESA (SIGLA)"]==empresa) & (df_brasileira["NATUREZA"]=="INTERNACIONAL"))]["COMBUSTÍVEL (LITROS)"].sum()
            decolagens_dom = df_brasileira[((df_brasileira["ANO"]==ano) & (df_brasileira["MÊS"]==mes) & (df_brasileira["EMPRESA (SIGLA)"]==empresa) &  (df_brasileira["NATUREZA"]=="DOMÉSTICA"))]["DECOLAGENS"].sum()
            decolagens_int = df_brasileira[((df_brasileira["ANO"]==ano) & (df_brasileira["MÊS"]==mes) & (df_brasileira["EMPRESA (SIGLA)"]==empresa) & (df_brasileira["NATUREZA"]=="INTERNACIONAL"))]["DECOLAGENS"].sum()
            hrvoo_dom = df_brasileira[((df_brasileira["ANO"]==ano) & (df_brasileira["MÊS"]==mes) & (df_brasileira["EMPRESA (SIGLA)"]==empresa) & (df_brasileira["NATUREZA"]=="DOMÉSTICA"))]["HORAS VOADAS"].sum()
            hrvoo_int = df_brasileira[((df_brasileira["ANO"]==ano) & (df_brasileira["MÊS"]==mes) & (df_brasileira["EMPRESA (SIGLA)"]==empresa) & (df_brasileira["NATUREZA"]=="INTERNACIONAL"))]["HORAS VOADAS"].sum()
            dist_dom = df_brasileira[((df_brasileira["ANO"]==ano) & (df_brasileira["MÊS"]==mes) & (df_brasileira["EMPRESA (SIGLA)"]==empresa) & (df_brasileira["NATUREZA"]=="DOMÉSTICA"))]["DISTÂNCIA VOADA (KM)"].sum()
            dist_int = df_brasileira[((df_brasileira["ANO"]==ano) & (df_brasileira["MÊS"]==mes) & (df_brasileira["EMPRESA (SIGLA)"]==empresa) & (df_brasileira["NATUREZA"]=="INTERNACIONAL"))]["DISTÂNCIA VOADA (KM)"].sum()
            passpg_dom = df_brasileira[((df_brasileira["ANO"]==ano) & (df_brasileira["MÊS"]==mes) & (df_brasileira["EMPRESA (SIGLA)"]==empresa) & (df_brasileira["NATUREZA"]=="DOMÉSTICA"))]["PASSAGEIROS PAGOS"].sum()
            passgra_dom = df_brasileira[((df_brasileira["ANO"]==ano) & (df_brasileira["MÊS"]==mes) & (df_brasileira["EMPRESA (SIGLA)"]==empresa) & (df_brasileira["NATUREZA"]=="DOMÉSTICA"))]["PASSAGEIROS GRÁTIS"].sum()
            passpg_int = df_brasileira[((df_brasileira["ANO"]==ano) & (df_brasileira["MÊS"]==mes) & (df_brasileira["EMPRESA (SIGLA)"]==empresa) & (df_brasileira["NATUREZA"]=="INTERNACIONAL"))]["PASSAGEIROS PAGOS"].sum()
            passgra_int = df_brasileira[((df_brasileira["ANO"]==ano) & (df_brasileira["MÊS"]==mes) & (df_brasileira["EMPRESA (SIGLA)"]==empresa) & (df_brasileira["NATUREZA"]=="INTERNACIONAL"))]["PASSAGEIROS GRÁTIS"].sum()


            list_append = [ano,mes,empresa,ask_dom,ask_int,rpk_dom,rpk_int,atk_dom,atk_int,rtk_dom,rtk_int,comb_dom,comb_int,decolagens_dom,decolagens_int,hrvoo_dom,hrvoo_int,dist_dom,dist_int, passpg_dom, passpg_int, passgra_dom, passgra_int]
            series_append = pd.Series(list_append, index=df_consolidada.columns)
            df_consolidada = df_consolidada.append(series_append, ignore_index=True)


df_consolidada.to_csv("G:\\My Drive\\TCC\\Database\\Anuario\\Dados\\dados_consolidados_final_2020-10-20.csv", sep=";", encoding='ISO-8859-1', decimal=".")
