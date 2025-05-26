# Jupyter Notebook interativo com filtros e gráficos

import pandas as pd
import numpy as np
import json
import math
import re
import os
import matplotlib.pyplot as plt
import seaborn as sns
import ipywidgets as widgets
from IPython.display import display, clear_output

# Função para converter diversos formatos de dados em float
def to_float(val):
    if isinstance(val, (list, tuple)):
        for v in val:
            f = to_float(v)
            if not (pd.isna(f) or (isinstance(f, float) and math.isnan(f))):
                return f
        return np.nan
    if hasattr(val, '__iter__') and not isinstance(val, (str, bytes, int, float)):
        try:
            for v in val:
                f = to_float(v)
                if not (pd.isna(f) or (isinstance(f, float) and math.isnan(f))):
                    return f
        except TypeError:
            pass
    if pd.isna(val):
        return np.nan
    if isinstance(val, (int, float)):
        return float(val)
    if isinstance(val, str):
        try:
            return float(val.replace(',', '.'))
        except ValueError:
            txt = val.replace(',', '')
            m = re.search(r'-?\d+(?:\.\d+)?', txt)
            return float(m.group()) if m else np.nan
    return np.nan

# Caminho do arquivo JSON

data_path = r"g:\Meu Drive\mauro_projetos\seattle_lodging_projeto_final\seattle-lodging\data\dados_hospedagem.json"

if os.path.exists(data_path):
    with open(data_path, 'r', encoding='utf-8') as f:
        raw = json.load(f)
    if isinstance(raw, dict) and raw:
        df = pd.DataFrame(next(iter(raw.values())))
    elif isinstance(raw, list):
        df = pd.DataFrame(raw)
    else:
        df = pd.DataFrame()
else:
    print(f"Arquivo não encontrado: {data_path}")
    df = pd.DataFrame()

if not df.empty:
    money_cols = [c for c in ['preco', 'preco_noite', 'taxa_limpeza', 'taxa_deposito'] if c in df.columns]
    for col in money_cols:
        df[col] = df[col].apply(to_float)

    int_cols = [c for c in ['quantidade_quartos', 'quantidade_banheiros', 'quantidade_camas', 'max_hospedes'] if c in df.columns]
    for col in int_cols:
        df[col] = df[col].apply(to_float)

    if 'avaliacao_geral' in df.columns:
        df['avaliacao_geral'] = pd.to_numeric(df['avaliacao_geral'], errors='coerce')

    display(df.head())
    print("Correlação (Avaliação x Preço):")
    if 'avaliacao_geral' in df.columns and 'preco' in df.columns:
        df_corr = df[['avaliacao_geral', 'preco']].dropna()
        if df_corr.shape[0] > 1:
            correlation = df_corr['avaliacao_geral'].corr(df_corr['preco'])
            print(f"{correlation:.2f}")
        else:
            print("Dados insuficientes.")

    # Widgets interativos
    def update_plot(quartos):
        clear_output(wait=True)
        display(quartos_slider)
        df_filt = df[df['quantidade_quartos'] == quartos]
        plt.figure(figsize=(10, 5))
        sns.histplot(df_filt['preco'].dropna(), kde=True, bins=30)
        plt.title(f"Distribuição de Preço - {quartos} Quartos")
        plt.xlabel("Preço")
        plt.ylabel("Frequência")
        plt.grid(True)
        plt.tight_layout()
        plt.show()

    quartos_slider = widgets.IntSlider(
        value=1,
        min=int(df['quantidade_quartos'].min(skipna=True)),
        max=int(df['quantidade_quartos'].max(skipna=True)),
        step=1,
        description='Quartos:',
        continuous_update=False
    )

    widgets.interact(update_plot, quartos=quartos_slider)
else:
    print("DataFrame vazio. Corrija o carregamento do JSON.")
