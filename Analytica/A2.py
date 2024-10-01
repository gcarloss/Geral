import pandas as pd
import matplotlib.pyplot as plt

df_taxa_motorizacao = pd.read_csv(r"D:\Gabriel\Documents\UFRJ\Analytica\br_mobilidados_indicadores_taxa_motorizacao.csv")
df_transporte_proximo = pd.read_csv(r"D:\Gabriel\Documents\UFRJ\Analytica\br_mobilidados_indicadores_proporcao_pessoas_proximas_pnt.csv")
df_divisao_modal = pd.read_csv(r"D:\Gabriel\Documents\UFRJ\Analytica\br_mobilidados_indicadores_divisao_modal.csv")
df_comprometimento_renda = pd.read_csv(r"D:\Gabriel\Documents\UFRJ\Analytica\br_mobilidados_indicadores_comprometimento_renda_tarifa_transp_publico.csv")
df_IBGE = pd.read_csv(r"D:\Gabriel\Documents\UFRJ\Analytica\br_bd_diretorios_brasil_municipio.csv")


# Verificar os cabeçalhos dos arquivos
print(df_taxa_motorizacao.head())
print(df_IBGE.head())

# Fazer o merge utilizando a coluna de código IBGE comum
df_merged = pd.merge(df_taxa_motorizacao, df_IBGE, how='left', left_on='id_municipio', right_on='codigo_ibge_ibge')

# # 1. Análise da Taxa de Motorização
# def analise_taxa_motorizacao(df):
#     # Tendências de Motorização
#     df_grouped = df.groupby('ano')['taxa_motorizacao'].mean().reset_index()
    
#     plt.figure(figsize=(10, 6))
#     plt.plot(df_grouped['ano'], df_grouped['taxa_motorizacao'], marker='o')
#     plt.title('Tendência da Taxa de Motorização (2001 a 2018)')
#     plt.xlabel('Ano')
#     plt.ylabel('Taxa de Motorização Média')
#     plt.grid()
#     plt.show()
    
#     # Comparação entre Capitais
#     capitais = df['capital'].unique()
#     for capital in capitais:
#         dados_capital = df[df['capital'] == capital]
#         plt.plot(dados_capital['ano'], dados_capital['taxa_motorizacao'], marker='o', label=capital)
    
#     plt.title('Taxa de Motorização por Capital')
#     plt.xlabel('Ano')
#     plt.ylabel('Taxa de Motorização')
#     plt.legend()
#     plt.grid()
#     plt.show()

# analise_taxa_motorizacao(df_taxa_motorizacao)