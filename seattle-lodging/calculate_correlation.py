import pandas as pd
import numpy as np
import json
import math
import re

# Recriar a função to_float e carregar os dados como no notebook
def to_float(val):
    if isinstance(val, (list, tuple)):
        for v in val:
            f = to_float(v)
            if not (pd.isna(f) or math.isnan(f)):
                return f
        return np.nan
    if hasattr(val, '__iter__') and not isinstance(val, (str, bytes, int, float)):
        try:
            for v in val:
                f = to_float(v)
                if not (pd.isna(f) or math.isnan(f)):
                    return f
        except TypeError:
            pass
    if pd.isna(val):
        return np.nan
    if isinstance(val, (int, float)):
        return float(val)
    txt = str(val).replace(',', '')
    m = re.search(r'-?\d+(?:\.\d+)?', txt)
    return float(m.group()) if m else np.nan

data_path = '/home/ubuntu/seattle-lodging/data/dados_hospedagem.json'
with open(data_path, 'r', encoding='utf-8') as f:
    raw = json.load(f)
df = pd.DataFrame(next(iter(raw.values())) if isinstance(raw, dict) else raw)

money_cols = [c for c in ['preco', 'preco_noite', 'taxa_limpeza', 'taxa_deposito'] if c in df.columns]
for col in money_cols:
    df[col] = df[col].apply(to_float)

int_cols = [c for c in ['quantidade_quartos', 'quantidade_banheiros', 'quantidade_camas', 'max_hospedes'] if c in df.columns]
for col in int_cols:
    df[col] = df[col].apply(to_float)

if 'avaliacao_geral' in df.columns:
    df['avaliacao_geral'] = pd.to_numeric(df['avaliacao_geral'], errors='coerce')

# Calcular a correlação entre 'avaliacao_geral' e 'preco'
correlation = df['avaliacao_geral'].corr(df['preco'])
print(f"Correlação entre avaliação geral e preço: {correlation:.2f}")

