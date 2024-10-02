import pandas as pd
import matplotlib.pyplot as plt

df_taxa_motorizacao = pd.read_csv(r"D:\Gabriel\Documents\UFRJ\Analytica\br_mobilidados_indicadores_taxa_motorizacao.csv")
df_transporte_proximo = pd.read_csv(r"D:\Gabriel\Documents\UFRJ\Analytica\br_mobilidados_indicadores_proporcao_pessoas_proximas_pnt.csv")
df_divisao_modal = pd.read_csv(r"D:\Gabriel\Documents\UFRJ\Analytica\br_mobilidados_indicadores_divisao_modal.csv")
df_comprometimento_renda = pd.read_csv(r"D:\Gabriel\Documents\UFRJ\Analytica\br_mobilidados_indicadores_comprometimento_renda_tarifa_transp_publico.csv")
df_IBGE = pd.read_csv(r"D:\Gabriel\Documents\UFRJ\Analytica\br_bd_diretorios_brasil_municipio.csv")


# Verificar os cabeçalhos dos arquivos
# print(df_taxa_motorizacao.head())
print(df_transporte_proximo.head())

# 1. Análise da Taxa de Motorização
def analise_taxa_motorizacao(df):
    # Filtrar apenas os dados do Rio de Janeiro (RJ)
    df_rj = df[df['sigla_uf'] == 'RJ']
    
    # Tendências de Motorização no RJ
    df_grouped = df_rj.groupby('ano')['taxa_motorizacao'].mean().reset_index()

    # Plotando o gráfico
    plt.figure(figsize=(10, 6))
    plt.plot(df_grouped['ano'], df_grouped['taxa_motorizacao'], marker='o')
    plt.title('Tendência da Taxa de Motorização no RJ (2001 a 2018)')
    plt.xlabel('Ano')
    plt.ylabel('Taxa de Motorização Média no RJ')
    plt.grid()
    plt.show()

# Executar a análise
analise_taxa_motorizacao(df_taxa_motorizacao)


# # 2. Análise do Percentual de Pessoas Próximas à Rede de Transporte (PNT)
# def analise_pnt(df):
#     # Filtrar os dados do Rio de Janeiro (RJ)
#     df_rj = df[df['sigla_uf'] == 'RJ']
    
#     # Agrupando os dados por ano
#     df_grouped = df_rj.groupby('ano')['percentual_pessoas_proximas_transporte'].mean().reset_index()

#     # Plotando o gráfico
#     plt.figure(figsize=(10, 6))
#     plt.plot(df_grouped['ano'], df_grouped['percentual_pessoas_proximas_transporte'], marker='o')
#     plt.title('Percentual de Pessoas Próximas à Rede de Transporte no RJ (2010 a 2019)')
#     plt.xlabel('Ano')
#     plt.ylabel('Percentual de Pessoas (%)')
#     plt.grid()
#     plt.show()

# # Executar a análise
# analise_pnt(df_transporte_proximo)
